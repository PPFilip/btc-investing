import pandas as pd
from sys import exit
from pathlib import Path

# Script to join Bitcoin historical data from various sources into one file

# Coinmetrics data from 2010-07-18 to 2013-10-05 , download at https://coinmetrics.io/data-downloads/
cm_file = Path()/"data"/"source"/"btc.csv"
cm = pd.read_csv(cm_file, usecols=['date', 'PriceUSD'])

cm['date'] = pd.to_datetime(cm['date'])
cm['PriceUSD'] = cm['PriceUSD'].round(4)

cm = cm.sort_values(['date'])
cm = cm.rename(columns={'date': 'Date', 'PriceUSD': 'Close'})

mask = (cm['Date'] > '2010-07-18') & (cm['Date'] <= '2013-10-05')
cm = cm.loc[mask]

# Kraken data from 2013-10-06 up to today, download at  http://www.cryptodatadownload.com/data/northamerican/
kraken_file = Path()/"data"/"source"/"Kraken_BTCUSD_d.csv"
kraken = pd.read_csv(kraken_file, skiprows=1, usecols=['Date', 'Close'])

kraken['Date'] = pd.to_datetime(kraken['Date'])
kraken = kraken.sort_values(['Date'])

result = pd.concat([cm, kraken])
out_file = Path()/"data"/"btcusd.csv"
result.to_csv(out_file, index=None, header=True)

exit(0)
