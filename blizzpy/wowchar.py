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

# A dictionary that maps the "class integer" to its full class name,
# e.g. '6': 'Death Knight'
int_to_class = {'1': 'Warrior', '2': 'Paladin', '3': 'Hunter', '4': 'Rogue', '5': 'Priest', '6': 'Death Knight',
	'7': 'Shaman', '8': 'Mage', '9': 'Warlock', '10': 'Monk', '11': 'Druid', '12': 'Demon Hunter'}

# A dictionary that maps the "race integer" to its full race name,
# e.g. '1': 'Human'
int_to_race = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '',
	'7': '', '8': '', '9': '', '10': '', '11': '', '12': '', '13': '', '14': '', '15': '',
	'16': '', '17': '', '18': '', '19': '', '20': '', '21': '', '22': '', '23': '', '24': '',}

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

		elif locale == "en_GB":
			self.root = "https://eu.api.battle.net"

		elif locale == "ko_KR":
			self.root = "https://kr.api.battle.net"

		elif locale == "zh_TW":
			self.root = "https://tw.api.battle.net"

		self.api_key = api_key
		self.locale = locale

		self.characterName = characterName
		self.realm = realm

		#
		self.character_data = {}


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

### Retrieving basic character data. ###

	"""Return basic character data of self.characterName as a Python dictionary, decoded from a JSON request.

	   Keys:
	   lastModified, name, realm, battlegroup, class, race, gender, level, achievementPoints, thumbnail,
	   calcClass, faction, totalHonorableKills."""
	def get_character_data(self):
		try:
			with urllib.request.urlopen(self._get_data()) as url:
				char_data = json.loads(url.read().decode())

			self.character_data = char_data

			return char_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return self.characterName's class. See int_to_class for details."""
	def get_class(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return int_to_class[str(self.character_data['class'])]


	"""Return self.characterName's race. See int_to_race for details."""
	def get_race(self):
		if not self.character_data:
			char_data = self.get_character_data()


	"""Return self.characterName's gender."""
	def get_gender(self):
		if not self.character_data:
			char_data = self.get_character_data()

		if self.character_data['gender'] == 0:
			return "Male"

		else:
			return "Female"


	"""Return self.characterName's level."""
	def get_level(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['level']


	"""Return self.characterName's total achievement points."""
	def get_achPoints(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['achievementPoints']


	"""Return self.characterName's faction."""
	def get_faction(self):
		if not self.character_data:
			char_data = self.get_character_data()

		if self.character_data['faction'] == 0:
			return "Alliance"

		else:
			return "Horde"


	"""."""
	# def get achievements


	"""."""
	# def get appearance


	"""."""
	# def get guild
	# sub functions


	"""."""
	# def get hunter pets


	"""."""
	# def get items


	"""."""
	# def get mounts


	"""."""
	# def get professions


	"""."""
	# def get raid prog


### Player PVP Statistics. ###

	"""."""
	# def get pvp data
	# Add sub functions

	"""."""
	def get_battlegroup(self):
		# Check if self.character_data is empty, i.e. if self.get_character_data() has been called yet.
		# If empty, call self.get_character_data() to point self.character_data and minimize API calls.
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['battlegroup']


	"""."""
	# def get reputation


	"""."""
	# def get quests


	"""."""
	# def get player statistics


	"""."""
	# def get stats


	"""."""
	# def get talents


	"""."""
	# def get titles





















