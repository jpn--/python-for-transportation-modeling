# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages

def version(path):
    """Obtain the packge version from a python file e.g. pkg/__init__.py
    See <https://packaging.python.org/en/latest/single_source_version.html>.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, path), encoding='utf-8') as f:
        version_file = f.read()
    version_match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

VERSION = version('transportation_tutorials/__init__.py')

with open('requirements.txt') as f:
    requirements_lines = f.readlines()

install_requires = [r.strip() for r in requirements_lines]

setup(
    name='transportation_tutorials',
    version=VERSION,
    packages=find_packages(),
    package_data={
        # If sub-package contains these types of files, include them:
        'transportation_tutorials': [
            'data/*.yml',
            'data/*.csv',
            'data/*.csv.gz',
            'data/*.tar.gz',
            'data/*.dbf.gz',
            'data/*.omx',
        ],
    },
    install_requires=install_requires,
)

