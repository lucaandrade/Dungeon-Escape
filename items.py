#!/usr/bin/env python3
# -*- coding: utf-8 -*-
items = {
	"corpse1" : {
		"room" : "your cell",
		"look1" : "A very rotten man's corpse. The corpse has a belt on.",
		"look2" : "A very rotten man's corpse.",
		"keywords" : ["corpse1", "corpse", "body", "dead", "cadaver", "rotten"],
		"takable" : [False, "Taking a rotten corpse doesn't sound like a good idea."],
		"movable" : [True, "You move the corpse. Nothing special happens."],
		"kickable" : [True, "You kick the corpse. That was so macabre..."]
		},
	"belt" : {
		"room" : "your cell",
		"look1" : "A leather belt. Hard and robust.",
		"takable" : [True, "Without any consideration to the dead body, you take the belt and hide it behind your back."],
		"keywords" : ["belt"],
		"movable" : [True, "That is absurd."],
		"kickable" : [True, "You kick the belt. You should take care of it instead."]
		},
	"doorYourCell" : {
		"room" : "your cell",
		"look1" : "A very heavy cell door. The door is locked.",
		"look2" : "A very heavy cell door. The door is open.",
		"keywords" : ["doorYourCell", "door", "cell door", "exit"],
		"takable" : [False, "You can't take a door!"],
		"movable" : [False, "You can't move a door!"],
		"kickable" : [True, "You kick the door. That hurts!"]
		},
	"guard1" : {
		"room" : ["your cell"],
		"look1" : "An angry and nervous man in an ancient military uniform. Not friendly at all. He has a bunch of keys in his hand.",
		"look2" : "A very dead guard, wearing a uniform. There is a bunch of keys in its hand.",
		"look3" : "A very dead guard, wearing a uniform.",
		"keywords" : ["guard1", "guard", "guardian", "sentinel"],
		"takable" : [False, "Taking an angry guard will do no good."],
		"movable" : [False, "You can't move the guard."],
		"kickable" : [True, "You kick the guard's dead body. That was so macabre..."]
		},
	"keys" : {
		"room" : ["your cell"],
		"look1" : "A bunch keys. These keys should open the dungeon cells.",
		"keywords" : ["keys", "key", "bunch"],
		"takable" : [True, "You take the bunch of keys."],
		"movable" : [True, "You move the keys. Nothing special happens..."]
		},
	"dead guard" : {
		"room" : "corridor",
		"look1" : "A very dead guard, wearing a uniform.",
		"look2" : "A very dead and naked guard.",
		"keywords" : ["dead guard", "guard", "dead", "guardian", "body", "corpse"],
		"takable" : [False, "Taking a dead guard sounds like a horrible idea."],
		"movable" : [True, "You move the dead guard. Nothing special happens..."],
		"kickable" : [True, "You kick the guard's dead body. That was so disgusting..."]
		},
	"uniform" : {
		"room" : ["your cell", "corridor"],
		"look1" : "An ancient military uniform. One looks like a true warrior in it.",
		"keywords" : ["uniform", "uniforms", "clothe", "clothes"],
		"takable" : [True, "You take the uniform and put it on. You look now like a dungeon sentinel."],
		"kickable" : [True, "You kick the uniform."],
		"movable" : [True, "You move the uniform. Nothing special happens..."]
		},
	"box" : {
		"room" : ["corridor"],
		"look1" : "A heavy wooden box. It feels like it is full with sand.",
		"keywords" : ["box", "wooden"],
		"takable" : [False, "The box is too heavy to be taken."],
		"movable" : [True, "You move the box and place it over the round button. The gate to the south opens..."],
		"kickable" : [True, "You kick the wooden box. That hurts..."]
		},
	"button": {
		"room" : "corridor",
		"look1" : "A metalic round button on the floor.",
		"keywords" : ["button", "round", "metalic"],
		"takable" : [False, "You can't take the button."],
		"movable" : [False, "You can't move the button."],
		"kickable" : [False, "The button can't be pushed down by kicking it."]
		},
	"dead body": {
		"room" : "western cell",
		"look1" : "A dead prisoner's body. It has signs of having being tortured. It has a lighter in a pocket.",
		"keywords" : ["dead", "body", "corpse", "prisioner"],
		"takable" : [False, "You can't take the body."],
		"movable" : [False, "You can't move the body."],
		"kickable" : [True, "You kick the dead body. I hope you don't find this funny."]
		},
	"lighter": {
		"room" : "western cell",
		"look1" : "A brown lighter. It works fine.",
		"keywords" : ["lighter", "light"],
		"takable" : [True, "You take the lighter."],
		"movable" : [True, "You move the lighter. Nothing special happens..."],
		"kickable" : [True, "You kick the lighter. That is so absurd..."]
		},
	"wardrobe": {
		"room" : "eastern cell",
		"look1" : "A little wooden wardrobe. It is attached to the wall at a low height. It is locked.",
		"keywords" : ["wardrobe", "wooden", "furniture"],
		"takable" : [False, "You can't take the wardrobe. It is attached to the wall."],
		"movable" : [False, "You can't move the wardrobe. It is attached to the wall."],
		"kickable" : [True, "You kick the wardrobe and it tears apart. There is a leather pouch inside."]
		},
	"pouch": {
		"room" : "eastern cell",
		"look1" : "A leather pouch containing som kind of powders.",
		"keywords" : ["pouch", "powder", "powders", "leather", "poison", "venom"],
		"takable" : [True, "You take the pouch with the powders inside and hide it behind your back."],
		"movable" : [True, "You move the pouch. Nothing special happens..."],
		"kickable" : [True, "You kick the pouch. Nothing happens..."]
		}
	}
