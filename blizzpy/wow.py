###############################################
# A wrapper for the WoW Community API.        #
# WoWChar: WoW Character Data.                #
# WoWGuild: WoW Guild Data.                   #
# WoWAuction: WoW Auction Snapshot Data.      #
# WoWPets: WoW Non-hunter Pet Data.           #
# WoWPVP: WoW PVP Leaderboard Data (NYI).     #
# WoWGeneral: WoW General Game Data.          #
# Part of BlizzPy.                            #
#                                             #
# Written by Lewis Kim.                       #
###############################################

import requests
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

		# Basic attributes for request URLs.
		self.api_key = api_key
		self.locale = locale

		self.characterName = characterName
		self.realm = realm

		# Initially empty datasets for the API data.
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

		self.feed_data = []
		self.raid_prog_data = []
		self.quests_data = []
		self.rep_data = []
		self.talents_data = []
		self.titles_data = []


	"""Returns the request URL that fetches the .json data from the Blizzard API."""
	def _get_data_url(self):
		url = "{root}/wow/character/{realm}/{characterName}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			characterName = self.characterName,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""Returns the request URL with a field that fetches the .json data from the Blizzard API."""
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
	def get_achievement_points(self):
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

	   Keys: 
	   achievementsCompleted, achievementsCompletedTimestamp, criteria, criteriaQuantity,
	   criteriaTimestamp, criteriaCreated"""
	def get_achievements_data(self):
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
			return df.sort_values('achievementsCompletedTimestamp')

		else:
			return df

	
	"""."""
	def has_achievement(self, achievement_id):
		return


### Retrieving the character's appearance data. ###

	"""Return self.characterName's appearance data as a dictionary, decoded from json.
	   Appearance refers to character features, such as face/haircolor, not transmog.

	   Keys: skinColor, hairVariation, hairColor, featureVariation, showHelm, showCloak, 
	         customDisplayOptions"""
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
	def get_hair_color(self):
		if not self.appearance_data:
			appearance_data = self.get_appearance_data()

		return self.appearance_data['hairColor']


### Retrieving the character's feed (activity) data. ###

	"""Return Return self.characterName's activity data as a dictionary, decoded from json."""
	def get_feed_data(self, as_df=False):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("feed")) as url:
				self.feed_data = json.loads(url.read().decode())['feed']

			return self.feed_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving the character's guild data. ###

	"""Return self.characterName's guild data as a dictionary, decoded from json."""
	def get_guild_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("guild")) as url:
				self.guild_data = json.loads(url.read().decode())['guild']

			return self.guild_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return

	
	"""Return the name of the guild self.characterName is a part of."""
	def get_guild_name(self):
		if not self.guild_data:
			guild_data = self.get_appearance_data()

		return self.guild_data['name']


	"""Return the number of members in the guild self.characterName is a part of."""
	def get_num_guild_members(self):
		if not self.guild_data:
			guild_data = self.get_appearance_data()

		return self.guild_data['members']


	"""Return the number of achievements the guild self.characterName is a part of has."""
	def get_guild_achievement_points(self):
		if not self.guild_data:
			guild_data = self.get_appearance_data()

		return self.guild_data['achievementPoints']


### Retrieving the character's hunter pet data, given that the character is a hunter. ###

	"""Return self.characterName's hunter pets data, decoded from json.

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

	"""Return self.characterName's items data, decoded from json."""
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


	"""Returns a dictionary containing information about the gear in SLOT_NAME."""
	def get_gear_piece(self, slot_name):
		if not self.items_data:
			items_data = self.get_items_data()

		if slot_name not in list(self.items_data.keys())[2:]:
			return None

		return self.items_data[slot_name]


### Retrieving the character's mounts data. ###

	"""Return self.characterName's mounts data, decoded from json."""
	def get_mounts_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("mounts")) as url:
				self.mounts_data = json.loads(url.read().decode())['mounts']

			return self.mounts_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Returns a dictionary containing information about the selected mount MOUNT_NAME."""
	def search_mount(self, mount_name):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		for mount in all_mounts:
			if mount['name'] == mount_name:
				return mount

		return None


	"""Returns a list of the character's mounts' names."""
	def get_mount_names(self):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		return [mount['name'] for mount in all_mounts]


	"""Returns a list of the character's ground mounts' names. Can intersect with flying mounts."""
	def get_ground_mounts(self):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		return [mount for mount in all_mounts if mount['isGround'] == True]


	"""Returns a list of the character's flying mounts' names. Can intersect with ground mounts."""
	def get_flying_mounts(self):
		if not self.mounts_data:
			mounts_data = self.get_mounts_data()

		all_mounts = self.mounts_data['collected']

		return [mount for mount in all_mounts if mount['isFlying'] == True]


### Retrieving the character's non-hunter pets data. ###

	"""Return self.characterName's non-hunter pets data, decoded from json."""
	def get_pets_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("pets")) as url:
				self.pets_data = json.loads(url.read().decode())['pets']

			return self.pets_data

			return 

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Returns the number of non-hunter pets the selected character owns."""
	def get_num_pets(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		return self.pets_data['numCollected']


	"""Returns the percentage of all pets owned."""
	def get_percent_collected(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		perc = round(100*self.pets_data['numCollected']/(self.pets_data['numCollected'] + self.pets_data['numNotCollected']), 2)

		return perc


	"""Returns a list of the names of the owned pets."""
	def get_pet_names(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()
		return [pet['name'] for pet in self.pets_data['collected']]


	"""Returns a list of the creatureIDs of the owned pets."""
	def get_pet_ids(self):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		return [pet['creatureID'] for pet in self.pets_data['collected']]


	"""Returns a list of the favorited pets' names if as_names=True. Else, returns a
	   list of dictionaries containing information about favorited pets."""
	def get_favorite_pets(self, as_names=True):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		if as_names:
			favorite_pets = [pet['name'] for pet in self.pets_data['collected'] if pet['isFavorite']]

		else:
			favorite_pets = [pet for pet in self.pets_data['collected'] if pet['isFavorite']]

		return favorite_pets		


	"""Returns the pet quality integer of PET_NAME."""
	def get_pet_quality(self, pet_name):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		quality = next((pet['stats']['petQualityId'] for pet in self.pets_data['collected'] if pet['name'].lower() == pet_name.lower()), None)

		return quality
		

	"""Returns a dictionary containing stats information about PET_NAME."""
	def get_pet_stats(self, pet_name):
		if not self.pets_data:
			pets_data = self.get_pets_data()

		stats = next((pet['stats'] for pet in self.pets_data['collected'] if pet['name'].lower() == pet_name.lower()), None)

		return stats


### Retrieving the character's professions data. ###

	"""Return self.characterName's professions data, decoded from json."""
	def get_professions_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("professions")) as url:
				self.professions_data = json.loads(url.read().decode())['professions']

			return self.professions_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Returns a dictionary whose keys are the character's primary profession names,
	   and values are the ranks associated with that profession."""
	def get_primary_professions(self):
		if not self.professions_data:
			professions_data = self.professions_data

		primary_profs = professions['primary']

		if len(primary_profs) == 0:
			return None

		return {prof['name']: prof['rank'] for prof in primary_profs}


	"""Returns a dictionary whose keys are the character's secondary profession names,
	   and values are the ranks associated with that profession."""
	def get_secondary_professions(self):
		if not self.professions_data:
			professions_data = self.professions_data

		secondary_profs = professions['secondary']

		if len(secondary_profs) == 0:
			return None

		return {prof['name']: prof['rank'] for prof in secondary_profs}


### Retrieving the character's raid progression data. ###

	"""Return self.characterName's raid progression data, decoded from json."""
	def get_raid_prog_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("progression")) as url:
				raid_prog_data = json.loads(url.read().decode())['progression']

			self.raid_prog_data = raid_prog_data['raids']

			return self.raid_prog_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Returns a dictionary that contains progression information about the selected raid with RAID_NAME.

	   Keys: name, lfr, normal, heroic, mythic, id, bosses"""
	def get_raid_prog(self, raid_name):
		if not self.raid_prog_data:
			raid_prog_data = self.get_raid_prog_data()

		if raid_name.lower() not in [raid['name'].lower() for raid in self.raid_prog_data]:
			raise ValueError("That raid does not exist. Please check its spelling. Upper/lowercase does not matter.")
			return

		raid = next((raid for raid in self.raid_prog_data if raid['name'].lower() == raid_name.lower()), None)

		return raid


	"""Returns an int of the number of BOSS_NAME kills in RAID_NAME on DIFFICULTY..

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


	"""Returns an int of the timetamp of the first selected BOSS_NAME kill in that RAID on that DIFFICULTY.

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

	"""Return self.characterName's PVP data, decoded from json."""
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

	"""Return self.characterName's reputations data, decoded from json."""
	def get_reputation_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("reputation")) as url:
				self.rep_data = json.loads(url.read().decode())['reputation']

			return self.rep_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def get_reputation_factions(self):
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

	"""Return self.characterName's quests data, decoded from json."""
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

	"""Return self.characterName's gameplay statistics data, decoded from json."""
	def get_statistics_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("statistics")) as url:
				self.statistics_data = json.loads(url.read().decode())['statistics']

			return self.statistics_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving the character's in-game stats (Str, Int, Agi, etc.). ###

	"""Return self.characterName's in-game stats data, decoded from json."""
	def get_stats_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("stats")) as url:
				self.stats_data = json.loads(url.read().decode())['stats']

			return self.stats_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


### Retrieving the character's talents. ###

	"""Return self.characterName's talents data, decoded from json."""
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

		if spec.lower() not in class_to_spec[int_to_class[str(self.character_data['class'])]]:
			raise ValueError("This character's class does not have that spec.")
			return

		spec_talents = next((talents for talents in self.talents_data if talents['talents'][0]['spec']['name'].lower() == spec.lower()), None)['talents']

		return {talent['tier']+1:talent['spell']['name'] for talent in spec_talents}


	# """."""
	# def get_tier_talents(self, tier, spec):
	# 	if not self.talents_data:
	# 		talents_data = self.get_talents_data()

	# 	if spec.lower() not in class_to_spec[self.get_class()]:
	# 		raise ValueError(self.characterName + "'s class does not have that spec.")
	# 		return

	# 	if tier not in [1, 2, 3, 4, 5, 6, 7]:
	# 		raise ValueError("Please select a valid talent tier (1-7).")
	# 		return

	# 	spec_talents = next((talents for talents in self.talents_data if talents['talents'][0]['spec']['name'].lower() == spec.lower()), None)['talents']

	# 	tier_talent = next((talent['spell']['name'] for talent in spec_talents if talent['tier'] == tier-1), None)

	# 	return tier_talent


### Retrieving the character's titles data. ###

	"""Return self.characterName's titles data, decoded from json."""
	def get_titles_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("titles")) as url:
				self.titles_data = json.loads(url.read().decode())['titles']

			return self.titles_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""Returns a list of str of title names the selected character owns."""
	def get_title_names(self):
		if not self.titles_data:
			titles_data = self.get_titles_data()

		return [title['name'] for title in self.titles_data]


	"""Returns an int of the number of titles the character owns."""
	def num_titles(self):
		if not self.titles_data:
			titles_data = self.get_titles_data()

		return len([title['name'] for title in self.titles_data])


#
class WoWGuild:

	""".

	   PARAMS:
	   self.root: String root URL.
	   self.api_key: Your API key (String).
	   self.locale: String locale of the region.
	   self.guild_name: String name of the guild to be searched.
	   self.realm: String name of the realm the guild is on. """
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


	# The following are API request functions. Returns the URL that contains the JSON data fetched
	# from Blizzard's API.


	def _api_request(self, endpoint):
		return


	def _get_data_url(self):
		url = "{root}/wow/guild/{realm}/{guild_name}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm.realm.replace(" ", "%20"),
			guild_name = self.guild_name.replace(" ", "%20"),
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	def _get_data_with_field_url(self, field):
		url = "{root}/wow/guild/{realm}/{guild_name}?fields={field}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm.replace(" ", "%20"),
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
	def get_achievements_data(self):
		try:
			with urllib.request.urlopen(self._get_data_with_field_url("achievements")) as url:
				self.ach_data = json.loads(url.read().decode())['achievements']

			return self.ach_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key, character name, or realm name.")
			return


	"""."""
	def has_achievement(self, achievement_id):
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


#
class WoWAuction:


	def __init__(self, api_key, realm, locale="en_US", token=None):
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

		self.realm = realm
		self.api_key = api_key
		self.locale = locale

		self.last_modified = 0
		self.auction_data = []


	"""."""
	def _get_auction_data_url(self):
		url = "{root}/wow/auction/data/{realm}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			realm = self.realm,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving WoW auction house patch data. ###

	"""."""
	def get_auction_data(self):
		try:
			with urllib.request.urlopen(self._get_auction_data_url()) as url1:
				raw_data = json.loads(url1.read().decode())
				self.last_modified = raw_data['files'][0]['lastModified']

			with urllib.request.urlopen(raw_data['files'][0]['url']) as url2:
				self.auction_data = json.loads(url2.read().decode())['auctions']

			return self.auction_data
		except:
			raise ValueError("Could not retrieve data. Please check your API key or realm.")
			return


	"""."""
	def get_last_modified(self):
		if not self.last_modified:
			auction_data = self.get_auction_data()

		return self.last_modified


	"""."""
	def get_buyout_prices(self, item_id, in_gold=False):
		if not self.auction_data:
			auction_data = self.get_auction_data()

		if in_gold:
			return {round(auction['buyout']/10000, 4):auction['quantity'] for auction in self.auction_data if auction['item'] == item_id}

		else:
			return {auction['buyout']:auction['quantity'] for auction in self.auction_data if auction['item'] == item_id}


	"""."""
	def get_auctions_by_player(self, player_name):
		if not self.auction_data:
			auction_data = self.get_auction_data()

		return [auction for auction in self.auction_data if auction['owner'] == player_name]


#
class WoWPets:

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

		self.master_data = []

		self.ability_data = {}
		self.species_data = {}
		self.stats_data = {}


	"""."""
	def _get_master_data_url(self):
		url = "{root}/wow/pet/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url

	"""."""
	def _get_ability_data_url(self, abilityId):
		url = "{root}/wow/pet/ability/{abilityId}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			abilityId = abilityId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_species_data_url(self, speciesId):
		url = "{root}/wow/pet/species/{speciesId}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			speciesId = speciesId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	"""."""
	def _get_stats_data_url(self, speciesId, level, breedId, qualityId):
		url = "{root}/wow/pet/stats/{speciesId}?level={level}&breedId={breedId}&qualityId={qualityId}&locale={locale}&apikey={api_key}".format(
			root = self.root,
			speciesId = speciesId,
			level = level,
			breedId = breedId,
			qualityId = qualityId,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving the pets master list. ###

	"""."""
	def get_master_list(self):
		try:
			with urllib.request.urlopen(self._get_master_data_url()) as url:
				self.master_data = json.loads(url.read().decode())['pets']

			return self.master_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key.")
			return


	"""."""
	def search_pet(self, pet_param):
		if not self.master_data:
			master_data = self.get_master_list()

		if type(pet_param) == str:
			return next((pet for pet in self.master_data if pet['name'] == pet_param), None)

		elif type(pet_param) == int:
			return next((pet for pet in self.master_data if pet['creatureId'] == pet_param), None)

		else:
			raise ValueError("Invalid parameters. PET_PARAM must be a string (pet name), or an integer (creature ID).")
			return


	"""."""
	def get_nameToID_dict(self):
		if not self.master_data:
			master_data = self.get_master_list()

		return {pet['name']: pet['creatureId'] for pet in self.master_data}


	"""."""
	def get_battle_pets(self, as_names=False):
		if not self.master_data:
			master_data = self.get_master_list()

		if as_names:
			return [pet['name'] for pet in self.master_data if pet['canBattle']]

		else:
			return [pet for pet in self.master_data if pet['canBattle']]


	"""."""
	def get_nonbattle_pets(self, as_names=False):
		if not self.master_data:
			master_data = self.get_master_list()

		if as_names:
			return [pet['name'] for pet in self.master_data if not pet['canBattle']]

		else:
			return [pet for pet in self.master_data if not pet['canBattle']]


	"""."""
	def get_pet_stats(self, pet_param):
		if not self.master_data:
			master_data = self.get_master_list()

		if type(pet_param) == str:
			return next((pet['stats'] for pet in self.master_data if pet['name'] == pet_param), None)

		elif type(pet_param) == int:
			return next((pet['stats'] for pet in self.master_data if pet['creatureId'] == pet_param), None)

		else:
			raise ValueError("Invalid parameters. Param PET must be a string (pet name), or an integer (creature ID).")
			return


### Retrieving pet abilities data. ###
	
	"""."""
	def get_ability_data(self, abilityId):
		try:
			with urllib.request.urlopen(self._get_ability_data_url(abilityId)) as url:
				self.ability_data = json.loads(url.read().decode())

			return self.ability_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or ability ID.")
			return


### Retrieving pet species data. ###

	"""."""
	def get_species_data(self, speciesId):
		try:
			with urllib.request.urlopen(self._get_species_data_url(speciesId)) as url:
				self.species_data = json.loads(url.read().decode())

			return self.species_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or ability ID.")
			return


### Retrieving species stat data. ###

	"""."""
	def get_species_stats_data(self, speciesId, level=1, breedId=3, qualityId=1):
		try:
			with urllib.request.urlopen(self._get_stats_data_url(speciesId, level, breedId, qualityId)) as url:
				self.ability_data = json.loads(url.read().decode())

			return self.ability_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or ability ID.")
			return


#
class WoWPVP:

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

		self.pvp_2v2_data = {}
		self.pvp_3v3_data = {}
		self.pvp_rbg_data = {}


	""".

	   https://us.api.battle.net/wow/leaderboard/2v2?locale=en_US&apikey=..."""
	def _get_pvp_data_url(self, bracket):
		url = "{root}/wow/leaderboard/{bracket}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			bracket = bracket,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving 2v2 arena data. ###

	"""."""
	def get_2v2_data(self):
		try:
			with urllib.request.urlopen(self._get_pvp_data_url("2v2")) as url:
				self.pvp_2v2_data = json.loads(url.read().decode())

			return self.pvp_2v2_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Achievement ID.")
			return


	"""."""
	def search_2v2_player(self, player_name):
		if not self.pvp_2v2_data:
			self.get_2v2_data()

		return next((player for player in self.pvp_2v2_data['rows'] if player['name'] == player_name), None)


	"""."""
	def search_2v2_players_by_rank(self, rank, as_names=False):
		if not self.pvp_2v2_data:
			self.get_2v2_data()

		if as_names:
			return [player['name'] for player in self.pvp_2v2_data['rows'] if player['ranking'] == rank]

		else:
			return [player for player in self.pvp_2v2_data['rows'] if player['ranking'] == rank]


### Retrieving 3v3 arena data. ###

	"""."""
	def get_3v3_data(self):
		try:
			with urllib.request.urlopen(self._get_pvp_data_url("3v3")) as url:
				self.pvp_3v3_data = json.loads(url.read().decode())

			return self.pvp_3v3_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Achievement ID.")
			return


	"""."""
	def search_3v3_player(self, player_name):
		if not self.pvp_2v2_data:
			self.get_2v2_data()

		return next((player for player in self.pvp_3v3_data['rows'] if player['name'] == player_name), None)


	"""."""
	def search_3v3_player_by_rank(self, rank):
		if not self.pvp_2v2_data:
			self.get_2v2_data()

		return [player for player in self.pvp_3v3_data['rows'] if player['ranking'] == rank]


	"""."""


### Retrieving RBG data. ###

	"""."""
	def get_rbg_data(self):
		try:
			with urllib.request.urlopen(self._get_pvp_data_url("rbg")) as url:
				self.pvp_rbg_data = json.loads(url.read().decode())

			return self.pvp_rbg_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Achievement ID.")
			return


	"""."""
	def search_rbg_player(self, player_name):
		if not self.pvp_2v2_data:
			self.get_2v2_data()

		return next((player for player in self.pvp_rbg_data['rows'] if player['name'] == player_name), None)


	"""."""
	def search_rbg_player_by_rank(self, rank):
		if not self.pvp_2v2_data:
			self.get_2v2_data()

		return [player for player in self.pvp_rbg_data['rows'] if player['ranking'] == rank]


#
class WoWResources:

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


	"""

	   e.g. https://us.api.battle.net/wow/achievement/2144?locale=en_US&apikey=..."""
	def _get_achievement_data_url(self, achievement_id):
		url = "{root}/wow/achievement/{achievement_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			achievement_id = achievement_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/boss/?locale=en_US&apikey=..."""
	def _get_boss_master_url(self):
		url = "{root}/wow/boss/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/boss/24723?locale=en_US&apikey=..."""
	def _get_boss_data_url(self, boss_id):
		url = "{root}/wow/boss/{boss_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			boss_id = boss_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/item/18803?locale=en_US&apikey=..."""
	def _get_item_data_url(self, item_id):
		url = "{root}/wow/item/{item_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			item_id = item_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/item/set/1060?locale=en_US&apikey=..."""
	def _get_item_set_data_url(self, set_id):
		url = "{root}/wow/item/set/{set_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			set_id = set_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/mount/?locale=en_US&apikey=..."""
	def _get_mount_master_url(self):
		url = "{root}/wow/mount/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/quest/13146?locale=en_US&apikey=..."""
	def _get_quest_data_url(self, quest_id):
		url = "{root}/wow/quest/{quest_id}/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			quest_id = quest_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/realm/status?locale=en_US&apikey=..."""
	def _get_realms_data_url(self):
		url = "{root}/wow/realm/status?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/recipe/33994?locale=en_US&apikey=..."""
	def _get_recipe_data_url(self, recipe_id):
		url = "{root}/wow/recipe/{recipe_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			recipe_id = recipe_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/spell/260997?locale=en_US&apikey=..."""
	def _get_spell_data_url(self, spell_id):
		url = "{root}/wow/spell/{spell_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			spell_id = spell_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/zone/?locale=en_US&apikey=..."""
	def _get_zone_master_url(self):
		url = "{root}/wow/zone/?locale={locale}&apikey={api_key}".format(
			root = self.root,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


	""".

	   e.g. https://us.api.battle.net/wow/zone/4131?locale=en_US&apikey=..."""
	def _get_zone_data_url(self, zone_id):
		url = "{root}/wow/zone/{zone_id}?locale={locale}&apikey={api_key}".format(
			root = self.root,
			zone_id = zone_id,
			locale = self.locale,
			api_key = self.api_key
			)

		return url


### Retrieving game achievements data. ###
	
	"""."""
	def get_achievement_data(self, achievement_id):
		try:
			with urllib.request.urlopen(self._get_achievement_data_url(achievement_id)) as url:
				self.achievement_data = json.loads(url.read().decode())

			return self.achievement_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Achievement ID.")
			return


### Retrieving game boss data. ###

	"""."""
	def get_bosses_data(self):
		try:
			with urllib.request.urlopen(self._get_boss_master_url()) as url:
				self.bosses_data = json.loads(url.read().decode())

			return self.bosses_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key.")
			return


	"""."""
	def get_boss_info(self, boss_id):
		try:
			with urllib.request.urlopen(self._get_boss_data_url(boss_id)) as url:
				self.boss_data = json.loads(url.read().decode())

			return self.boss_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game item data. ###

	"""."""
	def get_item_data(self, item_id):
		try:
			with urllib.request.urlopen(self._get_item_data_url(item_id)) as url:
				self.item_data = json.loads(url.read().decode())

			return self.item_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


	"""."""
	def get_item_set_data(self, itemSet_id):
		try:
			with urllib.request.urlopen(self._get_item_set_data_url(set_id)) as url:
				self.item_set_data = json.loads(url.read().decode())

			return self.item_set_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game mount data. ###

	"""."""
	def get_mounts_data(self):
		try:
			with urllib.request.urlopen(self._get_mount_master_url()) as url:
				self.mounts_data = json.loads(url.read().decode())

			return self.mounts_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game quest data. ###

	"""."""
	def get_quest_data(self, quest_id):
		try:
			with urllib.request.urlopen(self._get_quest_data_url(quest_id)) as url:
				self.quest_data = json.loads(url.read().decode())

			return self.quest_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving realm data. ###

	"""."""
	def get_realms_data(self):
		try:
			with urllib.request.urlopen(self._get_realms_data_url()) as url:
				self.realms_data = json.loads(url.read().decode())

			return self.realms_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game recipe data. ###

	"""."""
	def get_recipe_data(self, recipe_id):
		try:
			with urllib.request.urlopen(self._get_recipe_data_url(recipe_id)) as url:
				self.recipe_data = json.loads(url.read().decode())

			return self.recipe_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game spell data. ###

	"""."""
	def get_spell_data(self, spell_id):
		try:
			with urllib.request.urlopen(self._get_spell_data_url(spell_id)) as url:
				self.spell_data = json.loads(url.read().decode())

			return self.spell_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


### Retrieving game zone data. ###

	"""."""
	def get_zones_data(self):
		try:
			with urllib.request.urlopen(self._get_zone_master_url()) as url:
				self.zones_data = json.loads(url.read().decode())

			return self.zones_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return


	"""."""
	def get_zone_info(self, zone_id):
		try:
			with urllib.request.urlopen(self._get_zone_data_url(zone_id)) as url:
				self.zone_data = json.loads(url.read().decode())

			return self.zone_data

		except:
			raise ValueError("Could not retrieve data. Please check your API key or Boss ID.")
			return

