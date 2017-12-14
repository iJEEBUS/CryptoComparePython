
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'CryptoCompareWrapper',
    version = '1.0.0',
    url = 'https://github.com/iJEEBUS/CryptoCompareWrapper',
    download_url = 'https://github.com/iJEEBUS/CryptoCompareWrapper/archive/master.zip',
    author = 'Ronald Rounsifer : ronrounsifer@me.com',
    author_email = 'ronrounsifer@me.com',
    license = 'MIT',
    packages = ['CryptoCompareWrapper'],
    description = 'Python wrapper for cryptocompare.com API.',
    long_description = open('README.md','r').read(),
    install_requires=['requests', 'json'],
    keywords = ['cryptocurrency', 'API', 'cryptocompare','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin', 'ETH', 'Ethereum'],
)
