##################################################################
# A wrapper for the guild data in Blizzard's WoW Community API.  #
# Part of BlizzPy.                                               #
#                                                                #
# Written by Lewis Kim.                                          #
##################################################################

import requests
import urllib, json
import pandas as pd




# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


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

		self.guild_data = {}
		self.ach_data = {}

		self.members_data = []
		self.news_data = []
		self.challenge_data = []





	"""."""
	def _api_request(self, endpoint):
		return

	"""."""
	def _get_data_url(self):
		url = "{root}/wow/guild/{realm}/{guild_name}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			guild_name = self.guild_name.replace(" ", "%20"),
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_data_with_field_url(self, field):
		url = "{root}/wow/guild/{realm}/{guild_name}?fields={field}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			guild_name = self.guild_name.replace(" ", "%20"),
			field = field,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving basic guild data. ###

	"""."""
	def get_guild_data(self):
		try:
			with urllib.request.urlopen(self._get_data_url()) as url:
				self.guild_data = json.loads(url.read().decode())

			return self.guild_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return the guild name and realm for this instance of WoWGuild."""
	def get_guild_name(self):
		return self.guild_name + "-" + self.realm


	"""."""
	def get_guild_emblem(self):
		if not self.guild_data:
			guild_data = self.get_guild_data()

		return self.guild_data['emblem']


### Retrieving guild members data. ###

	"""."""
	def get_members_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("members")) as url:
				self.members_data = json.loads(url.read().decode())['members']

			return self.members_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return

	"""."""
	def get_member_info(self, member_name):
		if not self.members_data:
			members_data = self.get_members_data()

		return next((member for member in self.members_data if member['character']['name'].lower() == member_name.lower()), None)


	"""."""
	def get_member_rank(self, member_name):
		if not self.members_data:
			members_data = self.get_members_data()

		return next((member['rank'] for member in self.members_data if member['character']['name'] == member_name), None)


	"""."""
	def get_num_members(self):
		if not self.members_data:
			members_data = self.get_members_data()

		return len(self.members_data)


	"""."""
	def get_members_names(self):
		if not self.members_data:
			members_data = self.get_members_data()

		return [member['character']['name'] for member in self.members_data]


	"""."""
	def get_members_by_spec(self, spec, as_names=False):
		if not self.members_data:
			members_data = self.get_members_data()

		if as_names:
			filtered_members = [member['character']['name'] for member in self.members_data if 'spec' in member['character'].keys() and member['character']['spec']['name'].lower() == spec.lower()]

		else:
			filtered_members = [member for member in self.members_data if 'spec' in member['character'].keys() and member['character']['spec']['name'].lower() == spec.lower()]

		return filtered_members


	"""."""
	def get_members_by_role(self, role, as_names=False):
		if role.lower() not in ['dps', 'tank', 'healer']:
			raise ValueError("Not a valid role.")
			return

		role_map = {'dps': 'DPS', 'healer': 'HEALING', 'tank': 'TANK'}
		role = role_map[role.lower()]

		if not self.members_data:
			members_data = self.get_members_data()

		if as_names:
			filtered_members = [member['character']['name'] for member in self.members_data if 'spec' in member['character'].keys() and member['character']['spec']['role'].lower() == role.lower()]

		else:
			filtered_members = [member for member in self.members_data if 'spec' in member['character'].keys() and member['character']['spec']['role'].lower() == role.lower()]

		return filtered_members


	"""."""
	def get_members_by_rank(self, rank, names=False):
		if not type(rank) == int:
			raise ValueError("Rank must be an integer.")
			return

		if not self.members_data:
			members_data = self.get_members_data()

		if names:
			filtered_members = [member['character']['name'] for member in self.members_data if member['rank'] == rank]

		else:
			filtered_members = [member for member in self.members_data if member['rank'] == rank]

		return filtered_members	


### Retrieving guild achievements data. ###

	"""."""
	def get_guild_achievements_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("achievements")) as url:
				self.ach_data = json.loads(url.read().decode())['achievements']

			return self.ach_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def guild_has_achievement(self, achievement_id):
		if not self.ach_data:
			ach_data = self.get_guild_achievements_data()

		if achievement_id in self.ach_data['achievementsCompleted']:
			return True

		return False


### Retrieving guild news feed data. ###

	"""."""
	def get_guild_news_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("news")) as url:
				self.news_data = json.loads(url.read().decode())['news']

			return self.news_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving guild challenges data. ###

	"""."""
	def get_guild_challenge_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("challenge")) as url:
				self.challenge_data = json.loads(url.read().decode())['challenge']

			return self.challenge_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_completed_challenges(self, as_names=False):
		if not self.challenge_data:
			challenge_data = self.get_guild_challenge_data()

		if as_names:
			return [challenge['map']['name'] for challenge in self.challenge_data if challenge['map']['hasChallengeMode']]

		else:
			return [challenge for challenge in self.challenge_data if challenge['map']['hasChallengeMode']]


	"""."""
	def has_challenge(self, name):
		if not self.challenge_data:
			challenge_data = self.get_guild_challenge_data()

		try:
			challenge = next((challenge for challenge in self.challenge_data if challenge['map']['name'].lower() == name.lower()))

			return challenge['map']['hasChallengeMode']

		except:
			raise ValueError("Invalid challenge name.")
			return

