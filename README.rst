gears-coffeescript
==================

CoffeeScript_ compiler for Gears_. This package already includes the
CoffeeScript source code for you, so you don't need to worry about installing
it yourself.

Bundled CoffeeScript version: **1.3.3**

Installation
------------

Install ``gears-coffeescript`` with pip::

    $ pip install gears-coffeescript


Requirements
------------

``gears-coffeescript`` requires node.js_ to be installed in your system.


Usage
-----

Add ``gears_coffeescript.CoffeeScriptCompiler`` to ``environment``'s compilers
registry::

    from gears_coffeescript import CoffeeScriptCompiler
    environment.compilers.register('.coffee', CoffeeScriptCompiler.as_handler())

If you use Gears in your Django project, add this code to its settings::

    GEARS_COMPILERS = {
        '.coffee': 'gears_coffeescript.CoffeeScriptCompiler',
    }

.. _CoffeeScript: http://coffeescript.org/
.. _Gears: https://github.com/gears/gears
.. _node.js: http://nodejs.org/
