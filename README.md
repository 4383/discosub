# discosub 0.1.15

![build status for master branch](https://travis-ci.org/4383/discosub.svg?branch=master) (master) 
![build status for development branch](https://travis-ci.org/4383/discosub.svg?branch=development) (development)

![official pypi package](https://badge.fury.io/py/discosub.svg)
[![PyPI](https://img.shields.io/pypi/l/discosub.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/wheel/discosub.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/format/discosub.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/pyversions/discosub.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/implementation/discosub.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/status/discosub.svg?maxAge=2592000)]()

[![Docker Stars](https://img.shields.io/docker/stars/4383/discosub.svg?maxAge=2592000)]()
[![Docker Pulls](https://img.shields.io/docker/pulls/4383/discosub.svg?maxAge=2592000)]()
[![Docker Automated buil](https://img.shields.io/docker/automated/4383/discosub.svg?maxAge=2592000)]()

Free and opensource subdomain scanner. Discosub is simple and
faster subdomain discover.

Discosub test if a list of subdomains exist via fuzzing on root domain.

Discosub use dictionaries for perform an analyze (BruteForce).

For more details visit the [official webpage project](https://4383.github.io/discosub/).

## install
### From pypi
```shell
pip install discosub
```

### As a docker container
```shell
docker pull 4383/discosub:latest
```

### from sources
```shell
$ git clone https://github.com/4383/discosub
$ cd discosub
$ python setup.py install
```

## Usages
### with a system install (from pypi or from sources)
```shell
discosub run google.com
```

### inside a docker container
```shell
docker run -e "TARGET=google.com" 4383/discosub:latest
```

## Prerequistes
* python >= 2.6 (but prefer python3.x)

## Features
* Analyze a root domain and discover its subdomains

## Guidelines
* Perform whois request on discovered subdomains

## License

* Free software: GNU General Public License v3

## Credits
Author: 4383 (Hervé Beraud)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
