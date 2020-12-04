

from Game.player import Player
from pygame import *
from Game.const import *


class Story:
	""" Story line class """

	def __init__(self, message, treasure, player, screen, fade, maps, sound):
		
		self.screen = screen
		self.message = message
		self.treasure = treasure
		self.player = player
		self.fade = fade
		self.maps = maps
		self.sound = sound

# just for testing remove later
		self.treasure.collectedItems.add(self.treasure.items['boat'][0])

		self.selectedFirstLocation="rochelle"
		self.mainWorldMsgFinished = False
		self.gotWorldMap = False
		self.BurntHouseMsgFinished = False
		self.LabHouseMsgFinished = False
		self.islandMsgFinished = False
		self.passwordMsgFinished=False

		self.shipCorridorMsgFinished = False
		self.shipCabinMsgFinished = False

		# Flag to see if game is over (player won)
		self.gameWon = False

		
		self.letter1 = transform.scale(image.load("resources/graphics/items/letter1_preview_rev_1.png"),(70,70))
		self.letter2 = transform.scale(image.load("resources/graphics/items/letter1_preview_rev_1.png"),(70,70))
		self.brochure = transform.scale(image.load("resources/graphics/items/brochure.png"),(70,70))
		self.worldMap = transform.scale(image.load("resources/graphics/map/null.png"),(70,70))
		self.key = transform.scale(image.load("resources/graphics/items/key.png"),(70,70))
		self.laptop = transform.scale(image.load("resources/graphics/items/laptop.png"),(160,130))
		self.testtube = transform.scale(image.load("resources/graphics/items/testtube.png"),(70,70))
		self.microscope = transform.scale(image.load("resources/graphics/items/microscope.png"),(70,70))
		self.chestbox = transform.scale(image.load("resources/graphics/items/chest.png"),(70,70))
		# List of all available items (name -> description -> position -> cost -> rect)
		
		self.healthPotion = transform.scale(image.load("resources/graphics/items/healthPotion.png"), (70,70))
		# List of all available items (name -> description -> position -> cost -> rect)
		self.availableItems = {
			# "speedBoots" : [["These are the boots of Hermes.", "Legend says they increase your speed."], (156,135), 30, Rect(153,133,70,70)],
			# "earthGem" : [["Some sort of shining gem.", "It seems useless..."], (876,270), 200, Rect(864,262,self.earthGemImage.get_width()*2,self.earthGemImage.get_height()*2)],
			"healthPotion" : [["Potion to increase your health by 20."], (509,419), 50, Rect(509,419,70,70)],
			# "newPrayer" : [["New prayer to use at the church.", "You have %s prayers."%str(self.prayers)], (132,336), 100, Rect(132,336,100,100)],
			"brochure" : [[""], (876,270), 200, Rect(874,307,55,20)],
			"letter1" : [["Dr.Gwen says to Dr.Nevlin, ' I fear the zombie virus is far", "deadlier than we ever imagined. I have many unconfirmed reports , but", "there is no point spreading panic.'"], (676,250), 200, Rect(664,242,100,100)],
			"letter2" : [["You pick up Dr. Nevlin�s letter. 'Hope you are safe in the bunker.I ", "am working on the cure in our lab in Teshlor. I'm close.. The rest", "of it is gibberish - NEVLIN written repeatedly."],(132,336), 100, Rect(132,336,100,100)], 
			"worldMap" : [[""],(240,400), 100, Rect(240,400,70,70)],
			"key" : [[""], (429,339), 30, Rect(429,339,70,70)],
			"laptop" : [[""], (825,185), 200, Rect(825,185,100,100)],
			"testtube" : [[""], (123.5,464), 200, Rect(123.5,464,70,70)],
			"microscope" : [[""], (40.5,410), 200, Rect(40.5,410,70,70)],
			"chestbox" : [["treasure box."], (541,46), 200, Rect(530,35,80,80)]

		
		}
		# Reuturn rect
		self.shopReturn = Rect(833,508,300,300)

		# -----------------------------------

		# Keyboard actions
		self.spaceReady = False
		self.returnReady = False
		self.pReady = False

		
	def intro(self, next):
		""" Introduction """

		# Only do the narration scene once
		if not self.mainWorldMsgFinished:
			self.message.narration(["Clearly, this hideout has been deserted for quite some time.",\
				"Who was hiding.. And from what?",\
		], next, "top")
			if self.message.done:
				self.mainWorldMsgFinished = True
				if not mac:
					mixer.music.fadeout(500)
					mixer.music.load(self.sound.getMusic("mainWorldTheme"))
					mixer.music.play(loops=-1)
				self.message.reset()

	def hideout(self, click):
		""" Main hideout """
		pos = mouse.get_pos()

		def msg(text):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,200)), (229,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (255,49))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(1500)

		# Blit background
		self.screen.blit(transform.scale(self.message.background, (600,200)), (229,30))

		# Loop through the dictionary and draw the items
		for key,val in self.availableItems.items():
			

			if key == "letter1":
				# Animate gem shine
				self.screen.blit(self.letter1, val[1])
			if key == "letter2":
				# Animate gem shine
				self.screen.blit(self.letter2, val[1])
			
			
		# General description
		# Loop through items
		for item in [	
			["letter1", Rect(864,262,self.letter1.get_width()*2,self.letter1.get_height()*2)],
			["letter2", Rect(864,262,self.letter2.get_width()*2,self.letter2.get_height()*2)]
		]:
			if not item[1].collidepoint(pos):
				self.screen.blit(transform.scale(self.message.background, (600,200)), (229,30))
				self.screen.blit(self.message.font.render("Hover over an item to view its description.", True, (0,0,0)), (245,40))
				self.screen.blit(self.message.font.render("Click on it to collect it.", True, (0,0,0)), (245,90))

			else:
				if not item[0] in self.availableItems:
					self.screen.blit(transform.scale(self.message.background, (600,200)), (229,30))
					self.screen.blit(self.message.font.render("Hover over item for its description.", True, (0,0,0)), (245,40))
					self.screen.blit(self.message.font.render("Click on it to collect it.", True, (0,0,0)), (245,90))

		
		if "letter1" in self.availableItems:
			if self.availableItems["letter1"][3].collidepoint(pos):
				
				self.screen.blit(transform.scale(self.message.background, (600,200)), (229,30))
				self.screen.blit(self.message.font.render(self.availableItems["letter1"][0][0], True, (0,0,0)), (245,40))
				self.screen.blit(self.message.font.render(self.availableItems["letter1"][0][1], True, (0,0,0)), (245,90))
				self.screen.blit(self.message.font.render(self.availableItems["letter1"][0][2], True, (0,0,0)), (245,140))
				#self.screen.blit(self.message.font.render("$ %s"%str(self.availableItems["brochure"][2]), True, (255,255,255)), (515,532))
				if click:
						# Add item to inventory
					self.treasure.collectedItems.add("letter1")
						# Increase the player speed in all maps
						# Remove item from dictionary
					self.availableItems.pop("letter1", None)
					

		if "letter2" in self.availableItems:
			if self.availableItems["letter2"][3].collidepoint(pos):
				
				self.screen.blit(transform.scale(self.message.background, (600,150)), (229,30))
				self.screen.blit(self.message.font.render(self.availableItems["letter2"][0][0], True, (0,0,0)), (245,40))
				self.screen.blit(self.message.font.render(self.availableItems["letter2"][0][1], True, (0,0,0)), (245,90))
				self.screen.blit(self.message.font.render(self.availableItems["letter2"][0][2], True, (0,0,0)), (245,140))
				#self.screen.blit(self.message.font.render("$ %s"%str(self.availableItems["brochure"][2]), True, (255,255,255)), (515,532))
				if click:
						# Add item to inventory
					self.treasure.collectedItems.add("letter2")
						# Increase the player speed in all maps
						# Remove item from dictionary
					self.availableItems.pop("letter2", None)


		if self.shopReturn.collidepoint(pos) and click:
			# Fade into main world
			self.fade.fadeDark(self.maps.allScenes["mainWorld"][0], self.screen, self.player.mapCoords["mainWorld"])
			# Create new scene
			self.maps.newScene("mainWorld")
			# Set player coordinates
			self.player.x = self.player.mapx+9311
			self.player.y = self.player.mapy+2168
			# Reset fade
			self.fade.reset()
			# Change music

			if not mac:
				mixer.music.fadeout(500)
				mixer.music.load(self.sound.getMusic("mainWorldTheme"))
				mixer.music.play(loops=-1)

	def shipCorridor(self, next):
		""" Main surprise temple """
		#pos = mouse.get_pos()
		def msg(text, length):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (275,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(length)

		# Only do the narration scene once
		if not self.shipCorridorMsgFinished:
			self.message.narration(["You want answers and the only way to get them is get up and explore."], next, "top")
			if self.message.done:
				self.shipCorridorMsgFinished = True
				self.message.reset()

		for key,val in self.availableItems.items():
			if key == "brochure":
				self.screen.blit(self.brochure, val[1])
				break

		pos=[self.player.x,self.player.y]
		#pos=(x,y)
		# Speed boots
		if "brochure" in self.availableItems:
			if self.availableItems["brochure"][3].collidepoint(pos):
				# Word wrap text
				self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
				self.screen.blit(self.message.font.render(self.availableItems["brochure"][0][0], True, (0,0,0)), (275,59))
				self.treasure.collectedItems.add("brochure")
				
				self.availableItems.pop("brochure", None)
						# Notification
				msg("It's a brochure about some ship... The Black Pearl!", 3000)
				msg("Someone has scrawled, �CELL HERO� on it.", 3000)
				msg("Is it a hint?", 3000)

		
	
	def shipCabin(self, next):
		""" Main surprise temple """
		mousePos = mouse.get_pos()
		def msg(text, length):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (275,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(length)
		if not self.shipCabinMsgFinished:
			self.message.narration(["Looks like a control room of sorts"], next, "top")
			if self.message.done:
				self.shipCabinMsgFinished = True
				self.message.reset()

		for key,val in self.availableItems.items():
			if key == "worldMap":
				self.screen.blit(self.worldMap, val[1])

		pos=[self.player.x,self.player.y]
		# Speed boots
		if "worldMap" in self.availableItems:
			if self.availableItems["worldMap"][3].collidepoint(pos):
				# Word wrap text
				self.gotWorldMap = True
				self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
				self.screen.blit(self.message.font.render(self.availableItems["worldMap"][0][0], True, (0,0,0)), (275,59))
				self.treasure.collectedItems.add("worldMap")
				
				self.availableItems.pop("worldMap", None)
						# Notification

				msg("This is no ordinary map.", 2000)
				msg("It�s as though someone has marked on it... just for you.", 3000)
				msg("As you read it, it is stored in the hard-disk of your memory.", 3000)
				msg("Activate the map  by pressing the map button on the right.", 3000)
				msg("The ship demands the location of your first stop.", 3000)
				msg("What is it?", 2000)
				# while(not self.selectedFirstLocation):
				# 	self.selectedFirstLocation=self.message.firstLocationConfirm(click)
				# display.flip()
				#select first location here

	def BurntHouse(self, next):
		""" Main surprise temple """
		#pos = mouse.get_pos()
		def msg(text, length):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (275,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(length)

		# Only do the narration scene once
		if not self.BurntHouseMsgFinished:
			self.message.narration(["Acccchhhooo! You start coughing and sneezing as soon as you enter.",
									"The smell of burnt wood and ash is too strong.",
									"Maybe you will find something useful in the ruins?"
									], next, "top")
			if self.message.done:
				self.BurntHouseMsgFinished = True
				self.message.reset()
		for key,val in self.availableItems.items():
			if key == "key":
				self.screen.blit(self.key, val[1])

			if key == "laptop":
				self.screen.blit(self.laptop, val[1])

		pos=[self.player.x,self.player.y]
		#pos=(x,y)
		# Speed boots
		if "key" in self.availableItems:
			if self.availableItems["key"][3].collidepoint(pos):
				# Word wrap text
				self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
				self.screen.blit(self.message.font.render(self.availableItems["key"][0][0], True, (0,0,0)), (275,59))
				self.treasure.collectedItems.add("key")
				
				self.availableItems.pop("key", None)
						# Notification
				msg("The key is too light for its size (titanium, atomic number 22).", 3000)
				msg("It has a striped pattern(barcode signature), you think.", 3000)
				msg("Now how did you know that?", 2000)


		#print("pos 2 ")
		#print(pos)
		# Earth gem
		if "laptop" in self.availableItems:
			if self.availableItems["laptop"][3].collidepoint(pos):
				self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
				self.screen.blit(self.message.font.render(self.availableItems["laptop"][0][0], True, (0,0,0)), (275,59))
				self.treasure.collectedItems.add("laptop")
				
				self.availableItems.pop("laptop", None)
						# Notification
				msg("Your cyborg nature acts instinctively.", 2500)
				msg("You retrieve the hard-disk and connect it to your brain.", 3000)
				msg("Alas, most sectors are damaged and you see only random noise.", 3000)
				msg("A lone grainy video plays.", 2000)
				msg("�Frequent zombie attacks o--- coast...�", 2000)
				msg("�high infection rate in h--- Aquesta...�, a news reporter is saying.", 3000)
				msg("Aquesta. The name triggers something.", 2000)
				msg("All around him, there is rubble.", 2500)
				msg("People are running and screaming.", 2500)
				msg("You just realise you haven�t seen another person in days.", 3000)
				msg("Did the zombies kill everyone else ?", 2500)
	
	def Lab(self, next):
		""" Main surprise temple """
		#pos = mouse.get_pos()
		def msg(text, length):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,200)), (229,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (245,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(length)

		# Only do the narration scene once
		if not self.LabHouseMsgFinished:
			self.message.narration(["You have a sense of deja vu. ",
									"Yes, you had come here with Dr. Gwen!"
									], next, "top")
			if self.message.done:
				self.LabHouseMsgFinished = True
				self.message.reset()

		for key,val in self.availableItems.items():
			if key == "testtube":
				self.screen.blit(self.testtube, val[1])

			if key == "microscope":
				self.screen.blit(self.microscope, val[1])

		pos=[self.player.x,self.player.y]
		#pos=(x,y)
		# Speed boots
		if "testtube" in self.availableItems:
			if self.availableItems["testtube"][3].collidepoint(pos):
				# Word wrap text
				self.screen.blit(transform.scale(self.message.background, (600,150)), (229,30))
				self.screen.blit(self.message.font.render(self.availableItems["testtube"][0][0], True, (0,0,0)), (255,59))
				#self.screen.blit(self.message.font.render(self.availableItems["key"][0][1], True, (0,0,0)), (275,109))
				#self.screen.blit(self.message.font.render("$ %s"%str(self.availableItems["speedBoots"][2]), True, (255,255,255)), (515,532))
				self.treasure.collectedItems.add("testtube")
				
				self.availableItems.pop("testtube", None)
						# Notification
				msg("These test tubes are strangely familiar�", 3000)
				msg("You remember now, they are yours!", 3000)
				msg("Yes, you used to work here before as a researcher.", 3000)
				msg("Your name is Esra Stryker.", 2000)
				msg("Dr. Gwen and Dr. Nevlin were your colleagues and best friends.", 3000)
				msg("You recall everything right upto your accident. ", 3000)
				msg("Aha! Your friends made you a cyborg to save your life. ", 3000)
				msg("You must have been on the boat to get better treatment in Rochelle.", 3000)
				msg("They left behind the clues in case they didn�t survive.", 3000)
		#print("pos 2 ")
		#print(pos)
		if "microscope" in self.availableItems:
			if self.availableItems["microscope"][3].collidepoint(pos):
				self.screen.blit(transform.scale(self.message.background, (600,150)), (229,30))
				self.screen.blit(self.message.font.render(self.availableItems["microscope"][0][0], True, (0,0,0)), (255,59))
				self.treasure.collectedItems.add("microscope")
				
				self.availableItems.pop("microscope", None)
						# Notification
				msg("You peer through the microscope, observing the virus strains.", 3000)
				msg("You created them here.", 2000)
				msg("You had a rare gene that made you immune. ", 3000)
				msg("There was a mutation in your experiment and... ", 3000)
				msg("the zombie virus leaked out. Now everyone is gone.", 2000)
				msg("A wave of shame washes over you. ", 2500)
				msg("But wait, weren�t you trying to make the cure as well?", 3000)
				msg("Where is it? ", 2000)

	def dungeon(self, next):
		""" Main surprise temple """
		#pos = mouse.get_pos()
		def msg(text):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (275,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(1600)

	def finalisland(self, next):
		""" Main surprise temple """
		#pos = mouse.get_pos()
		def msg(text, length):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (275,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(length)

		if not self.islandMsgFinished:
			self.message.narration(["The cure is inside.",
									" In order to access it, ",
									" you must use the password."
									], next,"bottom")
			if self.message.done:
				self.islandMsgFinished = True
				self.message.reset()

		for key,val in self.availableItems.items():
			if key == "chestbox":
				self.screen.blit(self.chestbox, val[1])

		
		pos=[self.player.x,self.player.y]
		#pos=(x,y)
		# Speed boots
		if "chestbox" in self.availableItems:
			if self.availableItems["chestbox"][3].collidepoint(pos):
				# Word wrap text
				self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
				self.screen.blit(self.message.font.render(self.availableItems["chestbox"][0][0], True, (0,0,0)), (275,59))
				
				self.fade.fadeDark(self.maps.allScenes["islandPassword"][0], self.screen, (0, 0))
						# Create new scene	
				self.maps.newScene("islandPassword")
				# Set player coordinates
				self.player.x = self.player.mapx+516
				self.player.y = self.player.mapy+46
				# Reset fade
				self.fade.reset()
					
	def islandPassword(self, click, password):
		""" Ultimate shop to buy items """
		pos = mouse.get_pos()
		def msg(text, length):
			""" Render message """
			self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))
			self.screen.blit(self.message.font.render(text, True, (0,0,0)), (275,59))
			self.treasure.render(True, False, False, False, self.message)
			# Render and pause
			display.flip()
			time.wait(length)

		# Blit background
		# self.screen.blit(transform.scale(self.message.background, (600,150)), (259,30))

		keysDict = {
			"1": Rect(96, 72, 170, 90),
			"2": Rect(315, 72, 170, 90),
			"3": Rect(531, 72, 170, 90),
			"4": Rect(96, 200, 170, 90),
			"5": Rect(315, 200, 170, 90),
			"6": Rect(531, 200, 170, 90),
			"7": Rect(96, 322, 170, 90),
			"8": Rect(315, 322, 170, 90),
			"9": Rect(531, 322, 170, 90),
			"0": Rect(315, 451, 170, 90), 
			"cancel": Rect(803, 72, 170, 90),
			"clear": Rect(803, 200, 170, 90),
			"enter": Rect(803, 322, 170, 90)
		}
		if not self.passwordMsgFinished:
			msg("Enter Password", 1000)
			self.passwordMsgFinished=True
		correct = ["6", "3", "8", "5", "4", "6"]#original password
		for key in keysDict:
			if keysDict[key].collidepoint(pos):
				if click:
					# print("Pressed", key)
					if key!="cancel" and key!="clear" and key!="enter":
						password.append(key)
					if key== "cancel":
						self.fade.fadeDark(self.maps.allScenes["finalisland"][0], self.screen, (0, 0))
						# Create new scene	
						self.maps.newScene("finalisland")
						# Set player coordinates
						self.player.x = 510
						self.player.y = 46
						# Reset fade
						self.fade.reset()
					if key=="clear":
						password.clear()
					if key == "enter":
						if not ("key" in self.treasure.collectedItems):
							msg("Key Missing", 1500)
						else:
							if password == correct:
								#print("correct password")
								self.fade.fadeDark(self.maps.allScenes["finalisland"][0], self.screen, (0, 0))
								# Create new scene	
								self.maps.newScene("finalisland")
								# Set player coordinates
								self.player.x = 516
								self.player.y = 46
								# Reset fade
								self.fade.reset()
								msg("You have succesfully opened the safe.", 3000)
								self.gameWon=True

							else:
								msg("Wrong password. Press clear and try again.", 1500)


