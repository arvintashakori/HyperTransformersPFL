from io import open
from os import path
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# get reqs
def requirements():
    list_requirements = []
    with open('requirements.txt') as f:
        for line in f:
            list_requirements.append(line.rstrip())
    return list_requirements

setup(
      name='HyperTransformersPFL',
      version='1.0.0',
      description='HyperTransformersPFL: Heterogeneity-Robust Personalized Federated Learning with Vision Transformers using Hypernetwork-based Pruning',
      url='https://github.com/arvintashakori/HyperTransformersPFL',
      author='Arvin Tashakori',
      license='All rights reserved for Arvin Tashakori 2023-2024',
      author_email='arvin@ece.ubc.ca',
      packages=find_packages(exclude=['']),
      python_requires='>=3.8',
      install_requires=requirements()
)