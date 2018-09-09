##################################################
# A wrapper for the the SC2 Community API.       #
# SC2Profile: SC2 Profile Data.                  #
# SC2Ladder: SC2 Ladder Data.                    #
# SC2Resources: SC2 Achievements/Rewards Data.   #
# Part of BlizzPy.                               #
#                                                #
# Written by Lewis Kim.                          #
##################################################

import requests
import urllib, json

# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class SC2Profile:

	"""."""
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
		self.ladders_data = {}
		self.match_history = {}


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


	""".

	   https://us.api.battle.net/sc2/profile/3873960/1/Zorniza/ladders?locale=en_US&apikey=..."""
	def _get_profile_ladders_data_url(self):
		url = "{root}/sc2/profile/{profile_id}/{region_id}/{profile_name}/ladders?locale={locale}&apikey={api_key}".format(
			root = self.root,
			profile_id = self.profile_id,
			region_id = self.region_id,
			profile_name = self.profile_name,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/sc2/profile/3873960/1/Zorniza/matches?locale=en_US&apikey=..."""
	def _get_match_history_data_url(self):
		url = "{root}/sc2/profile/{profile_id}/{region_id}/{profile_name}/matches?locale={locale}&apikey={api_key}".format(
			root = self.root,
			profile_id = self.profile_id,
			region_id = self.region_id,
			profile_name = self.profile_name,
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
	def get_profile_career(self):
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
	def get_profile_achievements(self):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		return self.profile_data['achievements']


	# """."""
	# def get_total_achievement_points(self):
	# 	if not self.profile_data:
	# 		profile_data = self.get_profile_data()

	# 	return self.profile_data['achievements']['points']['totalPoints']


	# """."""
	# def get_achievement_points_by_category(self):
	# 	if not self.profile_data:
	# 		profile_data = self.get_profile_data()

	# 	return self.profile_data['achievements']['points']['categoryPoints']


	"""."""
	def has_earned_achievement(self, achievement_id):
		if not self.profile_data:
			profile_data = self.get_profile_data()

		achievement_ids = [ach['achievementId'] for ach in self.profile_data['achievements']['achievements']]

		return achievement_id in achievement_ids


### Retrieving profile ladders data. ###

	"""."""
	def get_profile_ladder_data(self):
		try:
			with urllib.request.urlopen(self._get_profile_ladders_data_url()) as url:
				self.ladders_data = json.loads(url.read().decode())

			return self.ladders_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_current_ladder(self):
		if not self.ladders_data:
			ladders_data = self.get_profile_ladder_data()

		if not self.ladders_data['currentSeason']:
			return None

		return self.ladders_data['currentSeason'][0]['ladder'][0]


	"""."""
	def get_current_ladder_name(self):
		if not self.ladders_data:
			ladders_data = self.get_profile_ladder_data()

		if not self.ladders_data['currentSeason'][0]['ladder']:
			return None

		return self.ladders_data['currentSeason'][0]['ladder'][0]['ladderName']


	"""."""
	def get_current_league(self):
		if not self.ladders_data:
			ladders_data = self.get_profile_ladder_data()

		if not self.ladders_data['currentSeason'][0]['ladder']:
			return None

		return self.ladders_data['currentSeason'][0]['ladder'][0]['league']


### Retrieving profile match history data. ###

	"""."""
	def get_match_history_data(self):
		try:
			with urllib.request.urlopen(self._get_match_history_data_url()) as url:
				self.match_history = json.loads(url.read().decode())

			return self.match_history

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def num_games_played(self):
		if not self.match_history:
			match_history = self.get_match_history_data()

		return len(self.match_history['matches'])


	"""."""
	def total_winrate(self):
		if not self.match_history:
			match_history = self.get_match_history_data()

		num_games = len(self.match_history['matches'])
		num_wins = len([game for game in self.match_history['matches'] if game['decision'] == "WIN"])

		return round((100*num_wins/num_games), 2)


	"""."""
	def solo_winrate(self):
		if not self.match_history:
			match_history = self.get_match_history_data()

		num_games = len([game for game in self.match_history['matches'] if game['type'] == "SOLO"])
		num_wins = len([game for game in self.match_history['matches'] if game['decision'] == "WIN" and game['type'] == "SOLO"])

		return round((100*num_wins/num_games), 2)


	"""."""
	def get_solo_games(self):
		if not self.match_history:
			match_history = self.get_match_history_data()

		solo_games = [game for game in self.match_history['matches'] if game['type'] == "SOLO"]

		return solo_games


#
class SC2Ladder:

	"""."""
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


#
class SC2Resources:

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
		self.rewards_data = {}


	""".

	   https://us.api.battle.net/sc2/data/achievements?locale=en_US&apikey=..."""
	def _get_achievements_data_url(self):
		url = "{root}/sc2/data/achievements?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   https://us.api.battle.net/sc2/data/rewards?locale=en_US&apikey=..."""
	def _get_rewards_data_url(self):
		url = "{root}/sc2/data/rewards?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url

### Retrieving game achievements data. ###

	"""."""
	def get_achievements_data(self):
		try:
			with urllib.request.urlopen(self._get_achievements_data_url()) as url:
				self.achievements_data = json.loads(url.read().decode())

			return self.achievements_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_achievement_names(self):
		if not self.achievements_data:
			self.get_achievements_data()

		return [achievement['title'] for achievement in self.achievements_data['achievements']]


	"""."""
	def get_achievement_nameToID_dict(self):
		if not self.achievements_data:
			self.get_achievements_data()

		return {achievement['title']:achievement['achievementId'] for achievement in self.achievements_data['achievements']}



### Retrieving game rewards data. ###

	"""."""
	def get_rewards_data(self):
		try:
			with urllib.request.urlopen(self._get_rewards_data_url()) as url:
				self.rewards_data = json.loads(url.read().decode())

			return self.rewards_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, profile ID, region ID, or profile name.")
			return


	"""."""
	def get_reward_by_id(self, reward_id):
		if not self.achievements_data:
			self.get_rewards_data()

		rewards_by_category = list(self.rewards_data.values())
		joined_rewards = []
		for i in range(len(rewards_by_category)):
			joined_rewards += rewards_by_category[i]

		return next((reward for reward in joined_rewards if reward['id'] == reward_id), None)


	"""."""
	def get_reward_by_name(self, reward_name):
		if not self.achievements_data:
			self.get_rewards_data()

		rewards_by_category = list(self.rewards_data.values())
		joined_rewards = []
		for i in range(len(rewards_by_category)):
			joined_rewards += rewards_by_category[i]

		return next((reward for reward in joined_rewards if reward['title'] == reward_name), None)


	"""."""
	def get_portraits(self, as_names=False):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['portraits']]

		else:
			return self.rewards_data['portraits']



	"""."""
	def get_terranDecals(self, as_names=False):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['terranDecals']]

		else:
			return self.rewards_data['terranDecals']


	"""."""
	def get_zergDecals(self, as_names=False):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['zergDecals']]

		else:
			return self.rewards_data['zergDecals']


	"""."""
	def get_protossDecals(self, as_names=False):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['protossDecals']]

		else:
			return self.rewards_data['protossDecals']


	"""."""
	def get_skins(self, as_names=False):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['skins']]

		else:
			return self.rewards_data['skins']


	"""."""
	def get_animations(self, as_names=False):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['animations']]

		else:
			return self.rewards_data['animations']

