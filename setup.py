
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'CryptoComparePython',
    version = '1.0.0',
    url = 'https://github.com/iJEEBUS/CryptoComparePython',
    download_url = 'https://github.com/iJEEBUS/CryptoComparePython/archive/master.zip',
    author = 'Ronald Rounsifer : ronrounsifer@me.com',
    author_email = 'ronrounsifer@me.com',
    license = 'MIT',
    packages = ['CryptoComparePython'],
    description = 'Python wrapper for cryptocompare.com API.',
    install_requires=['requests', 'json'],
    keywords = ['cryptocurrency', 'API', 'cryptocompare','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin', 'ETH', 'Ethereum'],
)
