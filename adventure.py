#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import textwrap
from rooms import rooms
from items import items
from maps import maps

"""
GENERAL GLOBAL VARIABLES
"""
LOC = "your cell" # The initial location (room)
INV = [] # The player inventory
INVmax = 5 # Max number of items that can be stored in the inventory
DIR = "" # Initializes the directions
ITEM = "" # Handles an item when it is taken or dropped or looked at
ROOMS_VISITED = [] # List with visited rooms

"""
GAME HISTORY SPECIFIC GLOBAL VARIABLES:
"""
CORPSE_BELT = True # True if the corpse wears the belt
GUARD1_IS_ALIVE = True # True if guard1 is alive
DEAD_GUARD_HAS_UNIFORM = True # True if the dead guard still wears the uniform
DEAD_GUARD_HAS_KEYS = True # True if the dead guard has the bunch of keys
LIGHTER_REVEALED = False # True if the player discovers the lighter
POUCH_REVEALED = False # True if the player discovers the pouch
BOX_ON_BUTTON = False # True if the box in the corridor is moved 
GUARDS_SLEEP = False # True if the pouch is used in the guards' room
BENCH_MOVED = False # True if the bench in the guards' room is moved
TORCH_REVEALED = False # True if the player discovers the torch
TORCH_FIRE = False # True if torch is in the inventory and lighter is in the inventory and lighter is used

def printw(txt):
	"""A textwrap for a nicer looking in the game text"""
	print(textwrap.fill(txt, 50))

def help():
	print("THIS IS THE HELP DISPLAY. IT IS HIDDEN IN help()")

def info():
	print("THIS IS THE INFO. IT IS IN info()")

def version():
	print("THIS IS THE VERSION. IN version()")

def about():
	print("THIS IS ABOUT ME. about()")

def cheat():
	print("THIS IS A GENERAL CHEAT. IT CONCERNS THE GAME IN GENERAL")

def gameOver(): # TODO: Write a text. Go to the main menu.
	printw("GAME OVER")
	sys.exit()

def roomInfo():
	"""
	Prints a room description and an ASCII-map. This function is called each time a rooms is entered.
	It also checks if the room is visited for the first time and if that is the case appends it to ROOMS_VISITED.
	"""
	global LOC, ROOMS_VISITED
	if LOC not in ROOMS_VISITED:
		ROOMS_VISITED.append(LOC)
	print(chr(27) + "[2J" + chr(27) + "[;H") # Clears the console
	if ROOMS_VISITED == ["your cell"]: 
		print(maps[0])
	elif ROOMS_VISITED == ["your cell", "corridor"]:
		print(maps[1])
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell"]:
		print(maps[2])
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell"]:
		print(maps[3])
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell"] or ROOMS_VISITED == ["your cell", "corridor", "western cell","eastern cell"]:
		print(maps[4])

	printw(rooms[LOC]["name"])
	printw("=" * len(rooms[LOC]["name"]))
	printw(rooms[LOC]["info"])

def printINV():
	"""Prints a list with the items in the player's inventory"""
	global INV
	if len(INV) == 0:
		printw("Your inventory is empty.")
	else:
		printw("You have the following things in the inventory:\n")
		for i in INV:
			printw("> " + i)

def roomLook():
	global LOC, GUARD1_IS_ALIVE
	print("\n")
	print(rooms[LOC]["name"])
	if LOC == "your cell" and GUARD1_IS_ALIVE == False:
		printw(rooms[LOC]["look2"])
		return
	printw(rooms[LOC]["look"])

def keywordSearch(w2, func):
	"""
	Searches for a keyword in items["keywords"] and calls the function specified in the argument
	"""
	global INV, LOC
	print("You are in keywordSearch()")
	search = w2.split(" ")
	for i in search:
		for item in items.keys():
			if i in items[item]["keywords"] and LOC in items[item]["room"]:
				arg = items[item]["keywords"][0] 
				print("arg=", arg)
				if func == "itemExamine":
					itemExamine(arg)
					return 
				elif func == "itemTake":
					itemTake(arg)
					return
				elif func == "itemDrop":
					if arg not in INV:
						printw("You don't have that in your inventory.")
						return
					else:
						itemDrop(arg)
						return
				elif func == "itemUse":
					itemUse(arg)
					return
				elif func == "open":
					open(arg)
					return
			elif i in INV:
				arg = items[item]["keywords"][0] 
				if func == "itemExamine":
					itemExamine(i)
					return
				if func == "itemDrop":
					itemDrop(i)
					return
	printw("There is no such thing in here.")

def itemExamine(arg):
	"""
	Takes the argument arg (an item) and checks if it is in LOC.
	If the item is in LOC the function will print a description.
	"""
	print("You are in itemExamine()")
	global INV, LOC, CORPSE_BELT, GUARD1_IS_ALIVE, PLAYER_HAS_KEYS, DEAD_GUARD_HAS_UNIFORM
	
	if arg in INV: # Examine items that are in the inventory:
		for item in items:
			if item == arg:
				print(items[item]["look1"])
	elif LOC == "your cell" and arg == "corpse1": ############### corpse1 ###############
		if CORPSE_BELT == True:
			for item in items:
				if item == arg:
					printw(items[item]["look1"])
		else:
			for item in items:
				if item == arg:
					printw(items[item]["look2"])
	elif LOC == "your cell" and arg == "belt": ############### belt ###############
		for item in items:
			if item == arg:
				printw(items[item]["look1"])
		CORPSE_BELT = False
	elif LOC == "your cell" and arg == "guard1": ############### guard1 ##############
		if GUARD1_IS_ALIVE:
			for item in items:
				if item == arg:
					printw(items[item]["look1"]) #guard1 is alive
		else:
			if DEAD_GUARD_HAS_KEYS == True:
				for item in items:
					if item == arg:
						printw(items[item]["look2"]) #guard1 is dead - it has keys
			else:
				for item in items:
					if item == arg:
						printw(items[item]["look3"]) #guard1 is dead - it has no keys
		# if arg == "keys": ###############keys###############
		# 	for item in items:
		# 		if item == arg:
		# 			printw(items[item]["look1"])
	elif LOC == "your cell" and arg == "uniform": ############### uniform ###############
		for item in items:
			if item == arg:
				printw(items[item]["look1"])
	elif LOC == "corridor" and arg == "dead guard":############### dead guard ###############
		print("You examine the dead guard")
		if DEAD_GUARD_HAS_UNIFORM == True:
			for item in items:
				if item == arg:
					printw(items[item]["look1"])
		else:
			for item in items:
				if item == arg:
					printw(items[item]["look2"])
	else: # Examine items that aren't bounded to a global variable (condition)
		for item in items:
			if item == arg:
				printw(items[item]["look1"])

def INVappend(arg):
	"""Appends new items to the inventory"""
	global INV
	if len(INV) < 5:
		INV.append(arg)
	else:
		printw("Your inventory is full. You need to drop something if you want to take this item.")


def roomRemoveItem(arg):
	""" Removes an item from the room when the player takes it """
	global LOC
	cc = -1
	for i in rooms[LOC]["items"]:
		cc += 1
		if rooms[LOC]["items"][cc] == arg:
			del rooms[LOC]["items"][cc]

def itemTake(arg):
	"""Implements the take command"""
	global INV, LOC, CORPSE_BELT, GUARD1_IS_ALIVE, DEAD_GUARD_HAS_UNIFORM, DEAD_GUARD_HAS_KEYS, GUARDS_SLEEP, TORCH_FIRE
	global LIGHTER_REVEALED, POUCH_REVEALED, TORCH_REVEALED
	if arg in rooms[LOC]["items"]: # If the item is in the current room:
		if LOC == "your cell" and arg == "keys": #--------------------KEYS in your cell-----------------------------------
			if GUARD1_IS_ALIVE == True:
				printw(items[arg]["takable1"][1])
				gameOver()
			else:
				if arg in rooms[LOC]["items"]:  
					printw(items[arg]["takable2"][1])	
					INVappend(arg)  
					roomRemoveItem(arg)
					DEAD_GUARD_HAS_KEYS = False
					return
				else:
					printw("The bunch of keys is not here.")
					return

		elif LOC == "your cell" and arg == "belt": #------------------BELT in your cell--------------------------------
			if arg in rooms[LOC]["items"]:
				if CORPSE_BELT == True:
					printw(items[arg]["takable1"][1])
					INVappend(arg)
					roomRemoveItem(arg)
					CORPSE_BELT = False
					return
				else:
					printw("You take the belt.")
					INVappend(arg)
					roomRemoveItem(arg)
					return
		elif LOC == "your cell" and arg == "uniform": #-------------------UNIFORM in your cell-----------------------------
			if GUARD1_IS_ALIVE == True:
				printw(items[arg]["takable1"][1])
				return
			else:
				printw(items[arg]["takable2"][1])
				return
		elif LOC == "corridor" and arg == "uniform":
			printw(items[arg]["takable3"][1])
			DEAD_GUARD_HAS_UNIFORM = False
			return
		elif LOC == "your cell" and arg == "guard1": #-----------------------GUARD1 in your cell----------------------------
			if GUARD1_IS_ALIVE == True:
				printw(items[arg]["takable1"][1])
				return
			else:
				printw(items[arg]["takable2"][1])
				return
		elif LOC == "corridor" and arg == "uniform": #-----------------------UNIFORM in corridor------------------------------
			if DEAD_GUARD_HAS_UNIFORM == True:
				printw(items[arg]["takable3"][1])
				DEAD_GUARD_HAS_UNIFORM = False
				return
		elif LOC == "eastern cell" and arg == "pouch": #-------------------------POUCH in eastern cell-----------------
			if POUCH_REVEALED == True:
				printw(items[arg]["takable1"][1])
				INVappend(arg)
				roomRemoveItem(arg)
				return
			else:
				printw("You can't see any pouch here.")
				return
		elif LOC == "guard room" and arg == "beer jars": #-----------------------BEER JARS in guard room------------------------------
			if GUARDS_SLEEP == False:
				printw(items[arg]["takable1"[1]])
				gameOver()
			else:
				if arg in rooms[LOC]["items"]:  
					printw(items[arg]["takable2"][1])	
					INVappend(arg)  
					roomRemoveItem(arg)
					return
				else:
					printw("The beer jars are not here.")
					return
		elif LOC == "guard room" and arg == "wristband": #--------------------------WRISTBAND in guard room--------------------------
			if GUARDS_SLEEP == False:
				printw(items[arg]["takable1"[1]])
				gameOver()
			else:
				if arg in rooms[LOC]["items"]:  
					printw(items[arg]["takable2"][1])	
					INVappend(arg)  
					roomRemoveItem(arg)
					return
				else:
					printw("The wristband is not here.")
					return
		elif LOC == "south room" and arg == "torch": #---------------------------TORCH in south room-------------------
			if TORCH_REVEALED == True:
				printw(items[arg]["takable1"[1]])
				INVappend(arg)
				roomRemoveItem(arg)
				return
			else:
				printw("You can't see any torch here.")
				return
		elif LOC == "darkness" and arg == "spikes trap": #-----------------------------SPIKES TRAP in darkness----------------
			if TORCH_FIRE == False:
				printw(items[arg]["takable1"][1])
				gameOver()
			else:
				printw(items[arg]["takable2"][0])
				return
		elif items[arg]["takable1"][0] == True: #----------------ALL THE REST (items that only have "takable1" and are not dependant on global variables)
			printw(items[arg]["takable1"][1])	
			INV.append(arg) # Store the item in the player's inventory
			cc = -1
			for i in rooms[LOC]["items"]:
				cc += 1
				if rooms[LOC]["items"][cc] == arg:
					del rooms[LOC]["items"][cc] # Remove the item from the room
		else: # If the item can't be taken
			printw(items[arg]["takable1"][1])
	else:
		printw("There is not such thing in here.")
# def itemTake(arg):
# 	"""Takes an item (arg), stores it in the player's inventory and removes it from the room"""
# 	global INV, LOC, CORPSE_BELT, GUARD1_IS_ALIVE, DEAD_GUARD_HAS_UNIFORM, DEAD_GUARD_HAS_KEYS
# 	print("You are in itemTake()")
# 	# TAKE ITEMS THAT DEPEND ON GLOBAL VARIABLES (items that have "takable1", "takable2", etc)
# 	if LOC == "your cell" and arg == "keys": ###########################TAKE KEYS
# 		if GUARD1_IS_ALIVE:
# 			printw(items[arg]["takable1"][1])
# 			gameOver()
# 		else:
# 			if arg in rooms[LOC]["items"]: # Check if the item is in the room (if the item exists)
# 				if items[arg]["takable2"][0] == True: # Do the following in case the item can be taken:
# 					printw(items[arg]["takable2"][1])	
# 					INV.append(arg) # Store the item in the player's inventory
# 					cc = -1
# 					for i in rooms[LOC]["items"]:
# 						cc += 1
# 						if rooms[LOC]["items"][cc] == arg:
# 							del rooms[LOC]["items"][cc] # Remove the item from the room
# 					DEAD_GUARD_HAS_KEYS = False
# 					return
# 	elif LOC == "your cell" and arg == "uniform": ##############################TAKE UNIFORM
# 		if GUARD1_IS_ALIVE:
# 			printw(items[arg]["takable1"][1])
# 		else:
# 			printw(items[arg]["takable2"][1])
# 	elif LOC == "your cell" and arg == "belt": ##############################TAKE BELT
# 		if CORPSE_BELT == True:
# 			if items[arg]["takable"][0] == True: # Do the following in case the item can be taken:
# 					printw(items[arg]["takable"][1])	
# 					INV.append(arg) # Store the item in the player's inventory
# 					cc = -1
# 					for i in rooms[LOC]["items"]:
# 						cc += 1
# 						if rooms[LOC]["items"][cc] == arg:
# 							del rooms[LOC]["items"][cc] # Remove the item from the room
# 					CORPSE_BELT = False
# 					return
# 	elif LOC == "corridor" and arg == "uniform":
# 		if items[arg]["takable"][0] == True: # Do the following in case the item can be taken:
# 					printw(items[arg]["takable"][1])
# 					cc = -1
# 					for i in rooms[LOC]["items"]:
# 						cc += 1
# 						if rooms[LOC]["items"][cc] == arg:
# 							del rooms[LOC]["items"][cc] # Remove the item from the room
# 					DEAD_GUARD_HAS_UNIFORM = False
# 	else: # Take items that aren't bounded to any condition
# 		if arg in rooms[LOC]["items"]: # Check if the item is in the room (if the item exists)
# 			if items[arg]["takable1"][0] == True: # Do the following in case the item can be taken:
# 				printw(items[arg]["takable1"][1])	
# 				INV.append(arg) # Store the item in the player's inventory
# 				cc = -1
# 				for i in rooms[LOC]["items"]:
# 					cc += 1
# 					if rooms[LOC]["items"][cc] == arg:
# 						del rooms[LOC]["items"][cc] # Remove the item from the room
# 			else: # If the item can't be taken
# 				printw(items[arg]["takable1"][1])
# 		else: # Do this if the itemo doesn't exist in the room:
# 			printw("There is not such thing in this room")

def itemDrop(arg):
	"""Drops an item (arg) from the inventory and appends it to the room's item list"""
	global INV, LOC
	print("You are in itemDrop()")
	if arg in INV:
		rooms[LOC]["items"].append(arg) 
		cc = -1
		for i in INV:
			if INV[cc] == arg:
				del INV[cc]
		printw("You drop: " + arg)

def itemUse(arg):
	"""Implements the use-command"""
	global INV, LOC, GUARD1_IS_ALIVE
	if arg == "keys":
		if arg in INV:
			printw("Type 'open' instead.")
	# ROOM "your cell":
	if arg == "belt":
		if arg in INV:
			if LOC == "your cell":
				if GUARD1_IS_ALIVE == True:
					GUARD1_IS_ALIVE = False
					printw("You call the guard while you hide the belt behind your back."
						" The guard comes to you with an angry face. When he is near enough"
						" you put the belt around his neck and strangle him to death."
						" His dead body falls on the corridor's floor.")
			else:
				printw("There is no point in using the belt here.")
		else:
			print("You have no such thing in your inventory.")

def open(arg):
	"""implements the open-command"""
	global INV, LOC, GUARD1_IS_ALIVE
	if LOC == "your cell" and "keys" in INV: #### your cell: open door #####
		if arg == "doorYourCell":
			printw("The door is now open.")
			rooms[LOC]["doorOpen"]["south"][0] = True
	elif LOC == "your cell" and "keys" not in INV:
		if arg == "doorYourCell":
			printw("The door is locked.")		
	elif LOC == "easter cell" and arg == "wardrobe": #### eastern cell: open wardrobe ######
		printw("The wardrobe is locked. You will have to open it some other way...")
	elif LOC == "eastern cell" and arg == "pouch": ###### eastern cell: open pouch ##########
		if arg in INV:
			printw("You open the pouch and look at its contents...")
		else:
			printw("You must take the pouch first...")
	
def roomPrintExits():
	global LOC
	printw("There are exits to these directions:")
	for exit in rooms[LOC]["exits"]:
		printw('\n'.join(rooms[LOC]["exits"]))
		return
	

def roomLeave(w1):
	"""
	Direction management.
	The function checks if there are available exits to the given direction.
	If there are, the function checks if the door is open.
	If the door is open the player will leave the room.
	"""
	print("You are in roomLeave()")
	global LOC
	DIR = w1
	if DIR == "n":
		DIR = "north"
	if DIR == "s":
		DIR = "south"
	if DIR == "e":
		DIR = "east"
	if DIR == "w":
		DIR = "west"

	if DIR in rooms[LOC]["exits"]:
		if rooms[LOC]["doorOpen"][DIR][0] == True:
			printw("You go " + DIR)
			LOC = rooms[LOC]["doorOpen"][DIR][1]
			roomInfo()
		else:
			printw("The door is locked.")
	else:
		printw("There are no exits to that direction.")
		roomExits()

def roomObjects():
	global LOC
	print("\n")
	printw("This room contains the following things:")
	for i in rooms[LOC]["items"]:
		keyword = items[i]["keywords"]
		if i in items:
			printw("-" + keyword[0])
		

def gameQuit(): # TODO: save options
	printw("Thank you for playing!")
	sys.exit()

def gameStart(): #TODO: develop this with more information
	"""Game presentation. This function gets called only once, at the beginning""" 
	print(chr(27) + "[2J" + chr(27) + "[;H") # Cleans the console
	printw("***DUNGEON ESCAPE***")
	printw("A game by Javier Martínez")
	printw("Type --help to see the help menu.")
	printw("Type quit to quit\n\n")
	roomInfo()
	game()

def game():
	while True:
		printw("+++--+++--+++--+++--+++--+++--+++--+++--+++--+++--")
		inp = input("\nWhat do you want to do?: -->")
		inp = inp.strip()
		inpList = inp.split(" ")
		w1 = inpList[0] # This is the first word. This will be used as argument to call different functions later.
		w2 = " ".join(inpList[1:])  # These are the following word(s). This will also be used as an argument.
		if w1 == "-h" or w1 == "--help": 
			help()
		elif w1 == "-i" or w1 == "--info": 
			info()
		elif w1 == "-v" or w1 == "--version": 
			version()
		elif w1 == "-a" or w1 == "--about": 
			about()
		elif w1 == "-c" or w1 == "--cheat": 
			cheat()
		elif w1 == "i" or w1 == "info": 
			roomInfo()
		elif w1 == "h" or w1 == "help": 
			pass
			#roomCommands()
		elif w1 == "l" or w1 == "look": 
			roomLook()
		elif w1 == "o" or w1 == "object" or w1 == "objects": 
			roomObjects()
		elif w1 == "ex" or w1 == "examine": 
			if w2=="":
				printw("Examine what?")
			else:
				keywordSearch(w2, "itemExamine")
		elif w1 == "t" or w1 == "take": 
			if w2=="":
				printw("Take what?")
			else:
				keywordSearch(w2, "itemTake")
		elif w1 == "d" or w1 == "drop": 
			if w2=="":
				printw("Drop what?")
			else:
				keywordSearch(w2, "itemDrop")
		elif w1 == "inv" or w1 == "inventory":
			printINV()
		elif w1 == "u" or w1 == "use":
			if w2=="":
				printw("Use what?")
			else:
				keywordSearch(w2, "itemUse")
		elif w1 == "open":
			if w2 == "":
				printw("Open what?")
			else:
				keywordSearch(w2, "open")
		elif w1 == "m" or w1 == "move":
			pass
			#if w2=="":
				#printw("What?")
			#else:
				#itemMove(LOC, w2)
		elif w1 == "k" or w1 == "kick":
			pass
			#if w2=="":
				#printw("What?")
			#else:
				#itemKick(LOC, w2)
		elif w1 == "exit" or w1 == "exits":
			roomPrintExits()
		elif w1 == "n" or w1 =="north" or w1 == "s" or w1 == "south" or w1 == "e" or w1 == "east" or w1 == "w" or w1 == "west":
			roomLeave(w1)
		elif w1 == "q" or w1 == "quit":
			gameQuit()
		else:
			printw("Sorry, I didn't understand that. Please type --help to see the help menu.")

# def parseOptions():
# 	global LOC, DIR, ITEM
# 	try:
# 		opts, args = getopt.getopt(sys.argv[1:], 'hivac', [
# 			"help",
# 			"info",
# 			"version",
# 			"about",
# 			"cheat"
# 			])
# 		for opt, arg in opts:
# 			if opt in ("-h", "--help"):
# 				help()
# 			elif opt in ("-i", "--info"):
# 				info()
# 			elif opt in ("-v", "--version"):
# 				version()
# 			elif opt in ("-a", "--about"):
# 				about()
# 			elif opt in ("-c", "--cheat"):
# 				cheat()
# 			else:
# 				print("Sorry... That is not a valid option.")
# 	except getopt.GetoptError:
# 		print("Sorry... That is not a valid option.")
# 		print("Please, type --help to see the help menu.")
	
# 	for arg in args:	
# 		if args[0] == "info" or args[0] == "i": # INFO
# 			roomInfo(LOC)
# 		elif args[0] == "look" or args[0] == "l": # LOOK
# 			roomLook(LOC)
# 		elif args[0] == "examine" or args[0] == "ex" or args[0] == "inspect": # EXAMINE
# 			if len(args) > 1:
# 				itemExamine(LOC, args[1])
# 			else:
# 				printw("What?")
# 		elif args[0] == "exit" or args[0] == "exits": # EXITS
# 			roomExits(LOC)
# 		elif args[0] in ["north", "n", "south", "s", "east", "e", "west", "w"]: # N S W E
# 			roomDirections(LOC, args[0])
# 		elif args[0] == "take" or args[0] == "t": # TAKE
# 			if len(args) > 1:
# 				itemTake(LOC, args[1])
# 			else:
# 				printw("What?")
# 		elif args[0] == "object" or args[0] == "objects" or args[0] == "o": # OBJECTS (list objects in the room)
# 			roomObjects(LOC)
# 		else:
# 			printw("Sorry... I didn't understand that. Please, type --help to see the help menu.")
		

if __name__ == '__main__':
	gameStart()