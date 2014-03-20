#!/usr/bin/env python

from setuptools import setup

setup(
    name='csv2vcd',
    version='1.0',
    description=
    'Signal analyzer CSV to IEEE 1364-2001 VCD file format converter',
    author='Carlos Jenkins',
    author_email='carlos@jenkins.co.cr',
    url='https://github.com/carlos-jenkins/csv2vcd',
    #packages=['csv2vcd'],
    #package_dir={'': 'lib'},
    scripts=['bin/csv2vcd'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
    #test_suite='test',
    setup_requires=[
        'flake8'
    ]
)
