#!/usr/bin/env python
"""Paul's Qiskit Addons

Addons for IBM Q Qiskit that are helpful for doing stuff.
"""

DOCLINES = __doc__.split('\n')

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
License :: OSI Approved :: Apache 2 License
Programming Language :: Python :: 3
Topic :: Scientific/Engineering
Operating System :: MacOS
Operating System :: POSIX
Operating System :: Unix
Operating System :: Microsoft :: Windows
"""

# import statements
import os
import sys
from setuptools import setup, Extension

# all information about QuTiP goes here
MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
REQUIRES = ['qiskit (>=0.8)']
INSTALL_REQUIRES = []
PACKAGES = ['pauls_qiskit_addons',
            'pauls_qiskit_addons/backends']
PACKAGE_DATA = {}

NAME = "pauls_qiskit_addons"
AUTHOR = ("Paul D. Nation")
AUTHOR_EMAIL = ("paul.nation@ibm.com")
LICENSE = "Apache 2"
DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = "\n".join(DOCLINES[2:])
KEYWORDS = "qiskit"
URL = "https://qiskit.org"
CLASSIFIERS = [_f for _f in CLASSIFIERS.split('\n') if _f]
PLATFORMS = ["Linux", "Mac OSX", "Unix", "Windows"]


def git_short_hash():
    try:
        git_str = "+" + os.popen('git log -1 --format="%h"').read().strip()
    except:
        git_str = ""
    else:
        if git_str == '+': #fixes setuptools PEP issues with versioning
            git_str = ''
    return git_str

FULLVERSION = VERSION
if not ISRELEASED:
    FULLVERSION += '.dev'+str(MICRO)+git_short_hash()


def write_version_py(filename='pauls_qiskit_addons/version.py'):
    cnt = """\
# THIS FILE IS GENERATED FROM PAULS_QISKIT_ADDONS SETUP.PY
short_version = '%(version)s'
version = '%(fullversion)s'
release = %(isrelease)s
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION, 'fullversion':
                FULLVERSION, 'isrelease': str(ISRELEASED)})
    finally:
        a.close()

local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(local_path)
sys.path.insert(0, local_path)
sys.path.insert(0, os.path.join(local_path, 'pauls_qiskit_addons'))

# always rewrite _version
if os.path.exists('pauls_qiskit_addons/version.py'):
    os.remove('pauls_qiskit_addons/version.py')

write_version_py()


# Setup commands go here
setup(
    name = NAME,
    version = FULLVERSION,
    packages = PACKAGES,
    include_package_data=True,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    license = LICENSE,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    keywords = KEYWORDS,
    url = URL,
    classifiers = CLASSIFIERS,
    platforms = PLATFORMS,
    requires = REQUIRES,
    package_data = PACKAGE_DATA,
    zip_safe = False,
    install_requires=INSTALL_REQUIRES
)
