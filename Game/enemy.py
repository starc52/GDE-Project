

from pygame import *
from random import choice


class Enemy(object):
	""" Enemy class """
	
	def __init__(self):
		# All enemies
		self.enemies = ["Zombie"]
		self.waterEnemies = ["a Swarly", "a Tentacruel", "Zombie"]
		# Enemy data -> (sprites, position, attack power possibilities, location of health bar)
		self.enemyData = {
			"Zombie" : [[transform.scale2x(image.load("resources/graphics/enemies/Skeleton Dancer/%s.png"%str(i)).convert_alpha()) for i in range(3)],
								(141,244), [2,2,2,3,3,2], (151,202)]
		}
		#0-4 in attack is for attack, 5-9 is for appear, 10-12 is to walk.
		self.waterEnemyData = {
			"Zombie" : [[transform.scale2x(image.load("resources/graphics/enemies/Skeleton Dancer/%s.png"%str(i)).convert_alpha()) for i in range(3)],
								(141,244), [2,2,2,3,3,2], (151,202)]
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
