#############################################################
# A wrapper for the ladder data in the SC2 Community API.   #
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

