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


########################## PRICE HISTORICAL ##########################
	def priceHistorical(self, **params):
		"""
		Get the price of any cryptocurrency in any other currency that you need at
		a given timestamp. The price comes from the daily infor - so it would be 
		the price at the end of the dat GMT based on the requested TS. If the crypto
		does not trade directly into the toSymbol requested, BTC will be used for 
		conversion. Tried to get trading pair data, if there is none or it is more 
		than 30 days before the ts requested, it uses BTC conversion. If the opposite
		pair trades then it is inverted (eg.: BTC-XMR)
		Optional parameters:
			(string) fsym - from symbol
			(string) tsyms - to symbols, include multiple symbols
			(timestamp) ts - timestamp
			(string) markets - Name of exhanges, include multiple
			(string) extraParams - Name of your application
			(bool) sign - If set to true, the server will sign the request
			(bool) tryConversion - If set to false, it will try to get values without any
								   conversion at all
		"""

		url = self.base_url
		if not params:
			raise Exception('Parameters are required for this feature.')
			return

		r = requests.get(url, params)
		return r.json()


########################## COIN SNAPSHOT ##########################
	def coinSnapshot(self, **params):
		"""
		Get data for a currency pair. It returns general block explorer information,
		aggregated data, and individual data for each exchange available.
		THIS API IS BEING ABUSED AND WILL BE MOVED IN THE FUTURE.
		DO NOT USE.
		Optional parameters:
			(string) fsym - the symbol of the currency you want to see
			(string) tsym - the symbol of the currency that data will be in
		"""
		url = self.base_url + 'coinsnapshot/'
		if not params:
			raise Exception('Parameters are required for this feature.')
			return
		r = requests.get(url, params)
		return r.json()

########################## FULL COIN SNAPSHOT BY ID ##########################
	def coinSnapshotFullById(self, id):
		"""
		Get the general, subs (used to connect to the streamer and to figure out
		what exhanges we have data for and what are the exact coin pairs of the coin)
		and the aggregated prices for all pairs available.
		Parameters:
			(int) id - The id of the cion you want data for
		"""
		params = {'id' : id}
		url = self.base_url + 'coinsnapshotfullbyid/'

		if not params:
			raise Exception('Parameters are required for this feature.')
			return
		r = requests.get(url, params)
		return r.json()




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

print C.priceHistorical(**(test))
