#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import adventure

def tictactoe():
	board = [0, 1, 2,
			 3, 4, 5,
			 6, 7, 8]

	boardReset = [0, 1, 2,
			 3, 4, 5,
			 6, 7, 8]
	# Dictionary that stores possible win combinations:
	winDict = {
		"line1" : [0, 1, 2],
		"line2" : [3, 4, 5],
		"line3" : [6, 7, 8],
		"col1" : [0, 3, 6],
		"col2" : [1, 4, 7],
		"col3" : [2, 5, 8],
		"dia1" : [0, 4, 8],
		"dia2" : [2, 4, 6]
	}

	winDictReset = {
		"line1" : [0, 1, 2],
		"line2" : [3, 4, 5],
		"line3" : [6, 7, 8],
		"col1" : [0, 3, 6],
		"col2" : [1, 4, 7],
		"col3" : [2, 5, 8],
		"dia1" : [0, 4, 8],
		"dia2" : [2, 4, 6]
	}

	def show():
		print(chr(27) + "[2J" + chr(27) + "[;H") # Clears the console
		print("\n")
		print(board[0], "|", board[1], "|", board[2])
		print("---------") 
		print(board[3], "|", board[4], "|", board[5])
		print("---------") 
		print(board[6], "|", board[7], "|", board[8])
		print("---------") 
		print("\n") 
		

	show()

	rounds = 0

	while rounds < 9:
		print(winDict)
		print("Round:", rounds)
		for win in winDict:
			if winDict[win] == ["x", "x", "x"]:
				adventure.playerWins()
			elif winDict[win] == ["o", "o", "o"]:
				print("\n")
				printw("You lose the match against the evil electronic brain. The TicTacToe chamber begins")
				(" to shake until it explodes with you inside. You are now dead.")
				adventure.gameOver()
		inp = input("\nSYour turn: ")
		inp = int(inp)

		if board[inp] != "x" and board[inp] != "o":
			board[inp] = "x"
			rounds += 1
			for x_item in winDict:
				cc = -1
				for v in winDict[x_item]:
					cc += 1
					if v == inp:
						winDict[x_item][cc] = "x"


			while True:
				random.seed()
				cpu = random.randint(0, 8)

				if board[cpu] != "o" and board[cpu] != "x":
					board[cpu] = "o"
					rounds += 1
					for x_item in winDict:
						cc = -1
						for v in winDict[x_item]:
							cc += 1
							if v == cpu:
								winDict[x_item][cc] = "o"

					break
		else:
			print("This spot is taken!")
		show() 
	board = boardReset
	winDict = winDictReset

