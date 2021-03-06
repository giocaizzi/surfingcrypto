"""
script to be run on ec2 istance
"""
import datetime as dt
from pathlib import Path


from TelegramBotNotifications import TelegramBot

from surfingcrypto import Config, TS
from surfingcrypto.scraper import Scraper
from surfingcrypto.reporting.reporting import (
    report_percentage_diff,
    report_coinbase_live_value,
    report_stock_gain,
)
from surfingcrypto.reporting.figures import ATHPlot, TaPlot
from surfingcrypto.portfolio import Portfolio
from surfingcrypto.algotrading.backtesting import BackTest
from surfingcrypto.algotrading.features import BinaryLaggedLogReturns
from surfingcrypto.algotrading.model import Model
from surfingcrypto.reporting.reporting import report_tomorrow_prediction

# get cwd
cwd = Path(__file__).resolve().parent

# time of execution
now = dt.datetime.today()
timestr = now.strftime("%Y%m%d-%H%M%S")

# config
coins={
    "BTC":"",
    "ETH":"",
}
c = Config(coins,str(cwd) + "/config")

# coinbase portfolio
p = Portfolio("coinbase", configuration=c)

# update config for coins that are not specified in config
c.add_coins(p.coinbase.active_accounts)

# telegram bot in channel mode
tg = TelegramBot(
    c.telegram["token"],
    channel_mode=True,
    users_path=str(cwd) + "/config/telegram_users.csv",
)

# scrape required data
print("### Scraper")
s = Scraper(c)
s.run()
tg.send_message_to_all(message=s.output_description)  # send scraper log to telegram

# start tracker AFTER having scraped required data
p.start_tracker(
    stocks_start="1-1-2021", benchmark="ETH",
)

coins_to_plot = [
    x for x in set(p.coinbase.active_accounts + list(c.coins.keys())) if x != "USDC"
]

# produce reports for each coin in configuration
for coin in coins_to_plot:
    # daily TA plots
    ts = TS(c, coin=coin)
    ts.ta_indicators()
    fig = TaPlot(object=ts, graphstart="6m")
    tmpname = c.temp_folder + "/" + coin + "_" + timestr + ".jpeg"
    fig.save(tmpname)
    tg.send_message_to_all(report_percentage_diff(ts.df, ts.coin))
    tg.send_photo_to_all(tmpname)

    # ATH(BTC) plot every monday
    if coin == "BTC" and now.weekday() == 0:
        ath = ATHPlot(ts, graphstart="1-1-2020")
        tmpname = c.temp_folder + "/" + coin + "_ATH_" + timestr + ".jpeg"
        ath.save(tmpname)
        tg.send_photo_to_all(tmpname)

# PORTFOLIO INFO
tg.send_message_to_user(report_coinbase_live_value(p), "admin")
tg.send_message_to_user(report_stock_gain(p.tracker.daily_snaphost("last")), "admin")

# ALGOTRADING

ticker = "ETH"
ts = TS(c, coin=ticker)
ts.ta_indicators()
f = BinaryLaggedLogReturns(
    [1, 2, 3, 7, 14],
    ts,
    indicators=[
        "SMA_12_26_Signal",
        "SMA_100_200_Signal",
        "MACD_12_26_9_Signal",
        "BB_20_2_Signal",
        "RSI_14_Signal",
    ],
)

model=Model("svm",f)
tg.send_message_to_user("ALGOTRADING - "+ticker+" :", "admin")
tg.send_message_to_user(report_tomorrow_prediction(model.make_tomorrow_prediction()), "admin")
