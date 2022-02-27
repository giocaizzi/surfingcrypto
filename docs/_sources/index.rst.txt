Welcome to surfingcrypto's documentation!
=========================================

.. image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20-blue
    :alt: PyPI - Python Version 

.. image:: https://img.shields.io/github/workflow/status/giocaizzi/surfingcrypto/ci
    :alt: GitHub Workflow Status

.. image:: https://img.shields.io/codecov/c/gh/giocaizzi/surfingcrypto
    :alt: codecov

This project provides a customizable and automatic reporting tool for crypto price data.
It is able to plot complex graphs for price information (from traditional **candlesticks&volume** to **technical analysis** indicators).
All outputs (plots and calculations) can be sent via telegram using a TelegramBot created with @BotFather.
It features also an integration with Coinbase to get notifications on portfolio value.

It's future developement will be based on **algotrading**.

.. note ::
   This is project is based on making money fast to go surf |:ocean:| in some tropical destination. |:palm_tree:|

.. warning ::
   The package is under developement and it has not been released yet.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   contents/installation.md
   contents/bodytext.md
   contents/references.md

.. toctree::
   :maxdepth: 2
   :caption: Examples:

   examples/scraper.ipynb
   examples/ts.ipynb
   examples/reporting.ipynb
   examples/portfolio_coinbase.ipynb

Code reference
==============

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :caption: Code reference:
   :recursive:

   surfingcrypto

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
