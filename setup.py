#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'c2c.recipe.msgfmt',
    version = '0.2.1',
    license = 'MIT License',

    author  = 'Frederic Junod',
    author_email = 'frederic.junod@camptocamp.com',
    url = 'http://github.com/fredj/c2c.recipe.msgfmt',

    description = 'A buildout recipe to compile message catalog to binary format.',
    long_description = open('README').read(),

    classifiers = [
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],

    zip_safe = False, 
    install_requires = ['zc.buildout', 'Babel'],
    packages = find_packages(exclude=['ez_setup']),
    namespace_packages = ['c2c', 'c2c.recipe'],
    entry_points = {'zc.buildout' : ['default = c2c.recipe.msgfmt.buildout:CompileMo']}
)
