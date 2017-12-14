import requests

class CryptoCompareWrapper(object):

	__DEFAULT_URL = 'https://min-api.cryptocompare.com/data/'

	def __init__(self, url=__DEFAULT_URL):
		self.base_url = url

## This handles all of the basic coin list information
	def coinList(self):
		"""
		Returns general info about all of the coins on the website.
		"""
		coin_list_URL = 'https://www.cryptocompare.com/api/data/coinlist/'
		r = requests.get(coin_list_URL)
		return r.json()

## These handle all of the price request
	def coinPrice(self, **params):
		"""
		Returns the price of the specified coin in terms of whichever
		currency is specified.
		Optional parameters:
			(string) fsym - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(string) e - name of exchange. Default: CCCAGG
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the requests
			(bool) tryConversion - If set to false, it will try to get values 
								   without using any conversion at all 
		"""
		url = self.base_url + 'price'
		r = requests.get(url, params)
		return r.json()

	def priceMultiple(self, **params):
		"""
		Returns a matrix of currency prices.
		Takes the same inputs as coinPrice.
		Optional parameters:
			(string) fsym - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(string) e - name of exchange. Default: CCCAGG
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the requests
			(bool) tryConversion - If set to false, it will try to get values 
								   without using any conversion at all 
		"""
		url = self.base_url + 'pricemulti'
		r = requests.get(url, params)
		return r.json()



########################## TESTING AND EXAMPLES ##########################
C = CryptoCompareWrapper()

test = {
		'fsym' : 'ETH', # from symbol
		'tsyms' : 'USD', # to symbol (include multiple symbols)
		#'e' : 'CCCAGG', # name of exhange
		#'extraParams' : , # name of your application
		'sign' : False, # if true - server will sign requests
		'tryConversion' : True # if false, will get values w/out using any conversion
}

print C.coinPrice(**(test))