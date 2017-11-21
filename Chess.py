import sys;
from Pieces import *;


# Initialize Game Stats and Board
def initialize():
	player_team = "white";
	enemy_team = "black";
	white_check = False;
	black_check = False;
	
	# TODO : expand this functionality to an "undo last move" stack
	# last_move : [ (row,col) , (row,col) , piece_taken ]  OR  None
	last_move = None;
	
	white_king_pos = (0,4);
	black_king_pos = (7,4);
	board = [[ Rook("black"), Kight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Kight("black"), Rook("black")],
			 [ Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
			 [ None, None, None, None, None, None, None, None],
			 [ None, None, None, None, None, None, None, None],
			 [ None, None, None, None, None, None, None, None],
			 [ None, None, None, None, None, None, None, None],
			 [ Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white")],
			 [ Rook("white"), Kight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Kight("white"), Rook("white")]];
	

# Display the board and Stats
def display_board():
	for i in range(0,8):
		print(board[i]);


# Check for jepordy/check
def analyze_check(self):
	white_check = False;
	black_check = False;
	for x in range(0,7):
		for y in range(0,7):
			if(board[x][y] != None and board[x][y].team == "black" and white_king_pos in board[x][y].get_moves()):
				white_check = True;
			elif(board[x][y] != None and board[x][y].team == "white" and black_king_pos in board[x][y].get_moves()):
				black_check = True;


# check input to make sure the moves enetered are valid
def validate_input(self,string):
	if(not(string.split().length == 2)):
		print("Invalid move format entered, please retry.");
		return False;
	col = string.lower().split()[0];
	row = string.lower().split()[1];
	if(ord(col) < 97 or ord(col) > 104):
		print("Invalid move format entered, please retry.");
		return False;
	if(int(row) < 1 or int(row) > 8):
		print("Invalid move format entered, please retry.");
		return False;
	return True;
	

# convert move from string-form (a4, b3, etc) to tuple coordinates
# this function assumes the string-form is a valid entry
def get_coordinates(self,string):
	col = string.lower().split()[0];
	row = string.lower().split()[1];
	

# Check if a move is valid, and return "" if move is good (check/checkmate is checked afterwards)
def validate_move(self,pos1,pos2):
	piece = board[pos1[0]][pos1[1]];
	if(piece == None):
		return "No piece exists at " + pos1 + "!";
	elif(piece.team != player_team):
		return "Piece at " + pos1 + " is not on your team!";
	elif(not (pos2 in piece.get_moves(board,pos1))):
		return "Illegal move: This piece cannot move to " + pos2;
	else:
		return "Move successful";


# Revert the last move made (by either team)
def revert_last_move(self):
	if(last_move == None):
		print("ERROR: no last move");
		return;
	else:
		board[last_move[0][0]][last_move[0][1]] = board[last_move[1][0]][last_move[1][1]];
		if(last_move[2] != None):
			board[last_move[1][0]][last_move[1][1]] = last_move[2];


# Attempt to move a piece, and return boolean move success
def move_piece(self,pos1,pos2):
	
	# check for valid move
	validation = validate_move(pos1,pos2);
	if(validation != "Move successful"):
		print(validation);
		return False;
	analyze_check();
	
	# check for invalid move due to putting oneself in check; revert move if necessary
	if((player_team == "white" and white_check == True) or (player_team == "black" and black_check == True)):
		revert_last_move();
		print("Illegal move: You cannot be in check!");
		return False;
	
	print(validation);
	return True;


# check for checkmate / stalemate
# TODO : handle stalemate
def checkmate(self):
	if(player_team == "white" and black_check == True and board[black_king_pos[0]][black_king_pos[1]].get_moves(board,black_king_pos).length == 0):
		print( "Checkmate! You Win!");
		return True;
	if(player_team == "black" and white_check == True and board[white_king_pos[0]][white_king_pos[1]].get_moves(board,white_king_pos).length == 0):
		print( "Checkmate! You Win!");
		return True;
	if(player_team == "white" and white_check == True and board[white_king_pos[0]][white_king_pos[1]].get_moves(board,white_king_pos).length == 0):
		print( "Checkmate! You Lose!");
		return True;
	if(player_team == "black" and black_check == True and board[black_king_pos[0]][black_king_pos[1]].get_moves(board,black_king_pos).length == 0):
		print( "Checkmate! You Lose!");
		return True;
	return False;


# Main Process
def main():
	endgame = False;
	initialize();
	display_board();
	while(not endgame):
		print("moves should be entered in traditional form: A# B#");
		player_move = input("Please enter your move:");
		if(validate_input(player_move)):
			continue;
		if(not move_piece(player)):
			continue;
		
		if(checkmate()):
			endgame = True;
			break;
		
		# TODO: run enemy AI move
		
		if((white_check and player_team == "white") or (black_check and player_team == "black")):
			print("Check!")


# Call Main
main();