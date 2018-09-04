#####################################################################
# A wrapper for the game resources data in the SC2 Community API.   #
# Part of BlizzPy.                                                  #
#                                                                   #
# Written by Lewis Kim.                                             #
#####################################################################

import urllib, json
import pandas as pd


# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]


#
class SC2Resources:


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
	def get_achievement_nameID_dict(self):
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
	def search_reward_by_id(self, reward_id):
		if not self.achievements_data:
			self.get_rewards_data()

		rewards_by_category = list(self.rewards_data.values())
		joined_rewards = []
		for i in range(len(rewards_by_category)):
			joined_rewards += rewards_by_category[i]

		return next((reward for reward in joined_rewards if reward['id'] == reward_id), None)


	"""."""
	def search_reward_by_name(self, reward_name):
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
	def get_terranDecals(self):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['terranDecals']]

		else:
			return self.rewards_data['terranDecals']


	"""."""
	def get_zergDecals(self):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['zergDecals']]

		else:
			return self.rewards_data['zergDecals']


	"""."""
	def get_protossDecals(self):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['protossDecals']]

		else:
			return self.rewards_data['protossDecals']


	"""."""
	def get_skins(self):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['skins']]

		else:
			return self.rewards_data['skins']


	"""."""
	def get_animations(self):
		if not self.achievements_data:
			self.get_rewards_data()

		if as_names:
			return [reward['title'] for reward in self.rewards_data['animations']]

		else:
			return self.rewards_data['animations']

