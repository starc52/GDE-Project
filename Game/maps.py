from pygame import *
class Maps:
	""" Main map class """
	
	def __init__(self, screen, player):
		self.screen = screen
		self.player = player
		# Dictionary with map image -> coordinates -> scrolling camera
		self.allScenes = {
			"shipCabin" : [image.load("resources/graphics/map/controlroom.png").convert(), (0,0), False], 
			"shipCorridor" : [image.load("resources/graphics/map/final_corridor.png").convert(), (0,0), False],
			"BurntHouse" : [image.load("resources/graphics/map/burnt_house1.png").convert(), (0,0), False],
			"mainWorld" : [transform.scale2x(image.load("resources/graphics/map/mainWorld.png").convert()), (-534,-1585), True],
			"hideout" : [transform.scale(image.load("resources/graphics/map/hideout.png").convert(),(1086,600)), (0,0), False],
			"dungeon" : [transform.scale(image.load("resources/graphics/map/fun_dungeon.png").convert(),(1086,600)), (0,0), False],
			"Lab" : [transform.scale(image.load("resources/graphics/map/lab1.png").convert(),(1086,600)), (0,0), False],
			"finalisland" : [transform.scale(image.load("resources/graphics/map/surpriseTemple.png").convert(),(1086,600)), (0,0), False], 
			"islandPassword" : [transform.scale(image.load("resources/graphics/map/keypad.jpg").convert(),(1086,600)), (0,0), False]
		}
		# Masks for each scene
		self.allScenesMasks = {
			"shipCabin" : image.load("resources/graphics/map/control_roomblit1.png").convert(), 
			"shipCorridor" : image.load("resources/graphics/map/final_corridorblit.png").convert(),
			"BurntHouse" : image.load("resources/graphics/map/Webp.net-resizeimage.png").convert(),
			"mainWorld" : transform.scale2x(image.load("resources/graphics/map/mainWorldMask.png").convert()),
			"hideout" : transform.scale(image.load("resources/graphics/map/hideout_finalblit.png").convert(),(1086,600)).convert(),
			"dungeon" : transform.scale(image.load("resources/graphics/map/fun_dungeonblit.png").convert(),(1086,600)).convert(),
			"Lab" : transform.scale(image.load("resources/graphics/map/lab1_blit.jpg").convert(),(1086,600)).convert(),
			"finalisland" : transform.scale(image.load("resources/graphics/map/surpriseTempleMask.png").convert(),(1086,600)).convert(),
			"islandPassword": transform.scale(image.load("resources/graphics/map/keypad.jpg").convert(),(1086,600)).convert()
		}

		# Initial World Setup
		self.sceneName = "shipCorridor"
		# Current image
		self.image = self.allScenes[self.sceneName][0]
		# Scrolling camera boolean
		self.scrollingCamera = self.allScenes[self.sceneName][2]
		# Mask image
		self.mask = self.allScenesMasks[self.sceneName]

	def newScene(self, scene):
		""" Set new scene """
		# Set new image and scene
		self.image = self.allScenes[scene][0]
		self.sceneName = scene
		# Flag if map can move
		self.scrollingCamera = self.allScenes[self.sceneName][2]
		# Update collision map
		self.mask = self.allScenesMasks[self.sceneName]

		# Scrolling map
		if self.allScenes[scene][2]:
			self.player.mapx, self.player.mapy = self.player.mapCoords[scene]

	def render(self, screen, x=None, y=None):
		""" Update new scene """

		# If map can move blit it at specific coordinates
		if self.allScenes[self.sceneName][2]:
			# print(self.sceneName, x, y)
			screen.blit(self.image, (x,y))
		# If not blit it at the top left
		else:
			# print(self.sceneName)
			screen.blit(self.image, (0,0))
