##############################################################
# A wrapper for the profile data in the SC2 Community API.   #
# Part of BlizzPy.                                           #
#                                                            #
# Written by Lewis Kim.                                      #
##############################################################

import urllib, json
import pandas as pd


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class SC2Profile:


	def __init__(self, api_key, profile_id, profile_name, region_id=1, locale="en_US", token=None):
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

		self.profile_id = profile_id
		self.region_id = region_id
		self.profile_name = profile_name

		self.locale = locale

		self.profile_data = {}


	""".

	   https://us.api.battle.net/sc2/profile/2376042/1/Ophidian/?locale=en_US&apikey=..."""
	def _get_profile_data_url(self):
		url = "{root}/sc2/profile/{profile_id}/{region_id}/{profile_name}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			profile_id = self.profile_id,
			region_id = self.region_id,
			profile_name = self.profile_name,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_profile_ladders_data_url(self):
		return


	"""."""
	def _get_match_history_data_url(self):
		return


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


	"""."""
	def get_clan_name(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['clanName']


	"""."""
	def get_clan_tag(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['clanTag']


	"""."""
	def get_profile_career_data(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['career']


	"""."""
	def get_primary_race(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['career']['primaryRace']


	"""."""
	def get_race_wins(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		career_data = self.profile_data['career']

		return {'Terran Wins': career_data['terranWins'], 'Protoss Wins': career_data['protossWins'], 'Zerg Wins': career_data['zergWins']}


	"""."""
	def get_season_total_games(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['career']['seasonTotalGames']


	"""."""
	def get_career_total_games(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['career']['careerTotalGames']


	"""."""
	def get_season_winrate(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		if self.profile_data['career']['seasonTotalGames'] == 0:
			return None

		numWins = self.profile_data['career']['terranWins'] + self.profile_data['career']['protossWins'] + self.profile_data['career']['zergWins']

		return round((100*numWins/self.profile_data['career']['seasonTotalGames']), 2)


	"""."""
	def get_highest_1v1_rank(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['career']['highest1v1Rank']


	"""."""
	def get_highest_team_rank(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['career']['highestTeamRank']


	"""."""
	def get_profile_rewards(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['rewards']


	"""."""
	def has_earned_reward(self, reward_id):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return reward_id in self.profile_data['rewards']['earned']


	"""."""
	def get_profile_achievements(self, as_df=False):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['achievements']


	"""."""
	def get_total_achievement_points(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['achievements']['points']['totalPoints']


	"""."""
	def get_achievement_points_by_category(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['achievements']['points']['categoryPoints']


	"""."""
	def has_earned_achievement(self, achievement_id):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		achievement_ids = [ach['achievementId'] for ach in self.profile_data['achievements']['achievements']]

		return achievement_id in achievement_ids


### Retrieving profile ladders data. ###




### Retrieving profile match history data. ###


















