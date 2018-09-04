#############################################################
# A wrapper for the profile data in the D3 Community API.   #
# Part of BlizzPy.                                          #
#                                                           #
# Written by Lewis Kim.                                     #
#############################################################

import urllib, json
import pandas as pd


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class D3Profile:


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
	def get_hero_items_data_url(self, hero_id):
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
	def get_follower_items_data_url(self, hero_id):
		url = "{root}/d3/profile/{battle_tag}/hero/{hero_id}/follower-items?locale={locale}&apikey={api_key}".format(
			root = self.root,
			battle_tag = self.battle_tag,
			hero_id = hero_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving profile data. ###


### Retrieving hero data. ###


### Retrieving item data. ###




