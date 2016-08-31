===============
discosub 0.1.12
===============

Free and opensource subdomain scanner. Discosub is simple and faster
subdomain discover.

Discosub test if a list of subdomains exist via fuzzing on root domain.

Discosub use dictionaries for perform an analyze (BruteForce).

For more details visit the `official webpage project`_.

install
-------
from pypi
~~~~~~~~~

.. code:: shell

    pip install discosub

as a docker container
~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

    docker pull 4383/discosub:latest

from sources
~~~~~~~~~~~~

.. code:: shell

    $ git clone https://github.com/4383/discosub
    $ cd discosub
    $ python setup.py install

Usages
------
with a system install (from pypi or from sources)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

    discosub run google.com

inside a docker container
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

    docker run -e "TARGET=google.com" 4383/discosub:latest

Prerequistes
------------

-  python >= 2.6 (but prefer python3.x)

Features
--------

-  Analyze a root domain and discover its subdomains

Guidelines
----------

-  Perform whois request on discovered subdomains

License
-------

-  Free software: GNU General Public License v3

Credits
-------

Author: 4383 (Hervé Beraud)

This package was created with `Cookiecutter`_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _official webpage project: https://4383.github.io/discosub/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
