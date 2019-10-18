import requests
from sys import exit
from pathlib import Path

urls = {
    'BTC': 'https://coinmetrics.io/newdata/btc.csv',
    'ETH': 'https://coinmetrics.io/newdata/eth.csv',
    'DOGE': 'https://coinmetrics.io/newdata/doge.csv',
    'BTCUSD': 'http://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_d.csv',
    'ETHUSD': 'http://www.cryptodatadownload.com/cdd/Kraken_ETHUSD_d.csv',
    'ETHBTC': 'http://www.cryptodatadownload.com/cdd/Kraken_ETHBTC_d.csv'
}

for url in urls.values():
    file = Path()/"data"/"source"/Path(url).name
    print('-----')
    print('Downloading url: ', url)
    print('Writing to:', file)
    request = requests.get(url, allow_redirects=True)
    open(file, 'wb').write(request.content)

exit(0)
