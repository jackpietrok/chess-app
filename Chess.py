import sys;
from Pieces import *;

player_team = "white";
enemy_team = "black";
white_check = False;
black_check = False;
last_move = None;
white_king_pos = (0,4);
black_king_pos = (7,4);
board = [];

# Initialize Game Stats and Board
def initialize():
	global player_team;
	global enemy_team;
	global white_check;
	global black_check;
	global last_move;
	global white_king_pos;
	global black_king_pos;
	global board;
	
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
def display_board(board):
	for i in range(0,8):
		print(board[i]);


# Check for jepordy/check
def analyze_check():
	white_check = False;
	black_check = False;
	for x in range(0,7):
		for y in range(0,7):
			if(board[x][y] != None and board[x][y].team == "black" and white_king_pos in board[x][y].get_moves()):
				white_check = True;
			elif(board[x][y] != None and board[x][y].team == "white" and black_king_pos in board[x][y].get_moves()):
				black_check = True;


# check input to make sure the moves enetered are valid
def validate_input(string):
	if(not(len(string.split(" ")) == 2)):
		print("Invalid move format entered, please retry.");
		return False;
	
	for x in range(2):
		str_move = string.split(" ")[x];
		if(len(list(str_move)) != 2):
			print("Invalid move format entered, please retry.");
			return False;
		col = list(str_move.lower())[0];
		row = list(str_move.lower())[1];
		if(ord(col) < 97 or ord(col) > 104):
			print("Invalid move format entered, please retry.");
			return False;
		if(int(row) < 1 or int(row) > 8):
			print("Invalid move format entered, please retry.");
			return False;
		
	return True;
	

# convert move from string-form (a4, b3, etc) to tuple coordinates
# this function assumes the string-form is a valid entry
def get_coordinates(string):
	col = list(string.lower())[0];
	row = list(string.lower())[1];
	col_index = ord(col) - 97;
	row_index = 8 - (int(row));
	return (row_index,col_index);


# convert move from tuple coordinates to string form
# this function assumes the coordinates are valid
def get_stringform(coords):
	col = coords[1];
	row = coords[0];
	return "" + chr(97 + col) + str(8 - row);
	

# Check if a move is valid, and return "" if move is good (check/checkmate is checked afterwards)
def validate_move(pos1,pos2):
	piece = board[pos1[0]][pos1[1]];
	if(piece == None):
		return "No piece exists at " + get_stringform(pos1) + "!";
	elif(piece.team != player_team):
		return "Piece at " + get_stringform(pos1) + " is not on your team!";
	elif(not (pos2 in piece.get_moves(board,pos1))):
		return "Illegal move: This piece cannot move to " + get_stringform(pos2);
	else:
		return "Move successful";


# Revert the last move made (by either team)
def revert_last_move():
	if(last_move == None):
		print("ERROR: no last move");
		return;
	else:
		board[last_move[0][0]][last_move[0][1]] = board[last_move[1][0]][last_move[1][1]];
		if(last_move[2] != None):
			board[last_move[1][0]][last_move[1][1]] = last_move[2];


# Attempt to move a piece, and return boolean move success
def move_piece(pos1,pos2):
	
	# check for valid move
	validation = validate_move(pos1,pos2);
	if(validation != "Move successful"):
		print(validation);
		return False;
	board[pos2[0]][pos2[1]] = board[pos1[0]][pos1[1]];
	board[pos2[0]][pos2[1]] = None;
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
def checkmate():
	if(player_team == "white" and black_check == True and len(board[black_king_pos[0]][black_king_pos[1]].get_moves(board,black_king_pos)) == 0):
		print( "Checkmate! You Win!");
		return True;
	if(player_team == "black" and white_check == True and len(board[white_king_pos[0]][white_king_pos[1]].get_moves(board,white_king_pos)) == 0):
		print( "Checkmate! You Win!");
		return True;
	if(player_team == "white" and white_check == True and len(board[white_king_pos[0]][white_king_pos[1]].get_moves(board,white_king_pos)) == 0):
		print( "Checkmate! You Lose!");
		return True;
	if(player_team == "black" and black_check == True and len(board[black_king_pos[0]][black_king_pos[1]].get_moves(board,black_king_pos)) == 0):
		print( "Checkmate! You Lose!");
		return True;
	return False;


# make a random move of those available
# move returned is in form ((row1,col1),(row2,col2))
def get_random_move(team):
	pieces = [];
	for i in range(8):
		for j in range(8):
			if(board[i][j] != None and board[i][j].team == team and len(board[i][j].get_moves(board,(i,j))) > 0):
				pieces += (i,j);
	rand_piece = randint(0,len(pieces) - 1);
	moves = board[pieces[rand_piece][0]][pieces[rand_piece][1]].get_moves(board,(i,j));
	
	move_arr = [];
	for x in range(0,len(moves)):
		piece_taken = board[moves[x][0]][moves[x][1]];
		board[moves[x][0]][moves[x][1]] = board[pieces[rand_piece][0]][pieces[rand_piece][1]];
		board[pieces[rand_piece][0]][pieces[rand_piece][1]] = None;
		analyze_check();
		if(not ((enemy_team == "white" and white_check) or (enemy_team == "black" and black_check))):
			move_arr += moves[x];
		board[pieces[rand_piece][0]][pieces[rand_piece][1]] = board[moves[x][0]][moves[x][1]];
		board[moves[x][0]][moves[x][1]] = piece_taken;
	
	rand_move = randint(0,len(move_arr));
	return ((pieces[rand_piece][0] , pieces[rand_piece][1]) , move_arr[rand_move]);


# Main Process
def main():
	
	endgame = False;
	initialize();
	display_board(board);
	
	while(not endgame):
		print("moves should be entered in traditional form: A# B#");
		player_move = raw_input("Please enter your move:\n");
		if(not validate_input(player_move)):
			continue;
		
		pos1 = get_coordinates(player_move.split(" ")[0]);
		pos2 = get_coordinates(player_move.split(" ")[1]);
		if(not move_piece(pos1,pos2)):
			continue;
		
		# At this point the player's move has been successfully completed
		board[pos2[0]][pos2[1]].has_moved = True;
		
		if(checkmate()):
			endgame = True;
			break;
		
		# Enemy move function goes here
		enemy_move = get_random_move(enemy_team,board);
		
		board[enemy_move[1][0]][enemy_move[1][1]] = board[enemy_move[0][0]][enemy_move[0][1]];
		board[enemy_move[0][0]][enemy_move[0][1]] = None;
		
		if(checkmate()):
			endgame = True;
			break;
		
		if((white_check and player_team == "white") or (black_check and player_team == "black")):
			print("Check!")


# Call Main
main();