# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

from tisea import __version__

here = os.path.dirname(__file__)
packages = find_packages(exclude=["docs", "examples", "tests"])


def read_readme(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def read_requirements(filename="requirements.txt"):
    requirements_path = os.path.join(here, filename)

    try:
        with open(requirements_path) as f:
            requirements = f.read().strip().split("\n")
    except FileNotFoundError:
        return []

    def modify_dependency_links(requirement):
        if "://" not in requirement:
            return requirement
        package = requirement.split("egg=")[-1]
        if package.split("-")[-1][0].isdigit():
            # check if version included e.g. package-name-1.3.0
            package = "0".join(package.split("-")[:-1])
        return f"{package} @ {requirement}"

    # Filter away commented out. ideally should use a regex
    requirements = [
        modify_dependency_links(r)
        for r in requirements
        if not (r.startswith("//") or r.startswith("#"))
    ]
    return requirements


setup(
    name="tisea",
    version=__version__,
    author="Ha Quan Nguyen",
    author_email="quan.ngha95@gmail.com",
    description="This is the package for Time Series Analysis",
    long_description=read_readme("README.md"),
    long_description_content_type="text/markdown",
    # package_dir={"": "src"}, # alr use find_packages()
    packages=packages,
    # requirements.txt
    install_requires=read_requirements("requirements.txt"),
    # install including interactive option
    # pip install -e ".[interactive, dev]"
    extras_require={
        # "interactive": [],
        "dev": read_requirements("requirements-dev.txt"),
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
)
