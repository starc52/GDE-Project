
from pygame import *
from Game.const import *

class Sound(object):
	""" Play sound effects """

	def __init__(self):
		# All sound effects

		if not mac:
			
			self.themes = {
				"mainWorldFight" : "resources/sound/mainWorldFight.ogg",
				"mainWorldTheme" : "resources/sound/travel1.ogg",
				"waterWorldTheme" : "resources/sound/travel1.ogg",
				"ship" : "resources/sound/theme1.ogg",
				"conclusion" : "resources/sound/conclusion.ogg",
				"introTheme" : "resources/sound/introTheme.ogg",
				"BurntHouseTheme" : "resources/sound/mystery1.ogg",
				"hideoutTheme" : "resources/sound/mystery2.ogg",
				"finalIslandTheme" : "resources/sound/mystery3.ogg"
			}
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

