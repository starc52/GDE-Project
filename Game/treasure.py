
from pygame import *
from random import randint

class Treasure:
	""" Displays treasures """

	def __init__(self, screen, player, maps):
		self.screen = screen
		self.player = player
		self.maps = maps
		# Resources
		self.coin = transform.scale(image.load("resources/graphics/misc/coin.png").convert(),(16,16))
		self.redDot = image.load("resources/graphics/misc/redDot.png").convert()
		# Fonts
		self.font = font.Font("resources/fonts/TooSimple.ttf", 12)
		self.arial = font.SysFont("Arial", 25)
		self.money = 10
		# Player's health
		self.health = 50
		# Weapons to keep track of max possible attack
		self.weapons = ["sword", "flameSword"]
		# Items -> (name, image, description, coordinates, rect, attack power)
		self.items = {
			"sword" : [
				"sword", 
				transform.scale2x(image.load("resources/graphics/items/sword.png").convert_alpha()),
				["A sword with an attack", "power of 5."],
				(363,209),
				Rect(363,209,50,50),
				5],
			"flameSword" : [
				"flameSword",
				transform.scale2x(image.load("resources/graphics/items/flameSword.png").convert_alpha()),
				["A fire sword with an", "attack power of 7"],
				(497,205),
				Rect(497,205,50,50),
				7],
			"boat" : [
				"boat", 
				image.load("resources/graphics/items/boat.png").convert_alpha(),
				["Power that allows you","to travel on water."],
				(422,200),
				Rect(422,200,50,50)],
			"brochure" : [
				"brochure",
				transform.scale2x(image.load("resources/graphics/items/brochure_small.png").convert_alpha()),
				["Brochure about The Black Pearl"," with 'CELL HERO' written on it."],
				(497,205),
				Rect(497,205,50,50),
				7],
			"letter1" : [
				"letter1",
				transform.scale2x(image.load("resources/graphics/items/letter1_preview_rev_1.png").convert_alpha()),
				["Dr.Newlin's reply:working", "on the vaccine", "in the Teshlor lab. NEVLIN...."],
				(560,205),
				Rect(560,205,50,50),
				7],
			"letter2" : [
				"letter2",
				transform.scale2x(image.load("resources/graphics/items/letter1_preview_rev_1.png").convert_alpha()),
				["Dr.Newlin's reply:working", "on the vaccine", "in the Teshlor lab. NEVLIN...."],
				(560,205),
				Rect(560,205,50,50),
				7],
			"key" : [
				"key",
				transform.scale2x(image.load("resources/graphics/items/key1.png").convert_alpha()),
				["Key which may help","you in the future."],
				(363,209),
				Rect(363,209,50,50),
				7],
			"laptop" : [
				"letter2",
				transform.scale2x(image.load("resources/graphics/items/laptop1.png").convert_alpha()),
				["Shows the zombie scare", "in Aquesta"],
				(630,205),
				Rect(630,205,50,50),
				7],
			"testtube" : [
				"testtube",
				transform.scale2x(image.load("resources/graphics/items/testtube.png").convert_alpha()),
				["Test tube which reminded","you how you became a cyborg."],
				(426,267),
				Rect(426,267,50,50),
				7],
			"microscope" : [
				"microscope",
				transform.scale2x(image.load("resources/graphics/items/microscope.png").convert_alpha()),
				["microscope which reminds you","of the vaccine."],
				(363,264),
				Rect(363,264,50,50),
				7],
			"worldMap" : [
				"worldMap",
				transform.scale(image.load("resources/graphics/map/null.png").convert_alpha(), (10, 10)),
				["World map which helps you navigate."],
				(540,192),
				Rect(540,192,50,50),
				7]
		}

		# All collected items
		self.collectedItems = set()
		# For speed instead of drawing text
		self.inventory = transform.scale2x(transform.scale2x(image.load("resources/graphics/misc/inventory.png").convert_alpha()))
		self.settings = transform.scale2x(transform.scale2x(image.load("resources/graphics/misc/settings1.jpg").convert_alpha()))
		self.mapView = transform.scale2x(transform.scale2x(image.load("resources/graphics/misc/mapView.png").convert_alpha()))
		self.smallMap = image.load("resources/graphics/map/smallMap1.png")

		# Item placeholders.
		self.placeholder = transform.scale2x(image.load("resources/graphics/misc/placeholder.png").convert_alpha())
		self.sPlaceholder = image.load("resources/graphics/misc/dropDown.png").convert_alpha()
		self.healthBar = transform.scale2x(image.load("resources/graphics/misc/healthBar.png").convert())

		self.inventoryRect = Rect(1028,140,40,40)
		self.settingsRect = Rect(1028,187,40,40)
		self.mapViewRect = Rect(1028,234,40,40)
		self.sceneLocs = {
			"hideout":(9311,2168),
			"BurntHouse":(1953, 2409),
			"dungeon":(1953,2409),
			"Lab":(1953,2409),
			"finalisland":(11517,8166),
			"islandPassword":(11517,8166)
		}
		# Slice up health bar and add to list
		self.healthPercent = []
		self.div = self.healthBar.get_width()/100
		for i in range(100):
			self.healthPercent.append(self.healthBar.subsurface(0,0,self.div*(i+1),self.healthBar.get_height()))

		self.transCol = (128,128,128)
		self.surf = Surface((150,150))
		self.surf.fill(self.transCol)
		self.surf.set_colorkey(self.transCol)
		draw.circle(self.surf, (0,0,0,100), (50,50), 50)
		self.surf.set_alpha(100)

		# Chosen setting
		self.inventoryOn = False
		self.settingsOn = False
		self.mapViewOn = False

		# Inventory/Settings surfaces
		self.back = Surface((1086,600))
		self.back.fill((0,0,0))
		self.back.set_alpha(150)

	def inventoryDisplay(self, click):
		""" Inventory (items) """
		pos = mouse.get_pos()
		close = Rect(707,56,65,80)
		self.screen.blit(self.back, (0,0))
		self.screen.blit(self.inventory, (318,30))
		# Blit collected items
		for item in self.collectedItems:
			self.screen.blit(self.items[item][1], self.items[item][3])
			# Text bitting with word wrap
			if self.items[item][4].collidepoint(pos):
				y = 441
				for i in range(len(self.items[item][2])):
					self.screen.blit(self.arial.render(self.items[item][2][i], True, (255,255,255)), (414,y))
					y += 26
		# Check for button press
		if close.collidepoint(pos) and click:
			self.inventoryOn = False

	def settingsDisplay(self, click):
		""" Settings """
		pos = mouse.get_pos()
		close = Rect(707,56,65,80)
		self.screen.blit(self.back, (0,0))
		self.screen.blit(self.settings, (318,30))
		# Check for button press
		if close.collidepoint(pos) and click:
			self.settingsOn = False

	def mapViewDisplay(self, click):
		""" Large scale map view """
		pos = mouse.get_pos()
		x, y = 0, 0
		if self.maps.sceneName == "mainWorld":
			x, y = self.player.x -self.player.mapCoords["mainWorld"][0], self.player.y-self.player.mapCoords["mainWorld"][1]
		elif self.maps.sceneName != "shipCabin" and self.maps.sceneName != "shipCorridor":
			x, y = self.sceneLocs[self.maps.sceneName][0], self.sceneLocs[self.maps.sceneName][1]
		
		smallMapLocx, smallMapLocy = 346+int((x/15564)*352), 195+int((y/9420)*355)
		#print(smallMapLocx, smallMapLocy)
		close = Rect(707,56,56,80)
		self.screen.blit(self.back, (0,0))
		self.screen.blit(self.mapView, (318,30))
		self.screen.blit(self.smallMap, (347,196))
		if self.maps.sceneName != "shipCabin" and self.maps.sceneName != "shipCorridor":
			self.screen.blit(self.redDot, (smallMapLocx, smallMapLocy))
		# Check for button press
		if close.collidepoint(pos) and click:
			self.mapViewOn = False

	def render(self, showing, inWorld, click, fighting, message):
		""" Render to screen """
		pos = mouse.get_pos()
		if showing:
			# Blit placeholders
			self.screen.blit(self.placeholder, (10,10))

			self.screen.blit(self.sPlaceholder, (940,10))
			self.screen.blit(self.healthPercent[self.health-1], (83,22))

			if fighting:
				if self.inventoryRect.collidepoint(pos) and click and not self.settingsOn and not self.mapViewOn:
					self.inventoryOn = True
				elif self.settingsRect.collidepoint(pos) and click and not self.inventoryOn and not self.mapViewOn:
					self.settingsOn = True
				elif self.mapViewRect.collidepoint(pos) and click and not self.settingsOn and not self.inventoryOn:
					self.mapViewOn = True

				# Check for button presses
				if self.inventoryOn and not self.settingsOn and not self.mapViewOn:
					self.player.canMove = False
					self.inventoryDisplay(click)
				if self.settingsOn and not self.inventoryOn and not self.mapViewOn:
					self.player.canMove = False
					self.settingsDisplay(click)
				if self.mapViewOn and not self.inventoryOn and not self.settingsOn:
					self.player.canMove = False
					self.mapViewDisplay(click)
