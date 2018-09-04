#############################################################
# A wrapper for the ladder data in the SC2 Community API.   #
# Part of BlizzPy.                                          #
#                                                           #
# Written by Lewis Kim.                                     #
#############################################################

import urllib, json
import pandas as pd
import statistics


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class SC2Ladder:


	def __init__(self, api_key, ladder_id, locale="en_US", token=None):
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

		self.ladder_id = ladder_id

		self.locale = locale

		self.ladder_data = {}


	""".

	   https://us.api.battle.net/sc2/ladder/194163?locale=en_US&apikey=..."""
	def _get_ladder_data_url(self):
		url = "{root}/sc2/ladder/{ladder_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			ladder_id = self.ladder_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving ladder data. ###

	"""."""
	def get_ladder_data(self):
		try:
			with urllib.request.urlopen(self._get_ladder_data_url()) as url:
				self.ladder_data = json.loads(url.read().decode())

			return self.ladder_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_ladder_members(self, as_names=False):
		if not self.ladder_data:
			self.get_ladder_data()

		if as_names:
			return [member['character']['displayName'] for member in self.ladder_data['ladderMembers']]

		else:
			return [member for member in self.ladder_data['ladderMembers']]


	"""."""
	def search_ladder_member(self, name):
		if not self.ladder_data:
			self.get_ladder_data()

		return next((member for member in self.ladder_data['ladderMembers'] if member['character']['displayName'] == name), None)


	"""."""
	def get_ladder_avg_rank(self):
		if not self.ladder_data:
			self.get_ladder_data()

		return round(statistics.mean([member['highestRank'] for member in self.ladder_data['ladderMembers']]), 2)


	"""."""
	def get_member_winrates(self):
		if not self.ladder_data:
			self.get_ladder_data()

		return {member['character']['displayName']:round(100*member['wins']/(member['wins']+member['losses']), 2) for member in self.ladder_data['ladderMembers']}


	"""."""
	def get_ladder_avg_winrate(self):
		if not self.ladder_data:
			self.get_ladder_data()

		winrates = [round(100*member['wins']/(member['wins']+member['losses']), 2) for member in self.ladder_data['ladderMembers']]

		return statistics.mean(winrates)


	"""."""
	def get_ladder_favorite_races(self):
		if not self.ladder_data:
			self.get_ladder_data()

		return {member['character']['displayName']:member['favoriteRaceP1'] for member in self.ladder_data['ladderMembers']}

