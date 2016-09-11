==============
discosub 0.3.0
==============

Free and opensource subdomain scanner. Discosub is simple and faster
subdomain discover.

Discosub test if a list of subdomains exist via fuzzing on root domain.

Discosub use dictionaries for perform an analyze (BruteForce).

You can use discosub directly from a python interpreter, or use it
inside docker container.

You can perform an anonymous scanning directly by using a specific
`docker version <https://hub.docker.com/r/4383/discosub/tags/>`__ (alias
tor).

Different type of docker container are available: \* simple docker
container with discosub installed on \* `torified
(tor) <https://www.torproject.org/>`__ docker container with discosub
installed on (all discosub scanning connections use tor network)

For more details visit the `official webpage
project <https://4383.github.io/discosub/>`__.

Install from pypi
-----------------

.. code:: shell

    pip install -U discosub

Install as a docker container
-----------------------------

.. code:: shell

    docker pull 4383/discosub:latest

Install as an anonymous scanner (tor + docker)
----------------------------------------------

.. code:: shell

    docker pull 4383/discosub:tor

Install from sources
--------------------

.. code:: shell

    $ git clone https://github.com/4383/discosub
    $ cd discosub
    $ python setup.py install

Usages from a local installation (from pypi or from sources)
------------------------------------------------------------

.. code:: shell

    discosub run google.com

Usages inside a docker container
--------------------------------

.. code:: shell

    docker run -e "TARGET=google.com" 4383/discosub:latest

Usages as an anonymous scanner from docker container (using tor inside docker)
------------------------------------------------------------------------------

.. code:: shell

    docker run -e "TARGET=google.com" 4383/discosub:tor

Usages for an agressive scanning mode
-------------------------------------

.. code:: shell

    discosub run google.com -a

Prerequistes
------------

-  python >= 2.6 (but prefer python3.x)

Features
--------

-  Analyze a root domain and discover its subdomains
-  Analyze domain over tor via specific docker container (anonymous
   scanning)

Advertissments
--------------

-  scan over docker container are more slowly than direct usage from
   python interpreter
-  scan over torified docker container are more slowly than direct usage
   from python interpreter and classical discosub docker container
-  scan over torified docker container are more verbose than an
   classical scanning (identifiable IP)

Upcoming features
-----------------

- Perform whois request on discovered subdomains
- Pass discosub options to docker container on run
- Perform scanning from user keywords file
- Save output into a file

License
-------

-  Free software: GNU General Public License v3

Credits
-------

Author: 4383 (Hervé Beraud)

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.
