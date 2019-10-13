import pandas as pd
from pandas import DataFrame
from sys import exit

# Script to join Bitcoin historical data from various sources into one file

# Coinmetrics data from 2010-07-18 to 2013-10-05 , download at https://coinmetrics.io/data-downloads/
cm = pd.read_csv("data/coinmetrics_btc.csv", usecols=['date', 'PriceUSD'])
cm['date'] = pd.to_datetime(cm['date'])
cm['PriceUSD'] = cm['PriceUSD'].round(4)
cm = cm.sort_values(['date'])

dfcm = DataFrame(cm, columns=['date', 'PriceUSD'])
dfcm = dfcm.rename(columns={'date':'Date','PriceUSD':'Close'})
mask = (dfcm['Date'] > '2010-07-18') & (dfcm['Date'] <= '2013-10-05')
dfcm = dfcm.loc[mask]

# Kraken data from 2013-10-06 up to today, download at  http://www.cryptodatadownload.com/data/northamerican/
kraken = pd.read_csv("data/Kraken_BTCUSD_d.csv", skiprows=1, usecols=['Date', 'Close'])
kraken['Date'] = pd.to_datetime(kraken['Date'])
kraken = kraken.sort_values(['Date'])

dfk = DataFrame(kraken, columns=['Date', 'Close'])

# put it all together
result = DataFrame(pd.concat([dfcm, dfk]))
result.to_csv(r'data/btcusd.csv', index=None, header=True)

exit(0)
