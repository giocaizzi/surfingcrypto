# Quick start

This project provides a customizable and automatic reporting tool for crypto price data.
It is able to plot complex graphs for price information (from traditional **candlesticks&volume** to **technical analysis** indicators).
All outputs (plots and calculations) can be sent via telegram using a TelegramBot created with @BotFather.
It features also an integration with Coinbase to get notifications on portfolio value.

![TA Figure](../images/ta.jpeg)

It is possible to get historical price data on any cryptocurrency listed on [coinmarketcap.com](http://www.coinmarketcap.com), such as `BTC`,`ETH`,`ADA`,`MATIC`, `SOL`.

The idea behind the package is to have a set of functions to produce daily reports, in form of plots and text. An example is as used as in [`main.py`](https://github.com/giocaizzi/surfingcrypto/blob/main/main.py).

This script is actually deployed as a crontab job on a AWS ec2 istance, every day at `10:30 AM UTC`.

___
- [Quick start](#quick-start)
  - [Key modules](#key-modules)
  - [Basic usage](#basic-usage)
    - [Configuration](#configuration)
    - [Price data scraping](#price-data-scraping)
    - [Telegram notifications](#telegram-notifications)
    - [Price data analysis](#price-data-analysis)
      - [Plotting prices and indicators](#plotting-prices-and-indicators)
      - [Reporting useful information](#reporting-useful-information)
  - [Package modules structure](#package-modules-structure)
___

## Key modules

1. The [Scraper](../_autosummary/surfingcrypto.scraper.Scraper.rst) class gets the necesarriy data from [coinmarketcap.com](http://www.coinmarketcap.com) and stores data locally. 
   
2. [TelegramBot](../_autosummary/surfingcrypto.telegram_bot.TelegramBot.rst) starts a telegram client to send outputs to bot followers.
   
3. [TaPlot](../_autosummary/surfingcrypto.reporting.figures.TaPlot.rst) Creates a time-series figure plot that resumes the price cryptocurrency. There are also other kinds of data plot, but specifically it can also plot also complex indicators.
  
The folder `examples` containsa a series of examples that allows to experiment interactively with the repository capacities.

## Basic usage

### Configuration

The [Config()](../_autosummary/surfingcrypto.config.Config.rst) class is used to pass the user configuration.

It requires to specify the location of the folder in which there is a `config.json` file, in which it is possible/required to specify the following parameters:
* the parametrization of Technical Analysis (eg. window of moving averages, RSI length, etc...)
* the API key to the [telegram](https://core.telegram.org/) bot.
* the API key to the [Coinbase](https://developers.coinbase.com/) client. 

Additionally, it is possible to specify the location of a `data` folder where to save all data (eg. time series of prices)

### Price data scraping

The [Scraper](../_autosummary/surfingcrypto.scraper.Scraper.rst) gets the necesarriy data from [coinmarketcap.com](http://www.coinmarketcap.com) and stores data locally. 

[Go to full example.](../examples/scraper.ipynb)

### Telegram notifications

In order to receive daily updates on prices, a telegram bot is used. Bots can be created with @BotFather.

The bot can be used both in "normal" mode or in "channel mode".
The normal mode (`channel_mode=False`) requires to specify a `chat_id` parameter to specify the desired chat to send the message/picture/document to. Otherwise, when `channel_mode=True` then the bot will send the content to all users specified in the `telegram_users.csv`.

The bot has the capability of adding new users to the known list of users, just by recording the `chat_id` of the users that have interacted with it. Everytime the bot is initiated, it checks for new users.

### Price data analysis

The project is focused on the production of a customizable and useful set of information to be up to date with cryptocurrency prices.

The reporting structure is based on the production of graphs and by well-structured text.

#### Plotting prices and indicators

There following are the kind of plots that have been implemented.

- `SimplePlot` Simple plot.
  - candlesticks
  - volume

- `TaPlot` Technical Analysis plot. 
  - candlestick (with MA lines)
  - volume
  - MACD 
  - Bollinger bands
  - RSI

- `ATHPlot` Distance from ATH plot

[Go to full example.](../examples/reporting.ipynb)


All plots inherits from the same base object `BaseFigure` that has useful methods for working with matplotlib figures.

#### Reporting useful information

The `TS` class has some reporting methods associated, such as `report_percentage_diff` that produces a well structured string with formatting to be sent via telegram or read over the terminal.

```
**ADA**
- 1d: 0.36 %
- 3d: -2.32 %
- 7d: 2.32 %
- 14d: 4.89 %
- 60d: -14.30 %
```
Ex: percentage difference for a set of different days.

## Package modules structure

The following image depicts the package module structure and integration architecture.

![TA Figure](../images/structure.png)