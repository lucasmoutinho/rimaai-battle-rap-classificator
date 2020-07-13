#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup


setup(
    name='battle_rap_classificator',
    version='0.1',
    description='Classificador para batalhas rap',
    author='Rima AI',
    author_email='lucas.moutinho@vert.com.br',
    url='https://github.com/lucasmoutinho/rimaai-battle-rap-classificator',
    packages=['battle_rap_classificator'],
    install_requires=[],
)
