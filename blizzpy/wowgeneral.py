##########################################################################
# A wrapper for general game data, such as quest, zones, and bosses, in  #
# Blizzard's WoW Community API.                                          #
# Part of BlizzPy.                                                       #
#                                                                        #
# Written by Lewis Kim.                                                  #
##########################################################################

import requests
import urllib, json
import pandas as pd



class WoWGeneral:

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






### Retrieving game achievements data. ###





### Retrieving game boss data. ###







### Retrieving game item data. ###







### Retrieving game mount data. ###




### Retrieving game quest data. ###





### Retrieving game recipe data. ###




### Retrieving game spell data. ###





### Retrieving game zone data. ###



