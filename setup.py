#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

# the name of the package
name = 'qtconsole'

#-----------------------------------------------------------------------------
# Minimal Python version sanity check
#-----------------------------------------------------------------------------

import sys

v = sys.version_info
if v[:2] < (2,7) or (v[0] >= 3 and v[:2] < (3,3)):
    error = "ERROR: %s requires Python version 2.7 or 3.3 or above." % name
    print(error, file=sys.stderr)
    sys.exit(1)

PY3 = (sys.version_info[0] >= 3)

#-----------------------------------------------------------------------------
# get on with it
#-----------------------------------------------------------------------------

from glob import glob
import io
import os

from setuptools import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

packages = []
for d, _, _ in os.walk(pjoin(here, name)):
    if os.path.exists(pjoin(d, '__init__.py')):
        packages.append(d[len(here)+1:].replace(os.path.sep, '.'))

package_data = {
    'qtconsole' : ['resources/icon/*.svg'],
}

version_ns = {}
with open(pjoin(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup_args = dict(
    name                          = name,
    version                       = version_ns['__version__'],
    scripts                       = glob(pjoin('scripts', '*')),
    packages                      = packages,
    package_data                  = package_data,
    description                   = "Jupyter Qt console",
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    author                        = 'Jupyter Development Team',
    author_email                  = 'jupyter@googlegroups.com',
    maintainer                    = 'Spyder Development Team',
    url                           = 'http://jupyter.org',
    license                       = 'BSD',
    platforms                     = "Linux, Mac OS X, Windows",
    keywords                      = ['Interactive', 'Interpreter', 'Shell'],
    install_requires = [
        'traitlets',
        'ipython_genutils',
        'jupyter_core',
        'jupyter_client>=4.1',
        'pygments',
        'ipykernel>=4.1', # not a real dependency, but require the reference kernel
        'qtpy',
    ],
    extras_require = {
        'test': ['pytest'],
        'test:python_version=="2.7"': ['mock'],
        'doc': 'Sphinx>=1.3',
    },
    entry_points = {
        'gui_scripts': [
            'jupyter-qtconsole = qtconsole.qtconsoleapp:main',
        ]
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
