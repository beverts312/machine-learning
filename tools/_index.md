---
title: Tools
type: docs
---

I have dockerized a number of open source tools for machine learning and data science. 
For each tool you will find a `docker-compose.yml`, `Dockerfile`, and an `info.yml`. 
The `info.yml` provides a standardized view of how to leverage the tool.
I have written scripts that use the information defined int he `info.yml` files to make the tools easy to use in a consistent manner.

## Getting Started
In order for the scripts to work, you will need to install the following:
* python3/pip3/virtualenv (then run `pip3 install -r requirements.txt` or `pip3 install -r dev-requirements.txt` for development)
* docker+docker-compose
* [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

An interactive script ([prepare.py](../bails_ml_wrappers/prepare.py)) is provided to help:
* initialize volume directories used by the tools
* download required datasets/models/checkpoints

## Docker

**If you are using these for production or dont want bloat I would reccomend using your own images, these images are geared towards making things easy, not optimized**

The compose file in each tool directory knows how to build the images (which are not currently on docker hub).
All of the tools extend one of the base images defined in this repo:
* [beverts312/mlbase](../mlbase/Dockerfile) - Based off `nvidia/cuda`, installs conda, common build tools, and sets up a non-root user `mluser`
* [beverts312/machine-learning](../Dockerfile) - Based off `beverts312/mlbase`, includes pytorch

Alot of data is downloaded in the course of building these images, if you need to share them across multiple machines in a local network I would reccomend using a local registry ([example config](https://github.com/beverts312/dev-env/blob/main/docker-envs/registry/docker-compose.yml)).