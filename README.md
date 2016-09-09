# discosub 0.2.0

[![Travis branch](https://img.shields.io/travis/4383/discosub/master.svg?maxAge=2592000&label=build branch master)]()
[![Travis branch](https://img.shields.io/travis/4383/discosub/development.svg?maxAge=2592000&label=build branch development)]()

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

You can use discosub directly from a python interpreter, or use it inside docker container.

You can perform an anonymous scanning directly
by using a specific [docker version](https://hub.docker.com/r/4383/discosub/tags/) (alias tor).

Different type of docker container are available:
* simple docker container with discosub installed on
* [torified (tor)](https://www.torproject.org/) docker container with discosub installed on (all discosub scanning connections use tor network)

For more details visit the [official webpage project](https://4383.github.io/discosub/).

## Install from pypi
```shell
pip install -U discosub
```

## Install as a docker container
```shell
docker pull 4383/discosub:latest
```

## Install as an anonymous scanner (tor + docker)
```shell
docker pull 4383/discosub:tor
```

## Install from sources
```shell
$ git clone https://github.com/4383/discosub
$ cd discosub
$ python setup.py install
```

## Usages from a local installation (from pypi or from sources)
```shell
discosub run google.com
```

## Usages inside a docker container
```shell
docker run -e "TARGET=google.com" 4383/discosub:latest
```

## Usages as an anonymous scanner from docker container (using tor inside docker)
```shell
docker run -e "TARGET=google.com" 4383/discosub:tor
```

## Prerequistes
* python >= 2.6 (but prefer python3.x)

## Features
* Analyze a root domain and discover its subdomains
* Analyze domain over tor via specific docker container (anonymous scanning)

## Advertissments
* scan over docker container are more slowly than direct usage from python interpreter
* scan over torified docker container are more slowly than direct usage from python interpreter and classical discosub docker container
* scan over torified docker container are more verbose than an classical scanning (identifiable IP)

## Upcoming features
* Perform whois request on discovered subdomains

## License
* Free software: GNU General Public License v3

## Credits
Author: 4383 (Hervé Beraud)

For create this project I've used some tools and packages so I want to thank them !

* [bumpversion](https://pypi.python.org/pypi/bumpversion). A magical python tools for automatic bumping version.
* [click](http://click.pocoo.org/). An amazing python package for handle cli options, arguments and flags, and more features !
* [Vincent Driessen](http://nvie.com/about/) and his [successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
* [The Semantic Versioning specification](http://semver.org/). A beautiful crafted specification who help me each days at work and on my personal projects.
* [Cookiecutter](https://github.com/audreyr/cookiecutter). A fucking good python command-line utility for initialize project.
* and all others what I've forgotten

This project was initialized with the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
