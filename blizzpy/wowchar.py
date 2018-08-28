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

# 
# Currently suppo
class WoWCharacter:

	""".

	   PARAMS:
	   self.root:
	   self.api_key:
	   self.locale:
	   self.characterName:
	   self.realm:"""
	def __init__(self, api_key, characterName, realm, locale="en_US", token=None):
		# Check if the user-given locale is supported, i.e. is one of Blizzard's regions.
		if locale not in accepted_locales:
			raise ValueError("Not supported locale.")
			return

		if locale == "en_US":
			self.root = "https://us.api.battle.net"

		elif locale = "en_GB":
			self.root = "https://eu.api.battle.net"

		elif locale == "ko_KR":
			self.root = "https://kr.api.battle.net"

		elif locale = "zh_TW":
			self.root = "https://tw.api.battle.net"

		self.api_key = api_key
		self.locale = locale

		self.characterName = characterName
		self.realm = realm


	"""."""
	def _api_request(self, endpoint):
		return


	"""."""
	def _get_data(self):
		url = "{root}/wow/character/{realm}/{characterName}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			characterName = self.characterName,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_data_with_endpoint(self, endpoint):
		url = "{root}/wow/character/{realm}/{characterName}?fields={endpoint}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			characterName = self.characterName,
			endpoint = endpoint,
			locale = self.locale,
			api_key = self.api_key
			)

		return url

### Retrieving Character Data. ###

	"""."""
	def get_character_data(self):
		try:
			with urllib.request.urlopen(self._get_data()) as url:
				char_data = json.loads(url.read().decode())

			return char_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return















