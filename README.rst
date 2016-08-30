
Try pandoc!

pandoc --from markdown --to rst

  from

to

discosub 0.1.0
==============

Simple and faster subdomain discover

-  Free software: GNU General Public License v3

Usages
------

.. code:: shell

    $ git clone https://github.com/4383/discosub
    $ cd discosub
    $ python discosub/main.py run <your target domain>

Prerequistes
------------

-  python >= 2.7 (but prefer python3.x)

Features
--------

-  Analyze a root domain a discover these subdomains

Guidelines
----------

-  Distributing via pipy
-  Using system command (``$ discosub run <your target domain`` instead
   of ``$ python discosub/main.py run <your target domain>``)
-  Execute discosub in a docker container and provide a standalone image
   of this

Credits
-------

Author: 4383 (Hervé Beraud)

This package was created with `Cookiecutter`_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

pandoc 1.17.2

© 2013–2015 John MacFarlane
