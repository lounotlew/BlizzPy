##########################################
# A wrapper for the D3 Community API.    #
# D3General: General D3 Game Data.       #
# D3Profile: D3 Profile/Hero Data.       #
# Part of BlizzPy.                       #
#                                        #
# Written by Lewis Kim.                  #
##########################################

import urllib, json

# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class D3Profile:

	"""."""
	def __init__(self, api_key, battle_tag, locale="en_US", token=None):
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

		self.battle_tag = battle_tag

		self.locale = locale

		self.profile_data = {}
		self.hero_data = {}
		self.hero_items_data = {}
		self.follower_items_data = {}


	""".

	   https://us.api.battle.net/d3/profile/1931/?locale=en_US&apikey=..."""
	def _get_profile_data_url(self):
		url = "{root}/d3/profile/{battle_tag}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			battle_tag = self.battle_tag,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/profile/1931/hero/1?locale=en_US&apikey=..."""
	def _get_hero_data_url(self, hero_id):
		url = "{root}/d3/profile/{battle_tag}/hero/{hero_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			battle_tag = self.battle_tag,
			hero_id = hero_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/profile/1931/hero/1/items?locale=en_US&apikey=..."""
	def _get_hero_items_data_url(self, hero_id):
		url = "{root}/d3/profile/{battle_tag}/hero/{hero_id}/items?locale={locale}&apikey={api_key}".format(
			root = self.root,
			battle_tag = self.battle_tag,
			hero_id = hero_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/profile/1931/hero/1/follower-items?locale=en_US&apikey=..."""
	def _get_follower_items_data_url(self, hero_id):
		url = "{root}/d3/profile/{battle_tag}/hero/{hero_id}/follower-items?locale={locale}&apikey={api_key}".format(
			root = self.root,
			battle_tag = self.battle_tag,
			hero_id = hero_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving profile data. ###

	"""."""
	def get_profile_data(self):
		try:
			with urllib.request.urlopen(self._get_profile_data_url()) as url:
				self.profile_data = json.loads(url.read().decode())

			return self.profile_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


### Retrieving hero data. ###

	"""."""
	def get_hero_data(self, hero_id):
		try:
			with urllib.request.urlopen(self._get_hero_data_url(hero_id)) as url:
				self.hero_data = json.loads(url.read().decode())

			return self.hero_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


### Retrieving item data. ###

	"""."""
	def get_hero_items_data(self, hero_id):
		try:
			with urllib.request.urlopen(self._get_hero_items_data_url(hero_id)) as url:
				self.hero_items_data = json.loads(url.read().decode())

			return self.hero_items_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_follower_items_data(self, hero_id):
		try:
			with urllib.request.urlopen(self._get_follower_items_data_url(hero_id)) as url:
				self.follower_items_data = json.loads(url.read().decode())

			return self.follower_items_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


#
class D3General:

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

		self.act_index_data = {}
		self.act_data = {}


	""".

	   https://us.api.battle.net/d3/data/act?locale=en_US&apikey=..."""
	def _get_act_index_data_url(self):
		url = "{root}/d3/data/act?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/d3/data/act/1?locale=en_US&apikey=..."""
	def _get_act_data_url(self, act_id):
		url = "{root}/d3/data/act/{act_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			act_id = act_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


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

	"""."""
	def get_act_index_data(self):
		try:
			with urllib.request.urlopen(self._get_act_index_data_url()) as url:
				self.act_index_data = json.loads(url.read().decode())

			return self.act_index_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_act_data(self, act_id):
		try:
			with urllib.request.urlopen(self._get_act_data_url(act_id)) as url:
				self.act_data = json.loads(url.read().decode())

			return self.act_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


### Retrieving artisan and recipe data. ###

	"""."""
	def get_artisan_data(self, artisanSlug):
		try:
			with urllib.request.urlopen(self._get_artisan_data_url(artisanSlug)) as url:
				self.artisan_data = json.loads(url.read().decode())

			return self.artisan_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_recipe_data(self, artisanSlug, recipeSlug):
		try:
			with urllib.request.urlopen(self._get_recipe_data_url(artisanSlug, recipeSlug)) as url:
				self.recipe_data = json.loads(url.read().decode())

			return self.recipe_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


### Retrieving follower data. ###

	"""."""
	def get_follower_data(self, followerSlug):
		try:
			with urllib.request.urlopen(self._get_follower_data_url(followerSlug)) as url:
				self.follower_data = json.loads(url.read().decode())

			return self.follower_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


### Retrieving character class and skill data. ###

	"""."""
	def get_character_class_data(self, classSlug):
		try:
			with urllib.request.urlopen(self._get_character_class_data_url(classSlug)) as url:
				self.character_class_data = json.loads(url.read().decode())

			return self.character_class_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_skill_data(self, classSlug, skillSlug):
		try:
			with urllib.request.urlopen(self._get_skill_data_url(classSlug, skillSlug)) as url:
				self.skill_data = json.loads(url.read().decode())

			return self.skill_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


### Retrieving item data. ###

	"""."""
	def get_itemtype_index_data(self):
		try:
			with urllib.request.urlopen(self._get_itemtype_index_data_url()) as url:
				self.itemtype_index_data = json.loads(url.read().decode())

			return self.itemtype_index_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_itemtype_data(self, itemTypeSlug):
		try:
			with urllib.request.urlopen(self._get_itemtype_data_url(itemTypeSlug)) as url:
				self.itemtype_data = json.loads(url.read().decode())

			return self.itemtype_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_item_data(self, itemSlugAndId):
		try:
			with urllib.request.urlopen(self._get_item_data_url(itemSlugAndId)) as url:
				self.item_data = json.loads(url.read().decode())

			return self.item_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return

