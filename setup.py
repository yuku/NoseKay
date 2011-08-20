from setuptools import setup

VERSION = "0.0.1"

DESCRIPTION = "nose plugin for Kay framework testing"

LONG_DESCRIPTION = """

Usage::

    $ cd /path/to/your/app
    $ nosetests --with-kay [app]

or::

    $ nosetest --with-kay --kay-app-dir /path/to/your/app [app]
"""

setup(
    name = "NoseKay",
    version = VERSION,
    author = "Yuku Takahashi",
    author_email = "taka84u9@gmail.com",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION
    license = "BSD",
    entry_points = {
        "nose.plugins.0.10": ["nosekay = nosekay:NoseKay"]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Testing",
    ],
    py_modules = ["nosekay"],
    install_required = ["nose>=0.10.1"],
)
