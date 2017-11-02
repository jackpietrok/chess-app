import sys;
from Piece import *;


# variable instantiation
board = [];


# Initialize Game Stats and Board
def initialize():
	board = [[ Rook("black"), Kight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Kight("black"), Rook("black")],
			 [ Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
			 [ null, null, null, null, null, null, null, null],
			 [ null, null, null, null, null, null, null, null],
			 [ null, null, null, null, null, null, null, null],
			 [ null, null, null, null, null, null, null, null],
			 [ Rook("white"), Kight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Kight("white"), Rook("white")],
			 [ Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white")]]
	

# Display the board and Stats
def display_board():
	for i in range(0,7):
		for j in range(0,7):
			print(board[i][j]);

# Check for jepordy/checkmate
def in_check():


# Main Process
def main():
	while()



# Call Main
main();