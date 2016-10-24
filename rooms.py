#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from items import items
import commands

"""
All rooms in the game are stored in a dictionary called rooms.
Each room itself is a dictionary containing the following:
	info: a general description of the room. info is displayed at the beginning of each room and when the user types 'info','i'
	look: a description that reveals important objects in the room. Commands: 'look', 'l'
	exits: lists the possible exits to take from the current room. Commands: 'exit', 'exits'
	doorOpen: a dictionary that stores a list with boolean values for each door in the room. 
		Arg1 = True: door is open. False: door is locked.
		Arg2 = The room behind the door.
		This is not a command that can be input by the user.
	items: lists the items that the user can interact with. Commands: 'objects', 'obj'
	hint: displays a hint to help the user get out of the room. Commands: 'hint'
	help: displays a list of the commands that are available. Commands: 'help', 'h'

"""
rooms = {
	"your cell" : {
		"name" : "YOUR CELL",
		"info" : "You are in a creepy dungeon cell. There is a rotten corpse lying on the ground.",
		"look" : "The cell has an intense smell of putrefaction. There is a door to the south. Behind it you can see a guard going back and forth.",
		"exits" : ["south"],
		"doorOpen" : {"south" : [False, "corridor"]},
		"items" : ["corpse1", "belt", "guard1", "keys", "uniform"],
		"hint" : "Look at the dead body. It might have something useful for you. The guard should be eliminated if you want to leave this cell.",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"corridor" : {
		"name" : "THE CORRIDOR",
		"info" : "You are in the dungeon's corridor. The dead guard's body lies on the floor.",
		"look" : "There is a big wooden box in one side of the corridor. There is a round metal button on the floor,"
		" placed next to a gate in the south. The guard that you killed is lying by your cell's door. There are two"
		" open cells, one to the west and one to the east.",
		"exits" : ["north", "south", "east", "west"],
		"doorOpen" : {"north" : [True, "your cell"], "south" : [False, "guard room"], "east" : [False, "Eastern cell"], "west" : [False, "Western cell"]},
		"items" : ["dead guard", "box", "button", "uniform"],
		"hint" : "You should look like a guard if you want to survive. Explore the cells in search of items. What can the box and the button do?",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	}

}
