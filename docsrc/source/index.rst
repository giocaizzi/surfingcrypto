Welcome to surfingcrypto's documentation!
=========================================

.. image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20-blue
    :alt: PyPI - Python Version 

.. image:: https://img.shields.io/github/workflow/status/giocaizzi/surfingcrypto/ci
    :alt: GitHub Workflow Status

.. image:: https://img.shields.io/codecov/c/gh/giocaizzi/surfingcrypto
    :alt: codecov


python package to surf crypto-waves.

- Scrapes *OHLC data* from `www.coinmarketcap.com <www.coinmarketcap.com>`_ and stores it locally.
- Compute *Technical Analysis* indicators and plot complex graphs
- Interact with *Coinbase API* to read transaction data and to compute Portfolio statistics

It's future developement will be based on **algotrading**.

.. note ::
   This is project is based on making money fast to go surf |:ocean:| in some tropical destination. |:palm_tree:|


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   contents/installation.md
   contents/bodytext.md
   contents/references.md

.. toctree::
   :maxdepth: 1
   :caption: Examples:

   examples/scraper.ipynb
   examples/ts.ipynb
   examples/reporting.ipynb
   examples/figures.ipynb
   examples/portfolio_01.ipynb
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
