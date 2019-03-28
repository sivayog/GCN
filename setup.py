# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:12:25 2019

@author: sivaj
"""

from setuptools import setup
from setuptools import find_packages

setup(name='gcn',
      version='1.0',
      description='Graph Convolutional Networks in Tensorflow',
      install_requires=['numpy',
                        'tensorflow',
                        'networkx',
                        'scipy'
                        ],
      package_data={'gcn': ['README.md']},
      packages=find_packages())