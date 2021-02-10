# Progressive Samplers



[![Python version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue.svg?style=for-the-badge)](https://pypi.org/project/kedro/) 
[![Version](https://img.shields.io/pypi/v/prosamplers?style=for-the-badge)](https://pypi.org/project/prosamplers/) 
[![codecov](https://img.shields.io/codecov/c/gh/ELC/prosamplers/master?style=for-the-badge&token=24HLR6VMK2)](https://codecov.io/gh/ELC/prosamplers) 
[![Master](https://img.shields.io/github/checks-status/ELC/prosamplers/master?label=Master&style=for-the-badge)](https://github.com/ELC/progressive-samplers/actions?query=workflow%3A%22Build%2C+Test+and+Deploy%22)
[![Develop](https://img.shields.io/github/checks-status/ELC/prosamplers/develop?label=develop&style=for-the-badge)](https://github.com/ELC/prosamplers/actions?query=workflow%3A%22Build+and+Test%22)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=for-the-badge)](https://github.com/ELC/prosamplers/blob/master/LICENSE)

Collection of progressive samplers for general use, mainly for Hyperparameter search

# Install using pip

`pip install prosamplers`

# Frequently Asked Questions

Some terminology explanations

### What is a sampler?

A sampler is a method / algorithm that generates a sequence of points in a given search space

### What is progressive?

A progressive sampler allows generating points on a point-by-point basis and does not required to say in advance how many points there need to be. They allow to ask for more points indefinetely, some only have a minimal memory footprint whereas other require complex memory mechanism

### Why we need Progressive Samplers?

Most use cases may be solve with a simple Grid or Random search, but when dimensionality is not huge (< 100 or so dimensions) and the computation time for each point is really expensive, this alternative sampling methods could outperform naive methods as Grid or Random Search. As dimensionality increases, results tend to converge to those of Random Search

# Usage

```
1+1
```




    2


