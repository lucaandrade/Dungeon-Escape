#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from items import items
import commands

"""
All rooms in the game are stored in a dictionary called rooms.
Each room in the dictionary ia a dictionary itself, containing the following:
	"name" : The room's name that will be printed in the game.
	"info": a general description of the room. info is displayed at the beginning of each room and when the user types 'info','i'
	"look": a description that reveals important objects in the room. Commands: 'look', 'l'
	"look 1-3": same as "look", but these are dependent on global variables that control the game flow.
	"exits": lists the possible exits to take from the current room. Commands: 'exit', 'exits'
	"doorOpen": a dictionary that stores a list with boolean values for each door in the room. 
		Arg1 = True: door is open. False: door is locked.
		Arg2 = The room behind the door.
		This is not a command that can be input by the user.
	"items": lists the items that the user can interact with. Commands: 'objects', 'obj'
	"hint": displays a hint to help the user get out of the room. Commands: 'hint'
	"help": displays a list of the commands that are useful within the roomxx. Commands: 'help', 'h'

"""
rooms = {
	"your cell" : {
		"name" : "YOUR CELL",
		"info" : "You are in a creepy dungeon cell. There is a rotten corpse lying on the ground.",
		"look" : "The cell has an intense smell of putrefaction. There is a door to the south. Behind it you can see a guard going back and forth.",
		"look2" : "The cell has an intense smell of putrefaction. There is a door to the south. Behind it you can see the dead guard lying on the floor.",
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
		" open cells, one to the west and one to the east. The gate to the south is locked.",
		"exits" : ["north", "south", "east", "west"],
		"doorOpen" : {"north" : [True, "your cell"], "south" : [False, "guard room"], "east" : [True, "eastern cell"], "west" : [True, "western cell"]},
		"items" : ["dead guard", "box", "button", "uniform", "gate"],
		"hint" : "You should look like a guard if you want to survive. Explore the cells in search of items. What can the box and the button do?",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"western cell" : {
		"name" : "THE WESTERN CELL",
		"info" : "A creepy dungeon cell. There is a dead body chained to the wall.",
		"look" : "This cell is as creepy and dark as the rest of the dungeon. The dead body has signs of having been tortured.",
		"exits" : ["east"],
		"doorOpen" : {"east" : [True, "corridor"]},
		"items" : ["dead body", "lighter"],
		"hint" : "Have you examined the dead body?",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"eastern cell" : {
		"name" : "THE EASTERN CELL",
		"info" : "Another creepy dungeon cell. At least there are no dead bodies in here...",
		"look" : "Dark and cold... There is a little wooden wardrobe attached to the wall.",
		"exits" : ["west"],
		"doorOpen" : {"west" : [True, "corridor"]},
		"items" : ["wardrobe", "pouch"],
		"hint" : "Break that wardrobe!",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"guard room" : {
		"name" : "THE GUARDS' ROOM",
		"info" : "You are at the guards' room.",
		"look" : "You see two guards playing cards and drinking beer in big jars. They believe you are one of them. "
		"There is a bench blocking an exit to the south.",
		"look2" : "The guards sleep deeply. There is a bench blocking an exit to the south.",
		"look3" : "The guards sleep deeply. The bench no longer blocks the exit to the south.",
		"exits" : ["north", "south", "east"],
		"doorOpen" : {"north" : [True, "corridor"], "south" : [False, "south room"], "east" : [True, "darkness"]},
		"items" : ["two guards", "beer jars", "bench", "wristband"],
		"hint" : "What can those powders in the leather couch be used for? They might combine perfectly with the beers... "
		"Have you tried to move the bench?",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"south room" : {
		"name" : "THE SOUTH ROOM",
		"info" : "You are at the south room.",
		"look" : "The only remarkable thing about this room is a big wardrobe next to a wall.",
		"look2" : "The only remarkable thing about this room is a big wardrobe next to a wall. There is a torch inside the wardrobe.",
		"exits" : ["north"],
		"doorOpen" : {"north" : [True, "guard room"]},
		"items" : ["wardrobe south", "torch"],
		"hint" : "Open the wardrobe and examine it. There is something important inside it.",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"darkness" : {
		"name" : "DARKNESS",
		"info" : "You are now in darkness...",
		"info1" : "The only light in the darkness is the flame that shines in a torch.",
		"look" : "The only thing your eyes manage to see is a kind of exit to the east ",
		"look2" : "The shining flame of the torch lets you discover a spike trap installed in the center of the room. By the trap's side there is "
		"a button on the floor.",
		"look3" : "The trap has been deactivated. The spikes are down.",
		"exits" : ["east", "west"],
		"doorOpen" : {"west": [True, "guard room"], "east" : [True, "the yard"]},
		"items" : ["spike trap", "button", "burning torch"],
		"hint" : "Have you found a lighter? Do you have a torch? When you are able to see you will then need to kick something.",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"the yard" : {
		"name" : "THE YARD",
		"info" : "You are in the outside of the dungeon, in a yard.",
		"look" : "At the end of the yard, to the east, you find the final gate. It is the gate to freedom. The gate has no keyhole,"
		"but instead there is a kind of magnetic opening mechanism at its center, with a headless dragon body drawn in it. It seems "
		"that the drawing must be completed with a head for the gate to open.",
		"exits" : ["east", "west"],
		"doorOpen" : {"west" : [True, "darkness"], "east" : [False, "TicTacToe"]},
		"items" : ["final gate"],
		"hint" : "Do you have anything in your inventory that has a dragon head drawn in it?",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	},
	"TicTacToe" : {
		"name" : "THE TICTACTOE CHAMBER",
		"info" : "You are one step away from freedom. Behind the final gate there is a chamber with a big touch screen at its center."
		" You have to play TicTacToe against an evil electronic brain. This match is about life or death. Type 'play' to begin. "
		"May God be with you now...",
		"look" : "You are one step away from freedom. Behind the final gate there is a chamber with a big touch screen at its center."
		" You have to play TicTacToe against an evil electronic brain. This match is about life or death. Type 'play' to begin. "
		"My God be with you now...",
		"doorOpen" : {},
		"items" : ["TicTacToe device"],
		"hint" : "Google the TicTacToe rules if you don't know how to play.",
		"help" : "You can use these commands in this room: look / objects / take / , TODO"
	}
}
