##########################################################################
# A wrapper for general game data, such as quest, zones, and bosses, in  #
# Blizzard's WoW Community API.                                          #
# Part of BlizzPy.                                                       #
#                                                                        #
# Written by Lewis Kim.                                                  #
##########################################################################

import requests
import urllib, json
import pandas as pd



class WoWGeneral:

	"""."""
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

		self.achievements_data = {}


	"""

	   e.g. https://us.api.battle.net/wow/achievement/2144?locale=en_US&apikey=..."""
	def _get_achievement_data_url(self, achievement_id):
		url = "{root}/wow/achievement/{achievement_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			achievement_id = achievement_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/boss/?locale=en_US&apikey=..."""
	def _get_boss_master_url(self):
		url = "{root}/wow/boss/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/boss/24723?locale=en_US&apikey=..."""
	def _get_boss_data_url(self):
		url = "{root}/wow/boss/{boss_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			boss_id = boss_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/item/18803?locale=en_US&apikey=..."""
	def _get_item_data_url(self, item_id):
		url = "{root}/wow/item/{item_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			item_id = item_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/item/set/1060?locale=en_US&apikey=..."""
	def _get_item_set_data_url(self, set_id):
		url = "{root}/wow/item/set/{set_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			set_id = set_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/mount/?locale=en_US&apikey=..."""
	def _get_mount_master_url(self):
		url = "{root}/wow/mount/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/quest/13146?locale=en_US&apikey=..."""
	def _get_quest_data_url(self, quest_id):
		url = "{root}/wow/quest/{quest_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			quest_id = quest_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/realm/status?locale=en_US&apikey=..."""
	def _get_realms_data_url(self):
		url = "{root}/wow/realm/status?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/recipe/33994?locale=en_US&apikey=..."""
	def _get_recipe_data_url(self, recipe_id):
		url = "{root}/wow/recipe/{recipe_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			recipe_id = recipe_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/spell/260997?locale=en_US&apikey=..."""
	def _get_spell_data_url(self, spell_id):
		url = "{root}/wow/spell/{spell_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			spell_id = spell_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/zone/?locale=en_US&apikey=..."""
	def _get_zone_master_url(self):
		url = "{root}/wow/zone/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/zone/4131?locale=en_US&apikey=..."""
	def _get_zone_data_url(self, zone_id):
		url = "{root}/wow/zone/{zone_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			zone_id = zone_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving game achievements data. ###
	
	"""."""
	def get_achievement_data(self, achievement_id):
		try:
			with urllib.request.urlopen(self._get_achievement_data_url(achievement_id)) as url:
				self.achievement_data = json.loads(url.read().decode())

			return self.achievement_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Achievement ID.")
			return


### Retrieving game boss data. ###

	"""."""
	def get_bosses_data(self):
		try:
			with urllib.request.urlopen(self._get_boss_master_url()) as url:
				self.bosses_data = json.loads(url.read().decode())

			return self.bosses_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key.")
			return


	"""."""
	def get_boss_info(self, boss_id):
		try:
			with urllib.request.urlopen(self._get_boss_data_url(boss_id)) as url:
				self.boss_data = json.loads(url.read().decode())

			return self.boss_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game item data. ###

	"""."""
	def get_item_data(self, item_id):
		try:
			with urllib.request.urlopen(self._get_item_data_url(item_id)) as url:
				self.item_data = json.loads(url.read().decode())

			return self.item_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


	"""."""
	def get_item_set_data(self, itemSet_id):
		try:
			with urllib.request.urlopen(self._get_item_set_data_url(set_id)) as url:
				self.item_set_data = json.loads(url.read().decode())

			return self.item_set_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game mount data. ###

	"""."""
	def get_mounts_data(self):
		try:
			with urllib.request.urlopen(self._get_mount_master_url()) as url:
				self.mounts_data = json.loads(url.read().decode())

			return self.mounts_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game quest data. ###

	"""."""
	def get_quest_data(self, quest_id):
		try:
			with urllib.request.urlopen(self._get_quest_data_url(quest_id)) as url:
				self.quest_data = json.loads(url.read().decode())

			return self.quest_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving realm data. ###

	"""."""
	def get_realms_data(self):
		try:
			with urllib.request.urlopen(self._get_realms_data_url()) as url:
				self.realms_data = json.loads(url.read().decode())

			return self.realms_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game recipe data. ###

	"""."""
	def get_recipe_data(self, recipe_id):
		try:
			with urllib.request.urlopen(self._get_recipe_data_url(recipe_id)) as url:
				self.recipe_data = json.loads(url.read().decode())

			return self.recipe_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game spell data. ###

	"""."""
	def get_spell_data(self, spell_id):
		try:
			with urllib.request.urlopen(self._get_spell_data_url(spell_id)) as url:
				self.spell_data = json.loads(url.read().decode())

			return self.spell_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game zone data. ###

	"""."""
	def get_zones_data(self):
		try:
			with urllib.request.urlopen(self._get_zone_master_url()) as url:
				self.zones_data = json.loads(url.read().decode())

			return self.zones_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


	"""."""
	def get_zone_info(self, zone_id):
		try:
			with urllib.request.urlopen(self._get_zone_data_url(zone_id)) as url:
				self.zone_data = json.loads(url.read().decode())

			return self.zone_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return



