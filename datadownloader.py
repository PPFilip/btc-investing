import requests
from sys import exit
from pathlib import Path

urls = {
    'BTC': 'https://coinmetrics.io/newdata/btc.csv',
    'ETH': 'https://coinmetrics.io/newdata/eth.csv',
    'DOGE': 'https://coinmetrics.io/newdata/doge.csv',
    'LTC': 'https://coinmetrics.io/newdata/ltc.csv',
    'BCH': 'https://coinmetrics.io/newdata/bch.csv',
    'XMR': 'https://coinmetrics.io/newdata/xmr.csv',
    'XRP': 'https://coinmetrics.io/newdata/xrp.csv',
    'BTCUSD': 'http://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_d.csv',
    'DOGEBTC': 'http://www.cryptodatadownload.com/cdd/Tidex_DOGEBTC_d.csv',
    'ETHUSD': 'http://www.cryptodatadownload.com/cdd/Kraken_ETHUSD_d.csv',
    'ETHBTC': 'http://www.cryptodatadownload.com/cdd/Kraken_ETHBTC_d.csv',
    'LTCUSD': 'http://www.cryptodatadownload.com/cdd/Kraken_LTCUSD_d.csv',
    'LTCBTC': 'http://www.cryptodatadownload.com/cdd/Kraken_LTCBTC_d.csv',
    'XRPUSD': 'http://www.cryptodatadownload.com/cdd/Kraken_XRPUSD_d.csv',
    'XRPBTC': 'http://www.cryptodatadownload.com/cdd/Poloniex_XRPBTC_d.csv',
    'BCHUSD': 'http://www.cryptodatadownload.com/cdd/Poloniex_BCHUSD_d.csv',
    'XMRUSD': 'http://www.cryptodatadownload.com/cdd/Poloniex_XMRUSD_d.csv',
    'XMRBTC': 'http://www.cryptodatadownload.com/cdd/Poloniex_XMRBTC_d.csv'
}

for url in urls.values():
    file = Path()/"data"/"source"/Path(url).name
    print('-----')
    print('Downloading url: ', url)
    print('Writing to:', file)
    request = requests.get(url, allow_redirects=True)
    open(file, 'wb').write(request.content)

exit(0)
