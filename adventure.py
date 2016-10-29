#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import getopt
import textwrap
import json
import os.path
import rooms 
import items 
import maps
import tictactoe

rooms = rooms.rooms
items = items.items

"""
GENERAL GLOBAL VARIABLES
"""
LOC = "your cell" # The initial location (room)
INV = [] # The player inventory
INVmax = 5 # Max number of items that can be stored in the inventory
ROOMS_VISITED = [] # List with visited rooms

"""
GLOBAL VARIABLES TO STORE CHANGES IN THE ROOMS ITEMS LIST
(we will use the to save and load game status)
"""
yourCell_items = []
corridor_items = []
westernCell_items = []
easternCell_items = []
guardRoom_items = []
southRoom_items = []
darkness_items = []
theYard_items = []

"""
GAME HISTORY SPECIFIC GLOBAL VARIABLES:
"""
CORPSE_BELT = True # True if the corpse wears the belt
GUARD1_IS_ALIVE = True # True if guard is alive
DEAD_GUARD_HAS_UNIFORM = True # True if the dead guard still wears the uniform
DEAD_GUARD_HAS_KEYS = True # True if the dead guard has the bunch of keys
BOX_ON_BUTTON = False # True if the box in the corridor is moved 
GUARDS_SLEEP = False # True if the pouch is used in the guards' room
BENCH_MOVED = False # True if the bench in the guards' room is moved
TORCH_FIRE = False # True if torch is in the inventory and lighter is in the inventory and lighter is used
SPIKES_UP = True # False if the button in darkness is pressed
PLAYER_WON = False # True if the player wins the TicTacToe match


def printw(txt):
	"""A textwrap for a nicer looking in the game text"""
	print(textwrap.fill(txt, 50))

def help():
	"""Displays the help options help menu"""
	print("\n")
	print("DUNGEON ESCAPE - HELP MENU")
	print("=" * len(("DUNGEON ESCAPE - HELP MENU")))
	print("This is a text based adventure game in which the player uses a series of ")
	print("commands and arguments in order to get to the next room, until she escapes the dungeon.")
	print("Type no options to start the game or...")
	print("You can type one of the following options:\n")
	print("   -h, --help:      Prints this help menu")
	print("   -i, --info:      Prints information about this game and the idea behind it")
	print("   -a, --about:     Prints information about me, the creator of this game")
	print("   -v, --version:   Prints the latest version")
	print("   -c, --cheat:     Prints an instruction, step by step, to win the game")


def info():
	print("\n")
	print("DUNGEON ESCAPE - GAME INFO")
	print("=" * len("DUNGEON ESCAPE - GAME INFO"))
	printw("This is a game about escaping from a dungeon without getting killed.")
	printw("You begin in a dungeon cell. The door is locked. There is a guard in the corridor."
	 		" What can you do?")
	printw("Use commands such us 'examine', 'look', 'take' or 'use' in order to solve the problems "
			"and get to the next room. Your reward is freedom...")
	print("\n")
	printw("This is my first text adventure game. I made it as a final project in a course on Python "
		"programming at Blekinge Institute of Technology (BTH) in Sweden.")
	printw("To develope this game I took much inspiration from the game 'Jabato', a classic Spanish "
		"text adventure game by Aventuras AD (1989). I think that a prison escape was a perfect topic "
		"for a text adventure game.")

def version():
	print("\n")
	print("DUNGEON ESCAPE - Version 1.0")

def about():
	print("\n")
	print("DUNGEON ESCAPE - ABOUT ME")
	print("=" * len("DUNGEON ESCAPE - ABOUT ME"))
	printw("My name is Javier Martinez and I am learning the basics of programming.")
	printw("Besides programming and making games I like music (metal, rock, jazz, classic), "
		"films, books and hamburgers.")

def cheat():
	print("\n")
	print("DUNGEON ESCAPE - CHEAT")
	print ("=" * len("DUNGEON ESCAPE - CHEAT"))
	print("There is a file that you can load that takes you to the very last room of the game.")
	print("In order to load it do one of these things:")
	print("- If you are in the start menu, type 2 and then type cheat.json or...")
	print("- If you are in the game, type load and then type cheat.json.\n")
	print("So you want to know how to get to end of the dungeon without loading any file?\nOk, I will expose the shortest way:\n")
	print("Room 1: Your cell")
	print("=" * len("Room 1: Your cell"))
	print(">>take belt   ... ... Take the belt from the corpse")
	print(">>use belt    ... ... Kill the guard by strangling him to death")
	print(">>take keys   ... ... Take the keys from the dead guard")
	print(">>open door   ... ... Open the door of your cell")
	print(">>south       ... ... Go south to the next room: The corridor")
	print("\n")
	print("Room 2: The corridor")
	print("=" * len("Room 2: The corridor"))
	print(">>take uniform... ... Take the dead guard's uniform and put it on")
	print(">>move box    ... ... Move the box and place it on the button. The gate to the south opens")
	print(">>west        ... ... Go west to the next room: Western cell")
	print("\n")
	print("Room 3: Western cell")
	print("=" * len("Room 3: Western cell"))
	print(">>take lighter... ... Take the lighter from inside the dead body's pocket")
	print(">>east        ... ... Go east to the next room: The corridor (again)")
	print(">>east        ... ... Go east to the next room: Eastern cell")
	print("\n")
	print("Room 4: Eastern cell")
	print("=" * len("Room 4: Eastern cell"))
	print(">>kick cupboard.. ... Kick the cupboard to break it")
	print(">>take pouch  ... ... Take the pouch")
	print(">>west        ... ... Go west to the next room: The corridor (again)")
	print(">>south       ... ... Go south to the next room: Guard room")
	print("\n")
	print("Room 5: Guard room")
	print("=" * len("Room 5: Guard room"))
	print(">>use pouch   ... ... Pour the powders into the guards' beer jars so that they fall asleep")
	print(">>take bracelet. ... Take the bracelet from one of the guards")
	print(">>move bench  ... ... Move the bench to unlock the exit to the south")
	print(">>south       ... ... Go south to the next room: South room")
	print("\n")
	print("Room 6: South room")
	print("=" * len("Room 6: South room"))
	print(">>open wardrobe.. ... Open the wardrobe")
	print(">>take torch  ... ... Take the torch")
	print(">>north       ... ... Go north to the next room: Guard room (again)")
	print(">>east        ... ... Go east to the next room: Darkness")
	print("\n")
	print("Room 7: Darkness")
	print("=" * len("Room 7: Darkness"))
	print(">>use lighter ... ... Use the lighter to lit the torch so that you can see")
	print(">>kick button ... ... Kick the trap button to deactivate the spikes trap")
	print(">>east        ... ... Go east to the next room: The yard")
	print("\n")
	print("Room 8: The yard")
	print("=" * len("Room 8: The yard"))
	print(">>use bracelet.. ... Use the bracelet to open the Final Gate")
	print(">>east        ... ... Go east to the next room: The TicTacToe chamber")
	print("\n")
	print("Room 9: The TicTacToe chamber")
	print("=" * len("Room 9: The TicTacToe chamber"))
	print("Type a number from 0 to 8 to select a spot. If you win you are free!")


def gameOver(): # TODO: Write a text. Go to the main menu.
	print("\n--++--+-+--++-+--+..GAME OVER..+--+-++--+-+--++--\n")
	sys.exit(0)
	

def saveGameStatus():
	global yourCell_items, corridor_items, westernCell_items, easternCell_items, guardRoom_items, southRoom_items, darkness_items, theYard_items
	printw("Saving game...\n")
	inp = input("Type the save file name: ")
	inp = inp.strip()
	if ".json" not in inp[-5:]:
		inp = inp + ".json"
	for i in rooms["your cell"]["items"]:
		yourCell_items.append(i)
	for item in rooms["corridor"]["items"]:
		corridor_items.append(item)
	for item in rooms["western cell"]["items"]:
		westernCell_items.append(item)
	for item in rooms["eastern cell"]["items"]:
		easternCell_items.append(item)
	for item in rooms["guard room"]["items"]:
		guardRoom_items.append(item)
	for item in rooms["south room"]["items"]:
		southRoom_items.append(item)
	for item in rooms["darkness"]["items"]:
		darkness_items.append(item)
	for item in rooms["the yard"]["items"]:
		theYard_items.append(item)
	
	gameStatus = {
		"LOC" : LOC,
		"INV" : INV,
		"ROOMS_VISITED" : ROOMS_VISITED,
		"CORPSE_BELT" : CORPSE_BELT,
		"GUARD1_IS_ALIVE" : GUARD1_IS_ALIVE,
		"DEAD_GUARD_HAS_UNIFORM" : DEAD_GUARD_HAS_UNIFORM,
		"DEAD_GUARD_HAS_KEYS" : DEAD_GUARD_HAS_KEYS,
		"LIGHTER_HIDDEN" : items["lighter"]["hidden"],
		"POUCH_HIDDEN" : items["pouch"]["hidden"],
		"BOX_ON_BUTTON" : BOX_ON_BUTTON,
		"GUARDS_SLEEP" : GUARDS_SLEEP,
		"BENCH_MOVED" : BENCH_MOVED,
		"TORCH_HIDDEN" : items["torch"]["hidden"],
		"TORCH_FIRE" : TORCH_FIRE,
		"SPIKES_UP" : SPIKES_UP,
		"YOUR CELL ITEMS" : yourCell_items,
		"CORRIDOR ITEMS" : corridor_items,
		"WESTERN CELL ITEMS" : westernCell_items,
		"EASTERN CELL ITEMS" : easternCell_items,
		"GUARD ROOM ITEMS" : guardRoom_items,
		"SOUTH ROOM ITEMS" : southRoom_items,
		"DARKNESS ITEMS" : darkness_items,
		"THE YARD ITEMS" : theYard_items
	}
	jsonfile = open(inp, "w")
	json.dump(gameStatus, jsonfile, indent=4)
	printw("Game status saved to " + inp)

def loadGameStatus():
	global INV, LOC, ROOMS_VISITED, CORPSE_BELT, GUARD1_IS_ALIVE, DEAD_GUARD_HAS_UNIFORM, DEAD_GUARD_HAS_KEYS
	global BOX_ON_BUTTON, GUARDS_SLEEP, BENCH_MOVED, TORCH_FIRE, SPIKES_UP
	global yourCell_items, corridor_items, westernCell_items, easternCell_items, guardRoom_items, southRoom_items, darkness_items, theYard_items
	printw("Loading game status...\n")
	inp = input("Type the save file name: ")
	inp = inp.strip()
	if ".json" not in inp[-5:]:
		inp = inp + ".json"
	if os.path.isfile(inp):
		jsonfile = open(inp, "r")
		jsonobject = json.load(jsonfile)
		INV = jsonobject["INV"] 
		LOC = jsonobject["LOC"]
		ROOMS_VISITED = jsonobject["ROOMS_VISITED"]
		CORPSE_BELT = jsonobject["CORPSE_BELT"]
		GUARD1_IS_ALIVE = jsonobject["GUARD1_IS_ALIVE"]
		DEAD_GUARD_HAS_UNIFORM = jsonobject["DEAD_GUARD_HAS_UNIFORM"]
		DEAD_GUARD_HAS_KEYS = jsonobject["DEAD_GUARD_HAS_KEYS"]
		items["lighter"]["hidden"] = jsonobject["LIGHTER_HIDDEN"]
		items["pouch"]["hidden"] = jsonobject["POUCH_HIDDEN"]
		BOX_ON_BUTTON = jsonobject["BOX_ON_BUTTON"]
		GUARDS_SLEEP = jsonobject["GUARDS_SLEEP"]
		BENCH_MOVED = jsonobject["BENCH_MOVED"]
		items["torch"]["hidden"] = jsonobject["TORCH_HIDDEN"]
		TORCH_FIRE = jsonobject["TORCH_FIRE"]
		SPIKES_UP = jsonobject["SPIKES_UP"]
		rooms["your cell"]["items"] = jsonobject["YOUR CELL ITEMS"]
		rooms["corridor"]["items"] = jsonobject["CORRIDOR ITEMS"]
	else:
		printw("File not found...")
		return

	roomInfo()
	game()

def printMap():
	"""
	MapDisplay(madness)
	"""
	if ROOMS_VISITED == ["your cell"]: 
		maps.map1()
	elif ROOMS_VISITED == ["your cell", "corridor"]: 
		maps.map2()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell"]: 
		maps.map3()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell"]: 
		maps.map4()
	elif ROOMS_VISITED == ["your cell", "corridor", "guard room"]: 
		maps.map14()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell"]: 
		maps.map5()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell"]: 
		maps.map5()
	elif ROOMS_VISITED == ["your cell", "corridor", "guard room", "darkness"]: 
		maps.map15()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room"]: 
		maps.map6()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room"]: 
		maps.map6()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room", "south room"]: 
		maps.map8()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room", "south room"]: 
		maps.map8()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room", "darkness"]: 
		maps.map7()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room", "darkness"]: 
		maps.map7()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room", "darkness", "south room"]: 
		maps.map9()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room", "south room", "darkness"]: 
		maps.map9()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room", "darkness", "south room"]: 
		maps.map9()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room", "south room", "darkness"]: 
		maps.map9()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room", "darkness", "south room", "the yard"]: 
		maps.map10()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "western cell", "guard room", "south room", "darkness", "the yard"]: 
		maps.map10()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room", "darkness", "south room", "the yard"]: 
		maps.map10()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "eastern cell", "guard room", "south room", "darkness", "the yard"]: 
		maps.map10()
	elif ROOMS_VISITED == ["your cell", "corridor", "western cell", "guard room", "darkness"]:
		map12()
	elif ROOMS_VISITED == ["your cell", "corridor", "guard room", "western cell", "darkness"]:
		maps.map12()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "guard room", "darkness", "south room"]:
		maps.map13()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "guard room", "south room", "darkness"]:
		maps.map13()
	elif ROOMS_VISITED == ["your cell", "corridor", "guard room", "darkness", "south room"]:
		maps.map13()
	elif ROOMS_VISITED == ["your cell", "corridor", "eastern cell", "guard room", "south room", "darkness"]:
		maps.map13()
	elif "freedom" in ROOMS_VISITED:
		maps.map11()

def roomInfo():
	"""
	Prints a room description and an ASCII-map. This function is called each time a rooms is entered.
	It also checks if the room is visited for the first time and if that is the case appends it to ROOMS_VISITED.
	"""
	global LOC, ROOMS_VISITED, DEAD_GUARD_HAS_UNIFORM
	if LOC not in ROOMS_VISITED:
		ROOMS_VISITED.append(LOC)
	print(chr(27) + "[2J" + chr(27) + "[;H") # Clears the console
	printMap()
	print("\n\n")
	printw(rooms[LOC]["name"])
	printw("=" * len(rooms[LOC]["name"]))
	if DEAD_GUARD_HAS_UNIFORM == True:
		if LOC == "guard room":
			printw("You enter in a room with two guards playing cards and drinking beer. When they see you they immediately grip you and then kill you.")
			gameOver()
	elif LOC == "freedom":
		printw("After winning the TicTacToe game, the chamber opened... You are free!")

	printw(rooms[LOC]["info"])

def printINV():
	"""Prints a list with the items in the player's inventory"""
	if len(INV) == 0:
		printw("Your inventory is empty.")
	else:
		printw("You have the following things in the inventory:\n")
		for i in INV:
			printw("> " + i)

def roomLook():
	global LOC, GUARD1_IS_ALIVE
	print("\n")
	if LOC == "your cell" and GUARD1_IS_ALIVE == False:
		printw(rooms[LOC]["look2"])
		return
	elif LOC == "guard room" and GUARDS_SLEEP == True and BENCH_MOVED == False:
		printw(rooms[LOC]["look2"])
		return
	elif LOC == "guard room" and GUARDS_SLEEP == True and BENCH_MOVED == True:
		printw(rooms[LOC]["look3"])
		return
	elif LOC == "darkness" and TORCH_FIRE == True:
		if SPIKES_UP == True:
			printw(rooms[LOC]["look2"])
			return
		else:
			printw(rooms[LOC]["look3"])
			return
	printw(rooms[LOC]["look"])

def keywordSearch(w2, func):
	"""
	Searches for a keyword in items["keywords"] and returns the keyword and the function specified in the argument
	"""
	global INV, LOC
	search = w2.split(" ")
	for i in search:
		for item in items.keys():
			if i in items[item]["keywords"] and LOC in items[item]["room"]:
				arg = items[item]["keywords"][0] 
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
				elif func == "itemOpen":
					itemOpen(arg)
					return
				elif func == "itemMove":
					itemMove(arg)
					return
				elif func == "itemKick":
					itemKick(arg)
					return
			elif i in INV:
				arg = items[item]["keywords"][0] 
				if func == "itemExamine":
					itemExamine(i)
					return
				if func == "itemDrop":
					itemDrop(i)
					return
				elif func == "itemUse":
					itemUse(i)
					return

	printw("There is no such thing in here.")

def itemExamine(arg):
	"""Implements the examine command"""
	# global INV, LOC, CORPSE_BELT, GUARD1_IS_ALIVE, DEAD_GUARD_HAS_KEYS, DEAD_GUARD_HAS_UNIFORM
	# global LIGHTER_REVEALED, POUCH_REVEALED, TORCH_REVEALED, TORCH_FIRE
	
	if arg in INV: # Examine items that are in the inventory:
		for item in items:
			if item == arg:
				print(items[item]["look1"])
				return
	elif arg in rooms[LOC]["items"]: # Check if the item is in the room
		if LOC == "your cell" and arg == "corpse": #-------------------- CORPSE1 -----------------
			if CORPSE_BELT == True:
				printw(items[arg]["look1"])
				return
			else:
				printw(items[arg]["look2"])
				return
		if LOC == "your cell" and arg == "guard": #----------------------- GUARD --------------------
			if GUARD1_IS_ALIVE == True:
				printw(items[arg]["look1"])
				return
			else:
				if DEAD_GUARD_HAS_KEYS == True and DEAD_GUARD_HAS_UNIFORM == True:
					printw(items[arg]["look2"])
					return
				elif DEAD_GUARD_HAS_KEYS == False and DEAD_GUARD_HAS_UNIFORM == True:
					printw(items[arg]["look3"])
					return
		if LOC == "corridor" and arg == "dead guard": #------------------------- DEAD GUARD------------------
			if DEAD_GUARD_HAS_UNIFORM:
				printw(items[arg]["look1"])
				return
			else:
				printw(items[arg]["look2"])
				return
		if LOC == "western cell" and arg == "dead body": #----------------------- DEAD BODY --------------
			if "lighter" in INV:
					printw(items[arg]["look2"])
					return
			else:
				printw(items[arg]["look1"])
				items["lighter"]["hidden"] = False
				return
		if LOC == "western cell" and arg == "lighter": #------------------------ LIGHTER ---------------------
			if items["lighter"]["hidden"] == False:
				printw(items[arg]["look1"])
				return
			else:
				printw("You can't see any lighter.")
		if LOC == "eastern cell" and arg == "cupboard":
			if items["pouch"]["hidden"] == True:
				printw(items[arg]["look1"])
				return
			else:
				printw(items[arg]["look2"])
				return
		if LOC == "eastern cell" and arg == "pouch": #---------------------------- POUCH ----------------------
			if items["pouch"]["hidden"] == False:
				printw(items[arg]["look1"])
				return
			else:
				printw("You can't see any pouch.")
		if LOC == "guard room" and arg == "two guards": #-------------------------TWO GUARDS-------------------
			if GUARDS_SLEEP == False:
				printw(items[arg]["look1"])
				return
			elif GUARDS_SLEEP == True:
				if "bracelet" in INV:
					printw(items[arg]["look3"])
					return
				else:
				 	printw(items[arg]["look2"])
				 	return
		if LOC == "south room" and arg == "torch": #----------------------------- TORCH ---------------------
			if items["torch"]["hidden"] == False:
				printw(items[arg]["look1"])
				return
			else:
				printw("You can't see any torch.")
		if LOC == "darkness" and arg == "spikes trap":
			if TORCH_FIRE == True:
				printw(items[arg]["look1"])
				return
			else:
				printw("You only see darkness...")
		else: # Examine items that aren't bounded to global variables
			printw(items[arg]["look1"])
			return
	else:
		printw("There is not such thing in this room.")
		return

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
	global INV, INVmax, LOC, CORPSE_BELT, GUARD1_IS_ALIVE, DEAD_GUARD_HAS_UNIFORM, DEAD_GUARD_HAS_KEYS, GUARDS_SLEEP, TORCH_FIRE
	global LIGHTER_REVEALED, POUCH_REVEALED, TORCH_REVEALED
	if arg in rooms[LOC]["items"]: # If the item is in the current room:
		if len(INV) < INVmax:
			if LOC == "your cell" and arg == "keys": #--------------------KEYS in your cell-----------------------------------
				if GUARD1_IS_ALIVE == True:
					printw(items[arg]["takable1"][1])
				else:
					if arg in rooms[LOC]["items"]:  
						printw(items[arg]["takable2"][1])	
						INV.append(arg)  
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
						INV.append(arg)
						roomRemoveItem(arg)
						CORPSE_BELT = False
						return
					else:
						printw("You take the belt.")
						INV.append(arg)
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
			elif LOC == "your cell" and arg == "guard": #-----------------------GUARD1 in your cell----------------------------
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
					roomRemoveItem(arg)
					return
			elif LOC == "western cell" and arg == "lighter": #-------------------------LIGHTER------------------------
				printw(items[arg]["takable1"][1])
				INV.append(arg)
				roomRemoveItem(arg)
				return
			elif LOC == "eastern cell" and arg == "pouch": #-------------------------POUCH in eastern cell-----------------
				if items["pouch"]["hidden"] == False:
					printw(items[arg]["takable1"][1])
					INV.append(arg)
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
						INV.append(arg)  
						roomRemoveItem(arg)
						return
					else:
						printw("The beer jars are not here.")
						return
			elif LOC == "guard room" and arg == "bracelet": #--------------------------BRACELET in guard room--------------------------
				if GUARDS_SLEEP == False:
					printw(items[arg]["takable1"][1])
					gameOver()
				else:
					if arg in rooms[LOC]["items"]:  
						printw(items[arg]["takable2"][1])	
						INV.append(arg)  
						roomRemoveItem(arg)
						return
					else:
						printw("The bracelet is not here.")
						return
			elif LOC == "south room" and arg == "torch": #---------------------------TORCH in south room-------------------
				if items["torch"]["hidden"] == False:
					printw(items[arg]["takable1"][1])
					INV.append(arg)
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
			printw("Your inventory is full. You need to drop something if you want to take an item.")
	else:
		printw("There is not such thing in here.")


def itemDrop(arg):
	"""Drops an item (arg) from the inventory and appends it to the room's item list"""
	global INV, LOC
	if arg in INV:
		rooms[LOC]["items"].append(arg) 
		cc = -1
		for i in INV:
			cc += 1
			if INV[cc] == arg:
				del INV[cc]
		printw("You drop: " + arg)

def itemUse(arg):
	"""Implements the use-command"""
	global INV, LOC, GUARD1_IS_ALIVE, TORCH_FIRE, GUARDS_SLEEP
	if arg in INV: # Only items that are in the inventory can be used
		if arg == "keys":
			if arg in INV:
				printw("Type 'open' instead.")
				return
		elif LOC == "your cell" and arg == "belt": #--------------------------BELT--------------------
			if GUARD1_IS_ALIVE == True:
				GUARD1_IS_ALIVE = False
				printw("You call the guard. He comes to you with an angry face." 
						" When he is near enough, you put the belt around his neck and strangle"
						" him to death. His dead body falls on the corridor's floor."
						)
			else:
				printw("You have already killed the guard.")
				return
		elif LOC == "darkness" and arg == "lighter": #-------------------------------LIGHTER-------------------------------------
			if "torch" in INV:
				TORCH_FIRE = True
				printw("You use the lighter and lit the torch. The torch's flame shines.")
				items["trap button"]["hidden"] == False
				items["spikes trap"]["hidden"] == False
				rooms[LOC]["items"].append("trap button")
				rooms[LOC]["items"].append("spikes trap")
			else:
				printw("You use the lighter. Nothing special happens...")
				return
		elif arg == "pouch": #---------------------------------POUCH--------------------------------------
			if LOC == "guard room":
				GUARDS_SLEEP = True
				printw("You use the pouch. You open it carefully and pour the powders into the guards' beer jars"
						" without them noticing it. After 5 minutes both guards fall in deep sleep.")
			else:
				printw("You use the pouch. Nothing special happens.")
				return
		elif arg == "torch": #---------------------------------TORCH--------------------------------------
			if TORCH_FIRE == False:
				printw("There is no point in using an unlit torch.")
			else:
				printw("You use the torch. Its flame shines.")
				return
		elif arg == "bracelet": #----------------------------WRISTBAND--------------------------------------
			if LOC == "the yard":
				printw("You use the bracelet. You place it on the gate so that the dragon's head connects to the"
					" dragon's body. The final gate opens...")
				rooms[LOC]["doorOpen"]["east"][0] = True
			else:
				printw("You use the bracelet. Nothing special happens...")
				return
	else:
		print("You can only use items that are in your inventory.")

def itemMove(arg):
	"""Implements the move command"""
	global LOC, BOX_ON_BUTTON, BENCH_MOVED
	if arg in rooms[LOC]["items"]: # If the item is in the actual room
		if arg == "box":
			BOX_ON_BUTTON = True 
			printw(items[arg]["movable1"][1])
			rooms[LOC]["doorOpen"]["south"][0] = True
			return
		elif arg == "bench":
			if GUARDS_SLEEP == False:
				printw(items[arg]["movable1"][1])
				gameOver()
			else:
				printw(items[arg]["movable2"][0])
				rooms[LOC]["doorOpen"]["south"][0] = True
				return
		else:
			printw(items[arg]["movable1"][1])
			return
	else:
		printw("There is no such thing.")
		return

def itemKick(arg):
	"""Implements the kick command"""
	print("\n")
	global LOC, GUARD1_IS_ALIVE, POUCH_REVEALED, SPIKES_UP
	if arg in rooms[LOC]["items"]: # If the item is in the room
		if arg == "guard":
			if GUARD1_IS_ALIVE:
				printw(items[arg]["kickable1"][1])
				gameOver()
			else:
				printw(items[arg]["kickable2"][1])
				return
		elif arg == "cupboard":
			if items["pouch"]["hidden"] == False:
				printw("You have already done this.")
				return
			else:
				items["pouch"]["hidden"] = False
				printw(items[arg]["kickable1"][1])
				rooms[LOC]["items"].append("pouch")
				roomRemoveItem(arg)
				return
		elif arg == "two guards":
			if GUARDS_SLEEP == False:
				printw(items[arg]["kickable1"][1])
				gameOver()
			else:
				printw(items[arg]["kickable2"][1])
				return
		elif arg == "beer jars":
			if GUARDS_SLEEP == False:
				printw(items[arg]["kickable1"][1])
				gameOver()
			else:
				printw(items[arg]["kickable2"][1])
				roomRemoveItem(arg)
				return
		elif arg == "trap button":
			if SPIKES_UP == True:
				SPIKES_UP = False
				printw(items[arg]["kickable1"][1])
				return
			else:
				printw("You only see darkness...")
				return
		elif arg == "spikes trap":
			if SPIKES_UP == True:
				printw(items[arg]["kickable1"][1])
				gameOver()
			else:
				printw(items[arg]["kickable2"][1])
				return
		else:
			printw(items[arg]["kickable1"][1])
			return
	else:
		printw("There is no such thing here.")

def itemOpen(arg):
	"""implements the open-command"""
	global INV, LOC, GUARD1_IS_ALIVE, BOX_ON_BUTTON, TORCH_REVEALED
	if LOC == "your cell": #### your cell: open door #####
		if arg == "doorYourCell":
			if "keys" in INV:
				printw("The door is now open.")
				rooms[LOC]["doorOpen"]["south"][0] = True
				return
			else:
				printw("The door is locked.")
	elif arg in rooms[LOC]["items"]:
		if LOC == "your cell" and "keys" not in INV:
			if arg == "doorYourCell":
				printw("The door is locked.")		
				return
		elif LOC == "corridor":
			if arg == "gate" or arg == "door":
				if BOX_ON_BUTTON == False:
					printw("The gate to the south is locked.")
				else:
					printw("The gate to the south is open.")
		elif LOC == "eastern cell" and arg == "cupboard": #### eastern cell: open cupboard ######
			printw("The cupboard is locked. You will have to open it some other way...")
			return
		elif LOC == "eastern cell" and arg == "pouch": ###### eastern cell: open pouch ##########
			if arg in INV:
				printw("You open the pouch and look at its contents...")
				return
			else:
				printw("You must take the pouch first...")
				return
		elif LOC == "south room" and arg == "wardrobe": ####### south room: wardrobe #########
			if items["torch"]["hidden"] == False:
				printw("The wardrobe is already open")
				return
			else:
				items["torch"]["hidden"] = False
				printw("You open the wardrobe. There is a torch inside it.")
				return
		else:
			printw("You can't open that.")
			return
	else:
		printw("There is no such thing here.")
		return

	
def roomPrintExits():
	global LOC
	printw("There are exits to these directions:")
	cc = -1
	for exit in rooms[LOC]["exits"]:
		cc += 1
		print("> " + rooms[LOC]["exits"][cc])
		
	

def roomLeave(w1):
	"""
	Direction management.
	The function checks if there are available exits to the given direction.
	If there are, the function checks if the door is open.
	If the door is open the player will leave the room.
	"""
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
			if LOC == "darkness" and TORCH_FIRE == False:
				printw("You try to get to the exit. You suddenly step on a spikes trap installed on the ground"
					" and your body falls on it. You die...")
				gameOver()
			else:
				printw("You go " + DIR)
				LOC = rooms[LOC]["doorOpen"][DIR][1]
				roomInfo()
		else:
			printw("The exit is locked.")
	else:
		printw("There are no exits to that direction.")
		roomPrintExits()

def roomObjects():
	#global LOC, LIGHTER_REVEALED, POUCH_REVEALED, TORCH_REVEALED
	print("\n")
	printw("You can see these objects:")
	for i in rooms[LOC]["items"]:
		if i in items:
			if items[i]["hidden"] == False:
				printw("> " +  items[i]["keywords"][0])
		
def roomHint(w1):
	global LOC
	printw(rooms[LOC]["hint"])

def gameQuit(): # TODO: save options
	printw("Thank you for playing!")
	sys.exit()

def gameHelp():
	"""
	Prints a list of the available commands and how to use them
	"""
	print("\n")
	print("HELP MENU - Commands list:")
	print("=========================\n")
	print("help, h:   ...   ...   Prints this help menu\n")
	print("info, i:   ...   ...   Prints a general description of the current room and ")
	print("                             the updated dungeon map\n")
	print("look, l:   ...   ...   Prints a more detailed description of the current room, ")
	print("                             sometimes revealing crucial information\n")
	print("objects, obj:.   ...   Prints a list of all existing objects in the current room")
	print("                             (a person is also considered as an object)\n")
	print("examine, ex [obj]...   Prints a description of the object, sometimes revealing")
	print("                             crucial information\n")
	print("take, t [obj]:   ...   Takes an existing object and stores it in the player's")
	print("                             inventory, e.g. take belt\n")
	print("drop, d [obj]:   ...   Drops an object from the inventory, e.g. drop belt\n")
	print("use, u [obj]:.   ...   Uses an object in the inventory, e.g. use belt\n")
	print("open, o [obj]:   ...   Opens an object, e.g. open door\n")
	print("move, m [obj]:   ...   Moves an object, e.g. move box\n")
	print("kick, k [obj]:   ...   Kicks an object, e.g. kick cupboard\n")
	print("exits:     ...   ...   Prints a list of all available exits in the current room\n")
	print("inventory, inv:  ...   Prints a list with all items in the player's inventory\n")
	print("north, n:  ...   ...   Goes north\n")
	print("south, s:  ...   ...   Goes south\n")
	print("east, e:   ...   ...   Goes east\n")
	print("west, w:   ...   ...   Goes west\n")
	print("save:      ...   ...   Saves the game state to a json file\n")
	print("load:      ...   ...   Loads the game state from a json file\n")
	print("hint:      ...   ...   Prints a hint that helps the player get to the next room\n")
	print("quit:      ...   ...   Exits the game\n")


def gameStart(): #TODO: develop this with more information
	"""Game presentation. This function gets called only once, at the beginning""" 
	print(chr(27) + "[2J" + chr(27) + "[;H") # Cleans the console
	print(" .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.")
	print("/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \ ")
	print("\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ /")
	print(" \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /")
	print(" / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\/ /\ ")
	print("/ /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\ \/\ \ ")
	print("\ \/\ \                                                    /\ \/ /")
	print(" \/ /\ \                                                  / /\/ /")
	print(" / /\/ /                 DUNGEON ESCAPE                   \ \/ /\ ")
	print("/ /\ \/                                                    \ \/\ \ ")
	print("\ \/\ \               a text adventure game                /\ \/ /")
	print(" \/ /\ \                                                  / /\/ /")
	print(" / /\/ /               by Javier Martínez                 \ \/ /\ ")
	print("/ /\ \/                                                    \ \/\ \ ")
	print("\ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /")
	print(" \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /")
	print(" / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\ ")
	print("/ /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \ ")
	print("\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /")
	print(" `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'")

	print("\n\n")
	print("                       TYPE 1 TO BEGIN")
	print("\n")
	print("                  TYPE 2 TO LOAD GAME STATUS")
	print("\n")
	print("               TYPE help TO SEE THE HELP MENU.")
	print("\n")
	while True:
		inp = input("-->")
		inp = inp.strip()
		inp = inp.lower()
		if inp == "1":
			roomInfo()
			game()
		elif inp == "2":
			loadGameStatus()
		elif inp == "h" or inp == "help":
			gameHelp()
		else:
			printw("Sorry, I didn't understand that. Please type help to see the help menu.")

def playerWins():
	"""When the player wins!"""
	global PLAYER_WON
	PLAYER_WON = True
	print(chr(27) + "[2J" + chr(27) + "[;H") # Clears the console
	print("\n")
	print("X", "|", "X", "|", "X")
	print("---------") 
	print("X", "|", "X", "|", "X")
	print("---------") 
	print("X", "|", "X", "|", "X")
	print("---------") 
	print("\n\n") 
	printw("The TicTacToe chamber opens in half...")
	printw("You are free now!")
	printw("RUN BEFORE THE GUARDS AWAKE!")
	print("\n")
	printw("Thank you for playing!")
	gameOver()

def game():
	while True:
		printw("+++--+++--+++--+++--+++--+++--+++--+++--+++--+++--")
		inp = input("\nWhat do you want to do?:\n>>  ")
		inp = inp.strip()
		inp = inp.lower()
		inpList = inp.split(" ")
		w1 = inpList[0] # This is the first word. This will be used as argument to call different functions later.
		w2 = " ".join(inpList[1:])  # These are the following word(s). This will also be used as an argument.
		if w1 == "h" or w1 == "help": 
			gameHelp()
		elif w1 == "i" or w1 == "info": 
			roomInfo()
		elif w1 == "l" or w1 == "look": 
			roomLook()
		elif w1 == "obj" or w1 == "object" or w1 == "objects": 
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
		elif w1 == "open" or w1 == "o":
			if w2 == "":
				printw("Open what?")
			else:
				keywordSearch(w2, "itemOpen")
		elif w1 == "m" or w1 == "move":
			if w2=="":
				printw("Move what?")
			else:
				keywordSearch(w2, "itemMove")
		elif w1 == "k" or w1 == "kick":
			if w2=="":
				printw("Kick what?")
			else:
				keywordSearch(w2, "itemKick")
		elif w1 == "exit" or w1 == "exits":
			roomPrintExits()
		elif w1 == "hint":
			roomHint(w1)
		elif w1 == "n" or w1 =="north" or w1 == "s" or w1 == "south" or w1 == "e" or w1 == "east" or w1 == "w" or w1 == "west":
			roomLeave(w1)
		elif w1 == "save":
			saveGameStatus()
		elif w1 == "load":
			loadGameStatus()
		elif w1 == "q" or w1 == "quit":
			gameQuit()
		elif LOC == "TicTacToe" and w1 == "play":
			tictactoe.gameStart()
		else:
			printw("Sorry, I didn't understand that. Please type --help to see the help menu.")


def parseOptions():
	"""Handles option input in the console"""
	global LOC, DIR, ITEM
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hivac', [
			"help",
			"info",
			"version",
			"about",
			"cheat",
			])
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				help()
				sys.exit(0)
			elif opt in ("-i", "--info"):
				info()
				sys.exit(0)
			elif opt in ("-v", "--version"):
				version()
				sys.exit(0)
			elif opt in ("-a", "--about"):
				about()
				sys.exit(0)
			elif opt in ("-c", "--cheat"):
				cheat()
				sys.exit(0)
	except getopt.GetoptError:
		print("Sorry... That is not a valid option.")
		print("Please, type --help to see the help menu.")
		sys.exit(1)
	gameStart()
	

if __name__ == '__main__':
	parseOptions()