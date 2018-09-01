###########################################################################
# A wrapper for the non-hunter pet data in Blizzard's WoW Community API.  #
# Part of BlizzPy.                                                        #
#                                                                         #
# Written by Lewis Kim.                                                   #
###########################################################################

import requests
import urllib, json
import pandas as pd


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]

class WoWPets:


	def __init__(self, api_key, locale="en_US", token=None):
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

		self.api_key = api_key
		self.locale = locale

		self.master_data = []

		self.ability_data = {}
		self.species_data = {}
		self.stats_data = {}


	"""."""
	def _get_master_data(self):
		url = "{root}/wow/pet/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url

	"""."""
	def _get_ability_data(self, abilityId):
		url = "{root}/wow/pet/ability/{abilityId}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			abilityId = abilityId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_species_data(self, speciesId):
		url = "{root}/wow/pet/species/{speciesId}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			speciesId = speciesId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_stats_data(self, speciesId, level, breedId, qualityId):
		url = "{root}/wow/pet/stats/{speciesId}?level={level}&breedId={breedId}&qualityId={qualityId}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			speciesId = speciesId,
			level = level,
			breedId = breedId,
			qualityId = qualityId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving the pets master list. ###

	"""."""
	def get_master_list(self):
		try:
			with urllib.request.urlopen(self._get_master_data()) as url:
				self.master_data = json.loads(url.read().decode())['pets']

			return self.master_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key.")
			return


	"""."""
	def search_pet(self, pet_param):
		if not self.master_data:
			master_data = self.get_master_list()

		if type(pet_param) == str:
			return next((pet for pet in self.master_data if pet['name'] == pet_param), None)

		elif type(pet_param) == int:
			return next((pet for pet in self.master_data if pet['creatureId'] == pet_param), None)

		else:
			raise ValueError("Invalid parameters. Param PET must be a string (pet name), or an integer (creature ID).")
			return


	"""."""
	def get_nameToID_dict(self):
		if not self.master_data:
			master_data = self.get_master_list()

		return {pet['name']: pet['creatureId'] for pet in self.master_data}


	"""."""
	def get_battle_pets(self, as_names=False):
		if not self.master_data:
			master_data = self.get_master_list()

		if as_names:
			return [pet['name'] for pet in self.master_data if pet['canBattle']]

		else:
			return [pet for pet in self.master_data if pet['canBattle']]


	"""."""
	def get_nonbattle_pets(self, as_names=False):
		if not self.master_data:
			master_data = self.get_master_list()

		if as_names:
			return [pet['name'] for pet in self.master_data if not pet['canBattle']]

		else:
			return [pet for pet in self.master_data if not pet['canBattle']]


	"""."""
	def get_pet_stats(self, pet_param):
		if not self.master_data:
			master_data = self.get_master_list()

		if type(pet_param) == str:
			return next((pet['stats'] for pet in self.master_data if pet['name'] == pet_param), None)

		elif type(pet_param) == int:
			return next((pet['stats'] for pet in self.master_data if pet['creatureId'] == pet_param), None)

		else:
			raise ValueError("Invalid parameters. Param PET must be a string (pet name), or an integer (creature ID).")
			return


### Retrieving pet abilities data. ###
	
	"""."""
	def get_ability_data(self, abilityId):
		try:
			with urllib.request.urlopen(self._get_ability_data(abilityId)) as url:
				self.ability_data = json.loads(url.read().decode())

			return self.ability_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or ability ID.")
			return


### Retrieving pet species data. ###

	"""."""
	def get_species_data(self, speciesId):
		try:
			with urllib.request.urlopen(self._get_species_data(speciesId)) as url:
				self.species_data = json.loads(url.read().decode())

			return self.species_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or ability ID.")
			return


### Retrieving species stat data. ###

	"""."""
	def get_species_stats_data(self, speciesId, level=1, breedId=3, qualityId=1):
		try:
			with urllib.request.urlopen(self._get_stats_data(speciesId, level, breedId, qualityId)) as url:
				self.ability_data = json.loads(url.read().decode())

			return self.ability_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or ability ID.")
			return

