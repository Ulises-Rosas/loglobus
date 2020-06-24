#!/usr/bin/env python3

import setuptools
from distutils.core import setup

setup(
    name    = "loglobus",
    version = "0.1",
    packages = ["transfer"],
    package_dir  = {"transfer" : "src"},
    entry_points = {
        'console_scripts': [
            'transferdirs = transfer.transferdirs:main'
        ]
    },
    classifiers = [
        'Programming Language :: Python :: 3'
        ]
    )