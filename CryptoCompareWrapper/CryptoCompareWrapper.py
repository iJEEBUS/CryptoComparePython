import requests

class CryptoCompareWrapper(object):

	__DEFAULT_URL = 'https://min-api.cryptocompare.com/data/'
	__DEFAULT_COIN = 'ETH'
	__DEFAULT_CURRENCY = 'USD'

	def __init__(self, url=__DEFAULT_URL, coin=__DEFAULT_COIN, currency=__DEFAULT_CURRENCY):
		self.base_url = url
		self.base_coin = coin
		self.base_currency = currency

########################## COINLIST ##########################
	def coinList(self):
		"""
		Returns general info about all of the coins on the website.
		"""
		coin_list_URL = 'https://www.cryptocompare.com/api/data/coinlist/'
		r = requests.get(coin_list_URL)
		return r.json()

########################## PRICE ##########################
	def price(self, **params):
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
		if params:
			r = requests.get(url, params)
		else:
			params = {'fsym' : self.base_coin, 'tsyms' : self.base_currency}
			r = requests.get(url, params)
		return r.json()

	def priceMultiple(self, **params):
		"""
		Returns a matrix of currency prices.
		Takes the same inputs as coinPrice.
		Optional parameters:
			(string) fsyms - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(string) e - name of exchange. Default: CCCAGG
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the requests
			(bool) tryConversion - If set to false, it will try to get values 
								   without using any conversion at all 
		"""
		url = self.base_url + 'pricemulti'
		if params:
			r = requests.get(url, params)
		else:
			params = {'fsyms' : self.base_coin, 'tsyms' : self.base_currency}
			r = requests.get(url, params)
		return r.json()

	def priceMultipleFull(self, **params):
		"""
		Get all the current trading info (price, vol, open, high, low)
		of any list of cryptocurrencies in any other currency that you
		need. If the crypto does not trade directly into the toSymbol 
		requested, BTC will be used for conversion. Also returns Display
		values for all the fields. If the opposite pair trades we invert it
		(eg.: BTC-XMR)
		Optional parameters:
			(string) fsyms - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(string) e - name of exchange. Default: CCCAGG
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the requests
			(bool) tryConversion - If set to false, it will try to get values 
								   without using any conversion at all 
		"""
		url = self.base_url + 'pricemulti'
		if params:
			r = requests.get(url, params)
		else:
			params = {'fsyms' : self.base_coin, 'tsyms' : self.base_currency}
			r = requests.get(url, params)
		return r.json()


	def generateAvg(self, **params):
		"""
		Get day average price. 
		Optional parameters:
			(string) fsym - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(string) e - name of exchange. Default: CCCAGG
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the requests
			(bool) tryConversion - If set to false, it will try to get values 
								   without using any conversion at all 
		"""
		url = self.base_url + 'generateAvg'
		r = requests.get(url, params)
		return r.json()

	def dayAvg(self, **params):
		"""
		Get day average price. The values are based on hourly vwap data and 
		the average can be calculated in different ways. It uses BTC conversion
		if data is not available because the coin is not trading in the specified 
		currency. If tryConversion is set to false it will give you the direct data.
		If no toTS is given it will automatically do the current day. Also, for 
		different timezones use the UTCHourDiff param. 
		The calculation types are:
		HourVWAP - a VWAP of the hourly close price
		MidHighLow - the average between the 24 H high and low
		VolFVolT - the total volume from / the total volume to (only available
				   with tryConversion set to false so only for direct trades, but
				   the value should be the most accurate price)
		Optional parameters:
			(string) fsym - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(string) e - name of exchange. Default: CCCAGG
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the requests
			(bool) tryConversion - If set to false, it will try to get values 
								   without using any conversion at all 
			(string) avgType - HourVWAP for default
			(int) UTCHourDiff - UTC for default. Pass the hour difference to 
								change timezones (-8 for PST)
			(timestamp) toTs - hour unit
		"""
		url = self.base_url + 'dayAvg'
		r = requests.get(url, params)
		return r.json()


########################## TESTING AND EXAMPLES ##########################




########################## TESTING AND EXAMPLES ##########################
C = CryptoCompareWrapper()

test = {
		#'fsym' : 'ETH', # from symbol
		#'tsyms' : 'USD', # to symbol (include multiple symbols)
		#'e' : 'CCCAGG', # name of exhange
		#'extraParams' : , # name of your application
		#'sign' : False, # if true - server will sign requests
		#'tryConversion' : True # if false, will get values w/out using any conversion
}

print C.priceMultipleFull(**(test))