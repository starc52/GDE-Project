# chest.py

from pygame import *
from random import choice, randint


class Chest:
	""" Handles treasure chest actions """
	
	def __init__(self, screen, treasure, message, maps, player, fight, sound, fade):
		self.screen = screen
		self.treasure = treasure
		self.message = message
		self.maps = maps
		self.player = player
		self.fight = fight
		self.sound = sound
		self.fade = fade
		self.chest = image.load("resources/graphics/items/chest.png")
		self.openChest = image.load("resources/graphics/items/chest-opened.png")
		# Possible random prizes (basic)
		self.prizes = ["money", "health", "enemy"]

	def render(self, pRect):
		""" Renders treasure chest """

		def pause(length):
			""" Pauses screen """
			display.flip()
			time.wait(length)

		def drawChests():
			""" To fix flashing chest bug """
			for key,val in self.allChests.items():
				# Draw chests based on current screen
				if key == self.maps.sceneName:
					for i in range(len(self.allChests[key])):
						coords = self.allChests[key][i][0]
						# Add the map coordinates only if the map is scrolling
						if self.allChests[key][i][3]:
							self.screen.blit(self.chest, (coords[0]+self.player.mapx, coords[1]+self.player.mapy))
						else:
							self.screen.blit(self.chest, coords)

		# Blit the opened or closed chest at specified positions
		for key,val in self.allChests.items():
			# Handle collision based on current screen
			if key == self.maps.sceneName:
				for i in range(len(self.allChests[key])):
					# Chest coordinattes
					coords = self.allChests[key][i][0]
					# Blit opened or closed chest

					# Draw the opened or closed treasure chest
					if self.allChests[key][i][1]:
						# Add the map coordinates if the map is scrolling
						if self.allChests[key][i][3]:
							self.screen.blit(self.openChest, (coords[0]+self.player.mapx, coords[1]+self.player.mapy))
						else:
							self.screen.blit(self.openChest, coords)
					else:
						# Add the map coordinates if the map is scrolling
						if self.allChests[key][i][3]:
							self.screen.blit(self.chest, (coords[0]+self.player.mapx, coords[1]+self.player.mapy))
						else:
							self.screen.blit(self.chest, coords)

						# Set the chest rect coordinates if the map is scrolling
						if self.allChests[key][i][3]:
							x = coords[0]+self.player.mapx
							y = coords[1]+self.player.mapy
						else:
							x = coords[0]
							y = coords[1]

						# Set chest state to opened
						if pRect.colliderect(Rect(x,y,32,32)):
							self.allChests[key][i][1] = True
							# Random prize
							prize = self.allChests[key][i][2]
							# Award prizes
							if prize == "money":
								reward = randint(10,30)
								drawChests()
								self.player.render()
								self.treasure.render(self.screen, True, False, False, self.message)
								self.message.botMessage("You have been rewarded with %s coins!"%str(reward), False)
								#self.sound.play("coinCollected")
								self.treasure.money += reward
								pause(1300)
							elif prize == "full health":
								drawChests()
								self.player.render()
								self.treasure.render(self.screen, True, False, False, self.message)
								self.message.botMessage("Your health has been restored.", False)
								#self.sound.play("coinCollected")
								self.treasure.health = 100
								pause(1300)
							elif prize == "fire gem":
								drawChests()
								self.player.render()
								self.treasure.render(self.screen, True, False, False, self.message)
								self.message.botMessage("You have obtained the fire gem!", False)
								self.treasure.gems["fire"] = True
								pause(1300)	
							elif prize == "health":
								reward = randint(10,20)
								drawChests()
								self.player.render()
								self.treasure.render(self.screen, True, False, False, self.message)
								self.message.botMessage("You have been rewarded with %s health!"%str(reward), False)
								self.treasure.health = min(100, self.treasure.health+reward)
								pause(1300)
							elif prize == "flameSword":
								drawChests()
								self.player.render()
								self.treasure.collectedItems.add("flameSword")
								self.treasure.render(self.screen, True, False, False, self.message)
								self.message.topMessage("You have been rewarded with the flame Sword!", False)
								pause(1300)
							else:
								# Call random fight
								self.fight.start()
