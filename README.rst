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

::

    $ cd /path/to/your/app/dir
    $ nosetests --with-kay [module]

You can use **--kay-app-dir** option to specify the location of your application directory::

    $ nosetests --with-kay --kay-app-dir /path/to/your/app/dir [module]

If you don't designate any module (at [module] position described in above), nose will find and execute test cases not only in your application but also in kay framework and other third party libraries installed in your project.
Because kay framework has hundreds of test cases, you may want to skip them.
So, for example if you have the module named *core*, call nosetests command as follows to do tests only in the app::

    $ nosetests --with-kay core
