#######
NoseKay
#######

nose plugin for `Kay framework <http://code.google.com/p/kay-framework/>`_ testing.

Installation
************

::

    $ easy_install NoseKay

or from the source::

    $ python setup.py install

Basic Usage
***********

Usage::

    $ cd /path/to/your/app
    $ nosetests --with-kay [app]

You can use --kay-app-dir to specify your application directory.::

    $ nosetests --with-kay --kay-app-dir /path/to/your/app [app]
