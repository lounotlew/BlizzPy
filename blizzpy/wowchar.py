######################################################################
# A wrapper for the character data in Blizzard's WoW Community API.  #
# Part of BlizzPy.                                                   #
#                                                                    #
# Written by Lewis Kim.                                              #
######################################################################

import urllib, json
import pandas as pd

# Accepted API locales. zh_TW has been excluded for now due to continuous "503 Service Unavailable" errors from the Blizzard API.
# To add: zh_TW
accepted_locales = ["en_US", "en_GB", "ko_KR"]

# A dictionary that maps the "class integer" to its full class name,
# e.g. '6': 'Death Knight'
int_to_class = {'1': 'Warrior', '2': 'Paladin', '3': 'Hunter', '4': 'Rogue', '5': 'Priest', '6': 'Death Knight',
	'7': 'Shaman', '8': 'Mage', '9': 'Warlock', '10': 'Monk', '11': 'Druid', '12': 'Demon Hunter'}

# A dictionary that maps the "race integer" to its full race name,
# e.g. '1': 'Human'
int_to_race = {'1': 'Human', '2': 'Orc', '3': 'Dwarf', '4': 'Night Elf', '5': 'Forsaken/Undead', '6': 'Tauren',
	'7': 'Gnome', '8': 'Troll', '9': 'Goblin', '10': 'Blood Elf', '11': 'Draenei', '22': 'Worgen',
	'25': 'Pandaren', '27': 'Nightborne', '28': 'Highmountain Tauren', '29': 'Void Elf', '30': 'Lightforged Draenei'}

# A dictionary that maps a character's class to their available specs.
class_to_spec = {'Warrior': ['arms', 'fury', 'protection'], 'Paladin': ['holy', 'protection', 'retribution'],
	'Hunter': ['beast mastery', 'marksmanship', 'survival'], 'Rogue': ['assassination', 'outlaw', 'subtlety'],
	'Priest': ['discipline', 'holy', 'shadow'], 'Death Knight': ['blood', 'frost', 'unholy'],
	'Shaman': ['elemental', 'enhancement', 'restoration'], 'Mage': ['arcane', 'fire', 'frost'],
	'Warlock': ['affliction', 'demonology', 'destruction'], 'Monk': ['brewmaster', 'mistweaver', 'windwalker'], 
	'Druid': ['balance', 'feral', 'guardian', 'restoration'], 'Demon Hunter': ['havoc', 'vengeance']}

# 
# Currently suppo
class WoWCharacter:

	""".

	   PARAMS:
	   self.root:
	   self.api_key:
	   self.locale:
	   self.characterName:
	   self.realm:"""
	def __init__(self, api_key, characterName, realm, locale="en_US", token=None):
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

		self.characterName = characterName
		self.realm = realm

		#
		self.character_data = {}
		self.ach_data = {}
		self.appearance_data = {}
		self.guild_data = {}
		self.hunter_pet_data = {}
		self.items_data = {}
		self.mounts_data = {}
		self.pets_data = {}
		self.professions_data = {}
		self.pvp_data = {}
		self.statistics_data = {}
		self.stats_data = {}

		#
		self.feed_data = []
		self.raid_prog_data = []
		self.quests_data = []
		self.rep_data = []
		self.talents_data = []
		self.titles_data = []



	"""."""
	def _api_request(self, endpoint):
		return


	"""."""
	def _get_data_url(self):
		url = "{root}/wow/character/{realm}/{characterName}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			characterName = self.characterName,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_data_with_field_url(self, field):
		url = "{root}/wow/character/{realm}/{characterName}?fields={field}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			characterName = self.characterName,
			field = field,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving basic character data. ###

	"""Return basic character data of self.characterName as a Python dictionary, decoded from a JSON request.

	   Keys:
	   lastModified, name, realm, battlegroup, class, race, gender, level, achievementPoints, thumbnail,
	   calcClass, faction, totalHonorableKills."""
	def get_character_data(self):
		try:
			with urllib.request.urlopen(self._get_data_url()) as url:
				self.character_data = json.loads(url.read().decode())

			return self.character_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return self.characterName's class. See int_to_class for details."""
	def get_class(self):
		# Check if self.character_data is empty, i.e. if self.get_character_data() has been called yet.
		# If empty, call self.get_character_data() to point self.character_data and minimize API calls.
		if not self.character_data:
			char_data = self.get_character_data()

		return int_to_class[str(self.character_data['class'])]


	"""Return self.characterName's race. See int_to_race for details."""
	def get_race(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return int_to_race[str(self.character_data['race'])]


	"""Return self.characterName's gender."""
	def get_gender(self):
		if not self.character_data:
			char_data = self.get_character_data()

		if self.character_data['gender'] == 0:
			return "Male"

		else:
			return "Female"


	"""Return self.characterName's level."""
	def get_level(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['level']


	"""Return self.characterName's total achievement points."""
	def get_achPoints(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['achievementPoints']


	"""Return self.characterName's faction."""
	def get_faction(self):
		if not self.character_data:
			char_data = self.get_character_data()

		if self.character_data['faction'] == 0:
			return "Alliance"

		else:
			return "Horde"


### Retrieving the character's achievements data. ###

	"""Return self.characterName's achievements data as a dictionary, decoded from json.

	   Keys: achievementsCompleted:
	         achievementsCompletedTimestamp: 
	         criteria: 
	         criteriaQuantity: 
	         criteriaTimestamp: 
	         criteriaCreated: """
	def get_achievement_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("achievements")) as url:
				self.ach_data = json.loads(url.read().decode())['achievements']

			return self.ach_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return self.ach_data as a pandas dataframe, with 2 columns: the IDs of all completed achievements (achievementsCompleted),
	   and the timestamps of their completions (achievementsCompletedTimestamp).

	   If ascending_time is True, sort the dataframe by ascending timestamp order and return it."""
	def get_achievements_df(self, ascending_time=False):
		if not self.ach_data:
			ach_data = self.get_achievement_data()

		df = pd.DataFrame({'achievementsCompleted': pd.Series(self.ach_data['achievementsCompleted']),
							'achievementsCompletedTimestamp': pd.Series(self.ach_data['achievementsCompletedTimestamp'])})

		if ascending_time:
			#sort
			return

		else:
			return df

	# More?


### Retrieving the character's appearance data. ###

	"""Return self.characterName's appearance data as a dictionary, decoded from json.
	   Appearance refers to character features, such as face/haircolor, not transmog.

	   Keys: skinColor:
	         hairVariation: 
	         hairColor: 
	         featureVariation: 
	         showHelm: 
	         showCloak: 
	         customDisplayOptions: """
	def get_appearance_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("appearance")) as url:
				self.appearance_data = json.loads(url.read().decode())['appearance']

			return self.appearance_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return self.characterName's facial features integer."""
	def get_facial_features(self):
		if not self.appearance_data:
			appearance_data = self.get_appearance_data()

		return self.appearance_data['faceVariation']


	"""Return self.characterName's skin color integer."""
	def get_skincolor(self):
		if not self.appearance_data:
			appearance_data = self.get_appearance_data()

		return self.appearance_data['skinColor']


	"""Return self.characterName's hair style integer."""
	def get_hairstyle(self):
		if not self.appearance_data:
			appearance_data = self.get_appearance_data()

		return self.appearance_data['hairVariation']


	"""Return self.characterName's hair color integer."""
	def get_haircolor(self):
		if not self.appearance_data:
			appearance_data = self.get_appearance_data()

		return self.appearance_data['hairColor']


### Retrieving the character's feed (activity) data. ###

	"""Return the """
	def get_feed_data(self, as_df=False):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("feed")) as url:
				self.feed_data = json.loads(url.read().decode())['feed']

			return self.feed_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving the character's guild data. ###

	"""."""
	def get_guild_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("guild")) as url:
				self.guild_data = json.loads(url.read().decode())['guild']

			return self.guild_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return

	
	"""."""
	def get_guild_name(self):
		if not self.guild_data:
			guild_data = self.get_appearance_data()

		return self.guild_data['name']


	"""."""
	def get_num_guild_members(self):
		if not self.guild_data:
			guild_data = self.get_appearance_data()

		return self.guild_data['members']


	"""."""
	def get_guild_ach_points(self):
		if not self.guild_data:
			guild_data = self.get_appearance_data()

		return self.guild_data['achievementPoints']


### Retrieving the character's hunter pet data, given that the character is a hunter. ###

	"""...

	   Returns a list of dictionaries containing data on each of self.characterName's pets."""
	def get_hunter_pet_data(self):
		# Check if self.character_data isn't empty. If it isn't, check if the selected character is a Hunter.
		error_msg = self.characterName + "-" + self.realm + " is not a Hunter."
		if self.character_data:
			if self.get_class() != "Hunter":
				raise ValueError(error_msg)
				return

		else:
			character_data = self.get_character_data()

			if self.get_class() != "Hunter":
				raise ValueError(error_msg)
				return

		try:
			with urllib.request.urlopen(self._get_data_with_field_url("hunterPets")) as url:
				self.hunter_pet_data = json.loads(url.read().decode())['hunterPets']

			return self.hunter_pet_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return a list of self.characterName's pet names, given the character is a Hunter."""
	def get_hunter_pet_names(self):
		if not self.hunter_pet_data:
			hunter_pet_data = self.get_hunter_pet_data()

		else:
			return [pet['name'] for pet in self.hunter_pet_data]


	"""Return the first element of self.hunter_pet_data whose 'name' key matches PET_NAME.
	   The element is a nested dictionary that contains all the data about the pet from the Blizzard API.
	   If there is no match, return None."""
	def get_hunter_pet_info(self, pet_name):
		if not self.hunter_pet_data:
			hunter_pet_data = self.get_hunter_pet_data()

		for pet in self.hunter_pet_data:
			if pet['name'] == pet_name:
				return pet

		return None


### Retrieving the character's equiped items data. ###

	"""."""
	def get_items_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("items")) as url:
				self.items_data = json.loads(url.read().decode())['items']

			return self.items_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Return a tuple containing self.characterName's item levels. The first element is the total ilvl, and
	   the second element is the equipped ilvl."""
	def get_ilvl(self):
		if not self.items_data:
			items_data = self.get_items_data()

		return self.items_data['averageItemLevel'], self.items_data['averageItemLevelEquipped']


	"""."""
	def get_gear_piece(self, slot_name):
		if not self.items_data:
			items_data = self.get_items_data()

		if slot_name not in list(self.items_data.keys())[2:]:
			return None

		return self.items_data[slot_name]


### Retrieving the character's mounts data. ###

	"""."""
	def get_mount_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("mounts")) as url:
				self.mounts_data = json.loads(url.read().decode())['mounts']

			return self.mounts_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_mount(self, mount_name):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		for mount in all_mounts:
			if mount['name'] == mount_name:
				return mount

		return None


	"""."""
	def get_mount_names(self):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		return [mount['name'] for mount in all_mounts]


	"""."""
	def get_ground_mounts(self):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		return [mount for mount in all_mounts if mount['isGround'] == True]


	"""."""
	def get_flying_mounts(self):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		return [mount for mount in all_mounts if mount['isFlying'] == True]


### Retrieving the character's non-hunter pets data. ###

	"""."""
	def get_pets_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("pets")) as url:
				self.pets_data = json.loads(url.read().decode())['pets']

			return self.pets_data

			return 

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_num_pets(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		return self.pets_data['numCollected']


	"""."""
	def get_percent_collected(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		perc = round(100*self.pets_data['numCollected']/(self.pets_data['numCollected'] + self.pets_data['numNotCollected']), 2)

		return perc


	"""."""
	def get_pet_names(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()
		return [pet['name'] for pet in self.pets_data['collected']]


	"""."""
	def get_pet_ids(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		return [pet['creatureID'] for pet in self.pets_data['collected']]


	"""."""
	def get_favorite_pets(self, as_names=True):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		if as_names:
			favorite_pets = [pet['name'] for pet in self.pets_data['collected'] if pet['isFavorite']]

		else:
			favorite_pets = [pet for pet in self.pets_data['collected'] if pet['isFavorite']]

		return favorite_pets		


	"""."""
	def get_pet_quality(self, pet_name):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		quality = next((pet['stats']['petQualityId'] for pet in self.pets_data['collected'] if pet['name'].lower() == pet_name.lower()), None)

		return quality
		


	"""."""
	def get_pet_stats(self, pet_name):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		stats = next((pet['stats'] for pet in self.pets_data['collected'] if pet['name'].lower() == pet_name.lower()), None)

		return stats


### Retrieving the character's professions data. ###

	"""."""
	def get_professions_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("professions")) as url:
				self.professions_data = json.loads(url.read().decode())['professions']

			return self.professions_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_primary_professions(self):
		if not self.professions_data:
			professions_data = self.professions_data

		primary_profs = professions['primary']

		if len(primary_profs) == 0:
			return None

		return {prof['name']: prof['rank'] for prof in primary_profs}


	"""."""
	def get_secondary_professions(self):
		if not self.professions_data:
			professions_data = self.professions_data

		secondary_profs = professions['secondary']

		if len(secondary_profs) == 0:
			return None

		return {prof['name']: prof['rank'] for prof in secondary_profs}


### Retrieving the character's raid progression data. ###

	"""."""
	def get_raid_prog_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("progression")) as url:
				raid_prog_data = json.loads(url.read().decode())['progression']

			self.raid_prog_data = raid_prog_data['raids']

			return self.raid_prog_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_raid_prog(self, raid_name):
		if not self.raid_prog_data:
			raid_prog_data = self.get_raid_prog_data()

		if raid_name.lower() not in [raid['name'].lower() for raid in self.raid_prog_data]:
			raise ValueError("That raid does not exist. Please check its spelling. Upper/lowercase does not matter.")
			return

		raid = next((raid for raid in self.raid_prog_data if raid['name'].lower() == raid_name.lower()), None)

		return raid


	"""

	   *Mythic difficulty kills start from SoO."""
	def get_num_boss_kills(self, boss_name, raid_name, difficulty):
		accepted_difficulties = ["lfr", "normal", "heroic", "mythic"]

		if difficulty.lower() not in accepted_difficulties:
			raise ValueError("Invalid difficulty. Your difficulty must be all, LFR, normal, heroic, or mythic.")
			return

		if not self.raid_prog_data:
			raid_prog_data = self.get_raid_prog_data()

		if raid_name.lower() not in [raid['name'].lower() for raid in self.raid_prog_data]:
			raise ValueError("That raid does not exist. Please check its spelling. Upper/lowercase does not matter.")
			return

		raid = next((raid for raid in self.raid_prog_data if raid['name'].lower() == raid_name.lower()), None)
		bosses = raid['bosses']

		if boss_name.lower() not in [boss['name'].lower() for boss in bosses]:
			raise ValueError("That boss does not exist in that raid. Please check its spelling. Upper/lowercase does not matter.")
			return

		difficulty_to_kills = {'lfr': 'lfrKills', 'normal': 'normalKills', 'heroic': 'heroicKills', 'mythic': 'mythicKills'}

		numKillsKey = difficulty_to_kills[difficulty.lower()]

		try:
			return next((boss for boss in bosses if boss['name'].lower() == boss_name.lower()), None)[numKillsKey]

		except:
			raise ValueError("That boss doesn't have that difficulty.")
			return


	"""

	   *Mythic difficulty kills start from SoO."""
	def get_boss_kill_time(self, boss_name, raid, difficulty):
		accepted_difficulties = ["lfr", "normal", "heroic", "mythic"]

		if difficulty.lower() not in accepted_difficulties:
			raise ValueError("Invalid difficulty. Your difficulty must be all, LFR, normal, heroic, or mythic.")
			return

		if not self.raid_prog_data:
			raid_prog_data = self.get_raid_prog_data()

		if raid_name.lower() not in [raid['name'].lower() for raid in self.raid_prog_data]:
			raise ValueError("That raid does not exist. Please check its spelling. Upper/lowercase does not matter.")
			return

		raid = next((raid for raid in self.raid_prog_data if raid['name'].lower() == raid_name.lower()), None)
		bosses = raid['bosses']

		if boss_name.lower() not in [boss['name'].lower() for boss in bosses]:
			raise ValueError("That boss does not exist in that raid. Please check its spelling. Upper/lowercase does not matter.")
			return

		difficulty_to_killtime = {'lfr': 'lfrTimestamp', 'normal': 'normalTimestamp', 'heroic': 'heroicTimestamp', 'mythic': 'mythicTimestamp'}

		killtimeKey = difficulty_to_kills[difficulty.lower()]

		try:
			return next((boss for boss in bosses if boss['name'].lower() == boss_name.lower()), None)[killtimeKey]

		except:
			raise ValueError("That boss doesn't have that difficulty.")
			return


### Retrieving the character's PVP statistics. ###

	"""

	   Returns"""
	def get_pvp_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("pvp")) as url:
				pvp_data = json.loads(url.read().decode())['pvp']

			self.pvp_data = pvp_data['brackets']

			return self.pvp_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""

	   Returns"""
	def get_battlegroup(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['battlegroup']


	"""

	   Returns"""
	def get_totalHK(self):
		if not self.character_data:
			char_data = self.get_character_data()

		return self.character_data['totalHonorableKills']


	"""

	   Returns"""
	def get_2v2_stats(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		return self.pvp_data['ARENA_BRACKET_2v2']


	"""

	   Returns"""
	def get_2v2_rating(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		return self.pvp_data['ARENA_BRACKET_2v2']['rating']


	"""."""
	def get_2v2_winrate(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		if self.pvp_data['ARENA_BRACKET_2v2']['seasonPlayed'] == 0:
			return None

		win_perc = round(self.pvp_data['ARENA_BRACKET_2v2']['seasonWon']*100 / self.pvp_data['ARENA_BRACKET_2v2']['seasonPlayed'], 2)

		return win_perc


	"""

	   Returns"""
	def get_3v3_stats(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		return self.pvp_data['ARENA_BRACKET_3v3']


	"""

	   Returns"""
	def get_3v3_rating(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		return self.pvp_data['ARENA_BRACKET_3v3']['rating']


	"""."""
	def get_3v3_winrate(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		if self.pvp_data['ARENA_BRACKET_3v3']['seasonPlayed'] == 0:
			return None

		win_perc = round(self.pvp_data['ARENA_BRACKET_3v3']['seasonWon']*100 / self.pvp_data['ARENA_BRACKET_3v3']['seasonPlayed'], 2)

		return win_perc


	"""

	   Returns"""
	def get_rbg_stats(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		return self.pvp_data['ARENA_BRACKET_RBG']


	"""

	   Returns"""
	def get_rbg_rating(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		return self.pvp_data['ARENA_BRACKET_RBG']['rating']


	"""."""
	def get_rbg_winrate(self):
		if not self.pvp_data:
			pvp_data = self.get_pvp_data()

		if self.pvp_data['ARENA_BRACKET_RBG']['seasonPlayed'] == 0:
			return None

		win_perc = round(self.pvp_data['ARENA_BRACKET_RBG']['seasonWon']*100 / self.pvp_data['ARENA_BRACKET_RBG']['seasonPlayed'], 2)

		return win_perc



### Retrieving the character's reputations data. ###

	"""."""
	def get_reputation_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("reputation")) as url:
				self.rep_data = json.loads(url.read().decode())['reputation']

			return self.rep_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data]


	"""."""
	def get_reputation_amount(self, faction_name):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		if faction_name not in [rep['name'] for rep in self.rep_data]:
			raise ValueError(self.characterName + " has no reputation with that faction.")

		return next((rep['value'] for rep in self.rep_data if rep['name'].lower() == faction_name.lower()), None)


	"""."""
	def get_reputation_level(self, faction_name):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		if faction_name not in [rep['name'] for rep in self.rep_data]:
			raise ValueError(self.characterName + " has no reputation with that faction.")

		rep_standing_map = {'7': 'Exalted', '6': 'Revered', '5': 'Honored', '4': 'Friendly', '3': 'Neutral',
			'2': 'Unfriendly', '1': 'Hostile', '0': 'Hated'}

		standing = next((rep['standing'] for rep in self.rep_data if rep['name'].lower() == faction_name.lower()), None)	

		return rep_standing_map[str(standing)]


	"""."""
	def get_exalted_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 7]


	"""."""
	def get_revered_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 6]


	"""."""
	def get_honored_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 5]


	"""."""
	def get_friendly_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 4]


	"""."""
	def get_neutral_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 3]


	"""."""
	def get_unfriendly_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 2]


	"""."""
	def get_hostile_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 1]


	"""."""
	def get_hated_reputations(self):
		if not self.rep_data:
			rep_data = self.get_reputation_data()

		return [rep['name'] for rep in self.rep_data if rep['standing'] == 0]


### Retrieving the character's quests data. ###

	"""."""
	def get_quests_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("quests")) as url:
				self.quests_data = json.loads(url.read().decode())['quests']

			return self.quests_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def has_completed_quest(self, quest_id):
		if not self.quests_data:
			quests_data = self.get_quests_data

		if quest_id in self.quests_data:
			return True

		else:
			return False


### Retrieving the character's gameplay statistics (most used X, least used Y, etc.). ###

	"""."""
	def get_statistics_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("statistics")) as url:
				self.statistics_data = json.loads(url.read().decode())['statistics']

			return self.statistics_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving the character's in-game stats (Str, Int, Agi, etc.). ###

	"""."""
	def get_stats_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("stats")) as url:
				self.stats_data = json.loads(url.read().decode())['stats']

			return self.stats_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving the character's talents. ###

	"""."""
	def get_talents_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("talents")) as url:
				self.talents_data = json.loads(url.read().decode())['talents']

			return self.talents_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_talents_by_spec(self, spec):
		if not self.character_data:
			character_data = self.get_character_data()

		if not self.talents_data:
			talents_data = self.get_talents_data()

		if spec.lower() not in class_to_spec[int_to_class[str(character_data['class'])]]:
			raise ValueError("This character's class does not have that spec.")
			return

		return [talents['talents']['spell']['name'] for talents in self.talents_data if talents['talents']['spec']['name'].lower() == spec.lower()]


	"""."""
	def get_tier_talents(self, tier, spec):
		if not self.talents_data:
			talents_data = self.get_talents_data()

		if spec.lower() not in class_to_spec[self.get_class()]:
			raise ValueError(self.characterName + "'s class does not have that spec.")
			return

		if tier not in [1, 2, 3, 4, 5, 6, 7]:
			raise ValueError("Please select a valid talent tier (1-7).")
			return

		spec_talents = next((talents for talents in self.talents_data if talents['talents'][0]['spec']['name'].lower() == spec.lower()), None)['talents']

		tier_talent = next((talent['spell']['name'] for talent in spec_talents if talent['tier'] == tier-1), None)

		return tier_talent


### Retrieving the character's titles data. ###

	"""."""
	def get_titles_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("titles")) as url:
				self.titles_data = json.loads(url.read().decode())['titles']

			return self.titles_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_titles(self):
		if not self.titles_data:
			titles_data = self.get_titles_data()

		return [title['name'] for title in self.titles_data]


	"""."""
	def num_titles(self):
		if not self.titles_data:
			titles_data = self.get_titles_data()

		return len([title['name'] for title in self.titles_data])	


