# enemy.py
# Paul Krishnamurthy 2015
# Enemy class

# The Third Element
# ICS3U Final Project

from pygame import *
from random import choice


class Enemy(object):
	""" Enemy class """
	
	def __init__(self):
		# All enemies
		self.enemies = ["Zombie"]
		self.waterEnemies = ["a Swarly", "a Tentacruel"]
		# Enemy data -> (sprites, position, attack power possibilities, location of health bar)
		self.enemyData = {
			"Zombie" : [[transform.scale2x(image.load("resources/graphics/enemies/Skeleton Dancer/%s.png"%str(i)).convert_alpha()) for i in range(3)],
								(141,244), [2,2,2,3,3,2], (151,202)]
		}
		self.waterEnemyData = {
			"a Swarly" : [[transform.scale2x(transform.scale2x(image.load("resources/graphics/enemies/Swarly/%s.png"%str(i)).convert_alpha())) for i in range(6)],
									(191,252), [2,2,2,3,3], (188,206)],
			"a Tentacruel" : [[transform.scale2x(transform.scale2x(image.load("resources/graphics/enemies/Tentacruel/%s.png"%str(i)).convert_alpha())) for i in range(10)],
								(155,204), [4,3,3,4,4,5], (164,163)]
		}
		# Other individual enemies (name, sprites, position, location of health bar, total health)
		self.broth = ["Broth", [transform.scale2x(image.load("resources/graphics/enemies/Broth/%s.png"%str(i)).convert_alpha()) for i in range(7)],
						(125,194), (132,161), 50, 20]
		# Dictionary to reference custom enemies
		self.customEnemies = {
			"broth" : self.broth
		}

	def randomEnemy(self, area, custom=None):
		""" Returns random enemy based on location"""
		# Return list if custom enemy is requested
		enemy = self.enemies[0]
		return [enemy, self.enemyData[enemy][1], choice(self.enemyData[enemy][2]), self.enemyData[enemy][3]]
