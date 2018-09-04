##################################################################
# A wrapper for the general game data in the D3 Community API.   #
# Part of BlizzPy.                                               #
#                                                                #
# Written by Lewis Kim.                                          #
##################################################################

import urllib, json
import pandas as pd


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class D3General:


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


	"""."""
	def _get_act_index_data_url(self):
		return


	"""."""
	def _get_act_data_url(self, actId):
		return


	""".

	   https://us.api.battle.net/d3/data/artisan/blacksmith?locale=en_US&apikey=..."""
	def _get_artisan_data_url(self, artisanSlug):
		url = "{root}/d3/data/artisan/{artisanSlug}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			artisanSlug = artisanSlug,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/artisan/blacksmith/recipe/apprentice-flamberge?locale=en_US&apikey=..."""
	def _get_recipe_data_url(self, artisanSlug, recipeSlug):
		url = "{root}/d3/data/artisan/{artisanSlug}/recipe/{recipeSlug}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			artisanSlug = artisanSlug,
			recipeSlug = recipeSlug,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/follower/templar?locale=en_US&apikey=..."""
	def _get_follower_data_url(self, followerSlug):
		url = "{root}/d3/data/follower/{followerSlug}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			followerSlug = followerSlug,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/hero/barbarian?locale=en_US&apikey=..."""
	def _get_character_class_data_url(self, classSlug):
		url = "{root}/d3/data/hero/{classSlug}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			classSlug = classSlug,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/hero/barbarian/skill/bash?locale=en_US&apikey=..."""
	def _get_skill_data_url(self, classSlug, skillSlug):
		url = "{root}/d3/data/hero/{classSlug}/skill/{skillSlub}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			classSlug = classSlug,
			skillSlug = skillSlug,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/item-type?locale=en_US&apikey=..."""
	def _get_itemtype_index_data_url(self):
		url = "{root}/d3/data/item-type?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/item-type/sword2h?locale=en_US&apikey=6j49d54nvcttpbhvsqxs6pcvqf5b7t9y"""
	def _get_itemtype_data_url(self, itemTypeSlug):
		url = "{root}/d3/data/item-type/{itemTypeSlug}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			itemTypeSlug = itemTypeSlug,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/item/corrupted-ashbringer-Unique_Sword_2H_104_x1?locale=en_US&apikey=..."""
	def _get_item_data_url(self, itemSlugAndId):
		url = "{root}/d3/data/item/{itemSlugAndId}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			itemSlugAndId = itemSlugAndId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving act data. ###


### Retrieving artisan and recipe data. ###


### Retrieving follower data. ###


### Retrieving character class and skill data. ###


### Retrieving item type data. ###


### Retrieving item data. ###



