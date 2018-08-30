#####
#
#
#
# Written by Lewis Kim.
######

import requests
import urllib, json
import pandas as pd







#
class WoWGuild:

	""".

	   PARAMS:
	   self.root:
	   self.api_key:
	   self.locale:
	   self.characterName:
	   self.realm:"""
	def __init__(self, api_key, guild_name, realm, locale="en_US", token=None):
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

		self.guild_name = guild_name
		self.realm = realm


	"""."""
	def _api_request(self, endpoint):
		return

	"""."""
	def _get_data(self):
		url = "{root}/wow/guild/{realm}/{guild_name}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			guild_name = self.guild_name.replace(" ", "%20"),
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_data_with_field(self, field):
		url = "{root}/wow/guild/{realm}/{guild_name}?fields={field}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			guild_name = self.guild_name.replace(" ", "%20"),
			field = field,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""Return the guild name and realm for this instance of WoWGuild."""
	def guild_name(self):
		return self.guild_name + "-" + self.realm


### Retrieving basic guild data. ###

	"""."""
	def get_guild_data(self):
		return


	"""."""
	def get_guild_emblem(self):
		return



### Retrieving guild members data. ###

	"""."""
	def get_guild_members_data(self):
		return


	"""."""
	def get_num_guild_members(self):
		return


	"""."""
	def get_guild_members_names(self, ordered=False):
		return


	"""."""
	def get_guild_members_by_spec(self, spec, ordered=False):
		return


	"""."""
	def get_guild_members_by_roles(self, role, ordered=False):
		return


	"""."""
	def get_guild_members_descriptions(self, members, ordered=False):
		return


### Retrieving guild achievements data. ###

	"""."""
	def get_guild_achievements_data(self):
		return



### Retrieving guild news feed data. ###

	"""."""
	def get_guild_news_data(self):
		return


### Retrieving guild challenges data. ###

	"""."""
	def get_guild_challenge_data(self):
		return













