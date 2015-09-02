#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='guest',
    version='1.0',
    license='Private',
    description='Guest bbs: modern modular telnet bbs',
    author='matao.xjtu@gmail.com',
    packages=find_packages('.'),
    install_requires=['eventlet', 'mongoengine'],
    entry_points='''
    [console_scripts]
    guest=guest.app:main
    ''',
)
