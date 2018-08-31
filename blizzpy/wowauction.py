#####
#
#
#
# Written by Lewis Kim.
######

import requests
import urllib, json
import pandas as pd


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]

class WoWAuction:


	def __init__(self, api_key, realm, locale="en_US", token=None):
		# Check if the user-given locale is supported, i.e. is one of Blizzard's regions.
		if locale not in accepted_locales:
			raise ValueError("Not supported locale.")
			return

		if locale == "en_US":
			self.root = "https://us.api.battle.net"

		elif locale == "en_GB":
			self.root = "https://eu.api.battle.net"

		elif locale == "ko_KR":
			self.root = "https://kr.api.battle.net"

		# elif locale == "zh_TW":
		# 	self.root = "https://tw.api.battle.net"

		self.realm = realm
		self.api_key = api_key
		self.locale = locale

		self.last_modified = 0


	"""."""
	def _get_auction_data(self):
		url = "{root}/wow/auction/data/{realm}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving WoW auction house patch data. ###

	"""."""
	def get_auction_data(self):
		try:
			with urllib.request.urlopen(self._get_auction_data()) as url1:
				raw_data = json.loads(url1.read().decode())
				self.last_modified = raw_data['files'][0]['lastModified']

			with urllib.request.urlopen(raw_data['files'][0]['url']) as url2:
				self.auction_data = json.loads(url2.read().decode())['auctions']

			return self.auction_data
		except:
			raise ValueError("Could not retrieve data. Please check your API key or realm.")
			return


	"""."""
	def get_last_modified(self):
		if not self.last_modified:
			auction_data = self.get_auction_data()

		return self.last_modified


	"""."""
	def get_buyout_prices(self, item_id):
		if not self.auction_data:
			auction_data = self.get_auction_data()

		return {auction['buyout']:auction['quantity'] for auction in self.auction_data}


	"""."""
	def get_auctions_by_player(self, player_name):
		if not self.auction_data:
			auction_data = self.get_auction_data()

		return [auction for auction in self.auction_data if auction['owner'] == player_name]

