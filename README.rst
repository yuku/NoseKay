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

    $ cd /path/to/your/project/dir
    $ nosetests --with-kay [module]

You can use **--kay-app-dir** to specify the location of your project directory::

    $ nosetests --with-kay --kay-app-dir /path/to/your/project/dir [module]

If you don't designate kay app module (at [module] position described in above), nose will find and execute all test cases in kay framework and other third party libraries installed in your project.
So, for example if you want to test the app named *core*, call nosetests command as follows::

    $ nosetests --with-kay core
