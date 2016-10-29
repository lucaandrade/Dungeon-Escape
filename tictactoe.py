#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import textwrap
import adventure

board = [0, 1, 2,
		 3, 4, 5,
		 6, 7, 8]

winner = ""

# Dictionary that stores all possible win combinations:
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


def printw(txt):
	"""A textwrap for a nicer looking in the game text"""
	print(textwrap.fill(txt, 50))

def gameStart():
	gameLoop()

def checkWinner():
	"""Iterates through winDict to check if someone has won"""
	global winner
	for win in winDict:
		if winDict[win] == ["x", "x", "x"]:
			winner = "player"
			adventure.LOC = "freedom"
			adventure.roomInfo()
			adventure.gameOver()
		elif winDict[win] == ["o", "o", "o"]:
			winner = "cpu"
			printw("You lose against the evil brain. The TicTacToe chamber explodes with you inside. You are dead...")
			adventure.gameOver()
	return winner

def drawBoard():
	"""Draws the game board"""
	print(chr(27) + "[2J" + chr(27) + "[;H") # Clears the console
	print("\n")
	print(board[0], "|", board[1], "|", board[2])
	print("---------") 
	print(board[3], "|", board[4], "|", board[5])
	print("---------") 
	print(board[6], "|", board[7], "|", board[8])
	print("---------") 
	print("\n") 
	print("Type a number (0-8) (x: you / o: CPU\n")

def gameLoop():
	global board, winDict
	drawBoard()
	while True:
		if 0 not in board and 1 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board:
			printw("You lose against the evil brain. The TicTacToe chamber explodes with you inside. You are dead...")
			adventure.gameOver()
		inp = input("Your turn: >")
		inp = int(inp) 
		if board[inp] != "x" and board[inp] != "o":
			board[inp] = "x"
			for x_item in winDict:
				cc = -1
				for v in winDict[x_item]:
					cc += 1
					if v == inp:
						winDict[x_item][cc] = "x"
		while True:
			if 0 not in board and 1 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board:
				printw("You lose against the evil brain. The TicTacToe chamber explodes with you inside. You are dead...")
				adventure.gameOver()
			random.seed()
			cpu = random.randint(0, 8) 
			if board[cpu] != "o" and board[cpu] != "x":
				board[cpu] = "o"
				for o_item in winDict:
					cc = -1
					for v in winDict[o_item]:
						cc += 1
						if v == cpu:
							winDict[o_item][cc] = "o"
				break
		drawBoard()
		checkWinner()


if __name__ == '__main__':
	gameStart()