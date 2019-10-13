import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib import style
from pandas.plotting import register_matplotlib_converters
from sys import exit

register_matplotlib_converters()

# load data
btc = pd.read_csv("data/btcusd.csv")

# Index dataset by date
btc['Date'] = pd.to_datetime(btc['Date'])
btc = btc.set_index('Date')
btc = btc.sort_index()

# resample dataset from days to months
btc_monthly = btc.resample('M').ffill()

btc_daily_returns = btc['Close'].pct_change()
btc_monthly_returns = btc_monthly['Close'].pct_change()

value_price = btc_monthly['Close'][-1]
initial_investment = 10000.00

num_btc_bought = initial_investment / btc_monthly['Close']
lumpsum = num_btc_bought * value_price
lumpsum.name = 'Lump Sum'


recenttime = 36 #number of months to look into past

def doDCA(investment, start_date):
    # Get 12 investment dates in 30 day increments starting from start date
    investment_dates_all = pd.date_range(start_date,periods=12,freq='1M')
    # Remove those dates beyond our known data range
    investment_dates = investment_dates_all[investment_dates_all < btc_monthly.index[-1]]

    # Get closest business dates with available data
    closest_investment_dates = btc.index.searchsorted(investment_dates)

    # How much to invest on each date
    portion = investment/12.0 # (Python 3.0 does implicit double conversion, Python 2.7 does not)

    # Get the total of all stocks purchased for each of those dates (on the Close)
    stocks_invested = sum(portion / btc_monthly['Close'][investment_dates])

    # Add uninvested amount back
    uninvested_dollars = portion * sum(investment_dates_all >= btc_monthly.index[-1])

    # value of stocks today
    total_value = value_price*stocks_invested + uninvested_dollars
    return total_value

# Generate DCA series for every possible date
dca = pd.Series(btc_monthly.index.map(lambda x: doDCA(initial_investment, x)), index=btc_monthly.index, name='Dollar Cost Averaging (DCA)')

diff = (lumpsum - dca)
diff.name = 'Difference (Lump Sum - DCA)'

first_100_day = (btc_monthly['Close'] >= 100).idxmax()
recentdiff = diff.loc[first_100_day:'2019-12-31']
