import os
from setuptools import setup

VERSION = "0.1.2"
DESCRIPTION = "nose plugin for Kay framework testing"
README = os.path.join(os.path.dirname(__file__), "README.rst")
LONG_DESCRIPTION = open(README).read() + "\n\n"

setup(
    name = "NoseKay",
    version = VERSION,
    author = "Yuku Takahashi",
    author_email = "taka84u9@gmail.com",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    license = "BSD",
    entry_points = {
        "nose.plugins.0.10": ["nosekay = nosekay:NoseKay"]
    },
    keywords="nose kay-framework",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Testing",
    ],
    py_modules = ["nosekay"],
    install_requires = ["nose>=0.10.1"],
)
