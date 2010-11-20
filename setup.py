#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setuptools import
from setuptools import setup, find_packages

# bewype import
from bewype import __version__ as version

setup(
    name="bewype.flask.controllers",
    version=version,
    author="Florent Pigout",
    author_email="florent.pigout@bewype.org",
    description="Bewype Flask Controllers",
    long_description="",
    license = "MIT",
    url="http://www.bewype.org",
    packages=find_packages(exclude=[]),
    package_data = {},
    data_files=["COPYING"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "Flask"
        ],
    namespace_packages=[
            "bewype.flask.controllers",
            ],
    entry_points={},
    test_suite = "bewype.flask.controllers.tests",
    )

