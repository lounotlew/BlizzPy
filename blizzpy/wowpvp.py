########################################################################
# A wrapper for the PvP Leaderboards in Blizzard's WoW Community API.  #
# Part of BlizzPy.                                                     #
# NYI due to API issues (see below.)                                   #
#                                                                      #
# Written by Lewis Kim.                                                #
########################################################################

import requests
import urllib, json
import pandas as pd


class WoWPVP:

	"""

	   Currently not implemented due to the Blizzard API returning an empty dataset upon requests."""
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

