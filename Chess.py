import sys;
from Piece import *;


# variable instantiation
board = [];
white_check = False;
black_check = False;
white_king_pos;
black_king_pos;

# Initialize Game Stats and Board
def initialize():
	white_check = False;
	black_check = False;
	white_king_pos = (0,4);
	black_king_pos = (7,4);
	black_king_pos;
	board = [[ Rook("black"), Kight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Kight("black"), Rook("black")],
			 [ Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
			 [ None, None, None, None, None, None, None, None],
			 [ None, None, None, None, None, None, None, None],
			 [ None, None, None, None, None, None, None, None],
			 [ None, None, None, None, None, None, None, None],
			 [ Rook("white"), Kight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Kight("white"), Rook("white")],
			 [ Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white")]]
	

# Display the board and Stats
def display_board():
	for i in range(0,7):
		for j in range(0,7):
			print(board[i][j]);


# Check for jepordy/checkmate
def analyze_check(self):
	white_check = False;
	black_check = False;
	for x in range(0,7):
		for y in range(0,7):
			if(board[x][y] != None and board[x][y].team == "black" and white_king_pos in board[x][y].get_moves()):
				white_check = True;
			elif(board[x][y] != None and board[x][y].team == "white" and black_king_pos in board[x][y].get_moves()):
				black_check = True;


# Main Process
def main():
	while();



# Call Main
main();