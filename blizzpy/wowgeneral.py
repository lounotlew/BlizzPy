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


	"""."""
	def _get_achievement_data_url(self):
		return


	"""."""
	def _get_boss_url(self):
		return


	"""."""
	def _get_item_url(self):
		return


	"""."""
	def _get_item_set_url(self):
		return


	"""."""
	def _get_mount_url(self):
		return


	"""."""
	def _get_quest_url(self):
		return


	"""."""
	def _get_realm_url(self):
		return


	"""."""
	def _get_recipe_url(self):
		return


	"""."""
	def _get_spell_url(self):
		return


	"""."""
	def _get_zone_url(self):
		return



### Retrieving game achievements data. ###

# https://us.api.battle.net/wow/achievement/2144?locale=en_US&apikey=6j49d54nvcttpbhvsqxs6pcvqf5b7t9y
	
	"""."""
	def get_achievement_data(self, achievement_id):
		return





### Retrieving game boss data. ###

	"""."""
	def get_bosses_data(self):
		return


	"""."""
	def get_boss_info(self, boss_id):
		return





### Retrieving game item data. ###

	"""."""
	def get_item_data(self, item_id):
		return


	"""."""
	def get_item_set_data(self, itemSet_id):
		return






### Retrieving game mount data. ###

	"""."""
	def get_mounts_data(self):
		return




### Retrieving game quest data. ###

	"""."""
	def get_quest_data(self, quest_id):
		return


### Retrieving realm data. ###

	"""."""
	def get_realms_data(self):
		return



### Retrieving game recipe data. ###

	"""."""
	def get_recipe_data(self):
		return


### Retrieving game spell data. ###

	"""."""
	def get_spell_data(self):
		return


### Retrieving game zone data. ###

	"""."""
	def get_zones_data(self):
		return


	"""."""
	def get_zone_info(self, zone_id):
		return



