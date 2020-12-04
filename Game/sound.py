
from pygame import *
from Game.const import *

class Sound(object):
	""" Play sound effects """

	def __init__(self):
		# All sound effects

		if not mac:
			# self.coinCollected = mixer.Sound("resources/sound/coinCollected.wav")

			# I was going to use dictionaries but it was too slow...

			self.themes = {
				"mainWorldFight" : "resources/sound/mainWorldFight.ogg",
				"mainWorldTheme" : "resources/sound/travel1.ogg",
				"waterWorldTheme" : "resources/sound/travel1.ogg",
				"ship" : "resources/sound/theme1.ogg",
				# "shopTheme" : "resources/sound/shop.ogg",
				# "fireWorldTheme" : "resources/sound/fireWorld.ogg",
				"conclusion" : "resources/sound/conclusion.ogg",
				"introTheme" : "resources/sound/introTheme.ogg",
				"BurntHouseTheme" : "resources/sound/mystery1.ogg",
				"hideoutTheme" : "resources/sound/mystery2.ogg",
				"finalIslandTheme" : "resources/sound/mystery3.ogg",
				"zombieTheme" : "resources/sound/zombie-17.ogg",
				"gunshotTheme" : "resources/sound/SHOOT025.ogg"
				# "churchTheme" : "resources/sound/church.ogg",
				# "castleTheme" : "resources/sound/castle.ogg",
				# "finalTempleTheme" : "resources/sound/temple.ogg"
			}

			# # Key -> scenename | value -> theme name
			# self.sceneData = {
			# 	"mainWorld" : "mainWorldTheme",
			# 	"mainWorldShop" : "shopTheme",
			# 	"waterWorldEnter" : "waterWorldTheme",
			# 	"waterWorld" : "waterWorldTheme",
			# 	"waterWorldRoom1" : "waterWorldTheme",
			# 	"waterWorldRoom2" : "waterWorldTheme",
			# 	"waterWorldRoom3" : "waterWorldTheme",
			# 	"waterWorldRoom4" : "waterWorldTheme",
			# 	"fireWorldEnter" : "fireWorldTheme",
			# 	"fireWorld" : "fireWorldTheme",
			# 	"fireWorldRoom1" : "fireWorldTheme",
			# 	"fireWorldRoom2" : "fireWorldTheme",
			# 	"church" : "churchTheme",
			# 	"ultimateShop" : "shopTheme",
			# 	"surpriseTemple" : "castleTheme",
			# 	"finalTemple" : "finalTempleTheme"
			# }

			# Set sound and theme volumes
			#self.coinCollected.set_volume(.8)
			mixer.music.set_volume(.6)

	def getMusic(self, sound):
		""" Return music themes """
		return self.themes[sound]

	def stopSound(self, sound):
		""" Stops specific sound """
		self.sounds[sound].fadeout(500)

	def stopMusic(self):
		""" Stop mixer """
		mixer.music.fadeout(500)

	# def setVolume(self, amount):
	# 	""" Set volume """
	# 	mixer.music.set_volume(amount)