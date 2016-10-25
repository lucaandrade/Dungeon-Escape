#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The items in the game are stored in a dictionary called items.
Each item in the dictionary is a dictionary itsfelf, containing the following:
"room" : the name of the room in which the item is initially placed.
"look1-3" : descriptions of the item. Some of them are dependant on global variables. Commands: ex, examine
"keywords" : a list of recognized words for each item. These keywords are parsed in the function keywordSearch(), which returns the
	first value in "keywords", which also corresponds to the key in the item's dictionary (ex "corpse1" or "belt")
"takable1-3": A list consisting on a boolean value (True: the item can be taken) and the corresponding string that gets printed after it.
"movable1-3": A list consisting on a boolean value (True: the item can be moved) and the corresponding string that gets printed after it.
"kickable1-3": A list consisting on a boolean value (True: the item can be kicked) and the corresponding string that gets printed after it.
"""
items = {
	"corpse1" : {
		"room" : "your cell",
		"look1" : "A very rotten man's corpse. The corpse has a belt on.",
		"look2" : "A very rotten man's corpse.",
		"keywords" : ["corpse1", "corpse", "body", "dead", "cadaver", "rotten"],
		"takable1" : [False, "Taking a rotten corpse doesn't sound like a good idea."],
		"movable1" : [True, "You move the corpse. Nothing special happens."],
		"kickable1" : [True, "You kick the corpse. That was so macabre..."]
		},
	"belt" : {
		"room" : "your cell",
		"look1" : "A leather belt. Hard and robust.",
		"takable1" : [True, "Without any consideration to the dead body, you take the belt and hide it behind your back."],
		"keywords" : ["belt"],
		"movable1" : [True, "That is absurd."],
		"kickable1" : [True, "You kick the belt. You should take care of it instead."]
		},
	"doorYourCell" : {
		"room" : "your cell",
		"look1" : "A very heavy cell door. The door is locked.",
		"look2" : "A very heavy cell door. The door is open.",
		"keywords" : ["doorYourCell", "door", "cell door", "exit"],
		"takable1" : [False, "You can't take a door!"],
		"movable1" : [False, "You can't move a door!"],
		"kickable1" : [True, "You kick the door. That hurts!"]
		},
	"guard1" : {
		"room" : ["your cell"],
		"look1" : "An angry and nervous man in an ancient military uniform. Not friendly at all. He has a bunch of keys in his hand.",
		"look2" : "A very dead guard, wearing a uniform. There is a bunch of keys in its hand.",
		"look3" : "A very dead guard, wearing a uniform.",
		"keywords" : ["guard1", "guard", "guardian", "sentinel"],
		"takable1" : [False, "Taking an angry guard will do no good..."],
		"takable2" : [False, "Taking a dead body sounds disgusting..."],
		"movable1" : [False, "You can't move the guard."],
		"kickable1" : [False, "You call the guard. When he is near enough you kick him through the door bars. "],
		"kickable2" : [True, "You kick the guard's dead body. That was so macabre..."]
		},
	"keys" : {
		"room" : ["your cell"],
		"look1" : "A bunch keys. These keys should open the dungeon cells.",
		"keywords" : ["keys", "key", "bunch"],
		"takable1" : [True, "You try to catch the guard's keys with your hands. The guard immediately starts shouting loud and two other guards"
		" come to help him. They then kill you."],
		"takable2" : [True, "You take the bunch of keys."],
		"movable1" : [True, "You move the keys. Nothing special happens..."],
		"kickable1" : [True, "You kick the bunch of keys. Nothing special happens..."]
		},
	"dead guard" : {
		"room" : "corridor",
		"look1" : "A very dead guard, wearing a uniform.",
		"look2" : "A very dead and naked guard.",
		"keywords" : ["dead guard", "guard", "dead", "guardian", "body", "corpse"],
		"takable1" : [False, "Taking a dead guard sounds like a horrible idea."],
		"movable1" : [True, "You move the dead guard. Nothing special happens..."],
		"kickable1" : [True, "You kick the guard's dead body. That was so disgusting..."]
		},
	"uniform" : {
		"room" : ["your cell", "corridor"],
		"look1" : "An ancient military uniform. One looks like a true warrior in it.",
		"keywords" : ["uniform", "uniforms", "clothe", "clothes"],
		"takable1" : [False, "You can't take the guard's uniform while he is alive."],
		"takable2" : [False, "You must go out to the corridor to take the guards's uniform."],
		"takable3" : [True, "You take the uniform and put it on. You look now like a dungeon sentinel."],
		"kickable1" : [True, "You kick the uniform."],
		"movable1" : [True, "You move the uniform. Nothing special happens..."]
		},
	"box" : {
		"room" : ["corridor"],
		"look1" : "A heavy wooden box. It feels like it is full with sand.",
		"keywords" : ["box", "wooden"],
		"takable1" : [False, "The box is too heavy to be taken."],
		"movable1" : [True, "You move the box and place it over the round button. The gate to the south opens..."],
		"kickable1" : [True, "You kick the wooden box. That hurts..."]
		},
	"button": {
		"room" : "corridor",
		"look1" : "A metalic round button on the floor.",
		"keywords" : ["button", "round", "metalic"],
		"takable1" : [False, "You can't take the button."],
		"movable1" : [False, "You can't move the button."],
		"kickable1" : [False, "The button can't be pushed down by kicking it."]
		},
	"dead body": {
		"room" : "western cell",
		"look1" : "A dead prisoner's body. It has signs of having being tortured. It has a lighter in a pocket.",
		"keywords" : ["dead body", "dead", "body", "corpse", "prisioner"],
		"takable1" : [False, "You can't take the body."],
		"movable1" : [False, "You can't move the body."],
		"kickable1" : [True, "You kick the dead body. I hope you don't find this funny."]
		},
	"lighter": {
		"room" : "western cell",
		"look1" : "A brown lighter. It works fine.",
		"keywords" : ["lighter", "light"],
		"takable1" : [True, "You take the lighter."],
		"movable1" : [True, "You move the lighter. Nothing special happens..."],
		"kickable1" : [True, "You kick the lighter. That is so absurd..."]
		},
	"wardrobe": {
		"room" : "eastern cell",
		"look1" : "A little wooden wardrobe. It is attached to the wall at a low height. It is locked.",
		"keywords" : ["wardrobe", "wooden", "furniture"],
		"takable1" : [False, "You can't take the wardrobe. It is attached to the wall."],
		"movable1" : [False, "You can't move the wardrobe. It is attached to the wall."],
		"kickable1" : [True, "You kick the wardrobe and it tears apart. There is a leather pouch inside."]
		},
	"pouch": {
		"room" : "eastern cell",
		"look1" : "A leather pouch containing som kind of powders.",
		"keywords" : ["pouch", "powder", "powders", "leather", "poison", "venom"],
		"takable1" : [True, "You take the pouch with the powders inside and hide it behind your back."],
		"movable1" : [True, "You move the pouch. Nothing special happens..."],
		"kickable1" : [True, "You kick the pouch. Nothing happens..."]
		},
	"two guards": {
		"room" : "guard room",
		"look1" : "Two guards drinking beer and playing cards. They are drunk. They believe you are one of them.",
		"look2" : "Two sleeping guards. One of them wears a metalic wristband with a dragon head drawn on it.",
		"look3" : "Two sleeping guards.",
		"keywords" : ["two guards", "guard", "guards", "sleeping", "guardian", "guardians", "sentinel", "sentinels"],
		"takable1" : [False, "You can't take the guards."],
		"movable1" : [False, "You can't move the guards."],
		"kickable1" : [True, "You run to the guards and start kicking them."],
		"kickable2" : [True, "You kick the sleeping guards. They can't feel the pain."]
		},
	"beer jars": {
		"room" : "guard room",
		"look1" : "Two beer jars with beer inside.",
		"keywords" : ["beer jars", "beer", "jar", "jars"],
		"takable1" : [True, "You take the beer jars. This annoys the guards a lot. They then realize who you really are and kill you."],
		"takable2" : [True, "You take the beer jars."],
		"movable1" : [True, "You move the beer jars. This annoys the guards a lot. They then realize who you really are and kill you."],
		"movable2" : [True, "You move the beer jars. Nothing special happens..."],
		"kickable1" : [True, "You kick the beer jars so that the beer falls on the guards. They get extremely upset. They then realize who you really are and kill you."],
		"kickable2" : [True, "You kick the beer jars so that they crash into the floor, spreading out the beer."]
		},
	"wristband": {
		"room" : "guard room",
		"look1" : "A metalic wristband with a dragon head drawn on it.",
		"keywords" : ["wristband", "dragon", "head", "metalic", "bracelet"],
		"takable1" : [True, "You try to take the wristband from the guard. They see this as an attack. They then realize who you really are and kill you."],
		"takable2" : [True, "You take the wristband"],
		"movable1" : [False, "You can't move the wristband."],
		"kickable1" : [False, "You can't kick the wristband."]
		},
	"bench": {
		"room" : "guard room",
		"look1" : "A robust wooden bench.",
		"keywords" : ["bench", "wooden"],
		"takable1" : [False, "You can't take the bench."],
		"movable1" : [True, "You start moving the bench. The guards react to this and when they look at you they "
		"realise that you are a prisioner."],
		"movable2" : ["You move the bench so that it no longer blocks the door to the south."],
		"kickable1" : [True, "You kick the bench. It hurts..."]
		},
	"wardrobe south": {
		"room" : "south room",
		"look1" : "A robust wooden wardrobe. Its doors are closed.",
		"look2" : "A robust wooden wardrobe. There is an unlit torch.",
		"keywords" : ["wardrobe south", "wardrobe", "wooden", "furniture"],
		"takable1" : [False, "You can't take the wardrobe."],
		"movable1" : [False, "You can't move the wardrobe."],
		"kickable1" : [True, "You kick the wardrobe. It hurts..."]
		},
	"torch": {
		"room" : "south room",
		"look1" : "An unlit torch.",
		"look2" : "A torch with a shining flame.",
		"keywords" : ["torch"],
		"takable1" : [True, "You take the torch."],
		"movable1" : [True, "You move the torch. Nothing special happens..."],
		"kickable1" : [True, "You kick the torch. Nothing special happens..."]
		},
	"spikes trap": {
		"room" : "darkness",
		"look1" : "A system of sharp spikes installed on the floor.",
		"look2" : "A deactivated trap. Not dangerous anymore.",
		"keywords" : ["spikes trap", "trap", "spike", "spikes"],
		"takable1" : [True, "You try to take the spikes, but your body falls on them. You die."],
		"takable2" : [False, "You can't take the trap."],
		"movable1" : [True, "You try to move the spikes, but your body falls on them. You die."],
		"movable2" : [False, "You can't move the trap."],
		"kickable1" : [True, "You try to kick the spikes, but your body falls on them. You die."],
		"kickable2" : [False, "You can't kick the trap."]
		},
	"trap button": {
		"room" : "darkness",
		"look1" : "A button the size of your foot. It should deactivate the spikes.",
		"keywords" : ["trap button", "button"],
		"takable1" : [False, "You can't take the button."],
		"movable1" : [False, "You can't move the button."],
		"kickable1" : [True, "You kick the button to push it down. It deactivates the spikes trap."],
		},
	"final gate": {
		"room" : "the yard",
		"look1" : "It is the gate to freedom. The gate has no keyhole,"
		"but instead there is a kind of magnetic opening mechanism at its center, with a headless dragon body drawn in it. It seems "
		"that the drawing must be completed with a head for the gate to open.",
		"keywords" : ["final gate", "final", "gate", "door"],
		"takable1" : [False, "You can't take the final gate."],
		"movable1" : [False, "You can't move the final gate."],
		"kickable1" : [True, "You kick the final gate. That hurts..."],
		},
	"TicTacToe device": {
		"room" : "TicTacToe",
		"look1" : "A big touch screen inviting you to play TicTacToe against an evil electronic brain.",
		"keywords" : ["TicTacToe device", "TicTacToe", "device", "screen", "touch", "electronic"],
		"takable1" : [False, "You can't take the TicTacToe device."],
		"movable1" : [False, "You can't move the TicTacToe device."],
		"kickable1" : [True, "You kick the TicTacToe device. That hurts..."],
		},
	}
