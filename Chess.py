import sys;
from random import *;
from Pieces import *;
from EnemyAI import *;

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
	
	white_king_pos = (7,4);
	black_king_pos = (0,4);
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
	print("  -----------------------------------");
	for i in range(0,8):
		string = str(8 - i) + " | ";
		for j in range(0,8):
			if(board[i][j] == None):
				string += "--- ";
			else:
				string += ("" + repr(board[i][j]) + " ");
		print(string + "|");
	print("  -----------------------------------");
	print("     A   B   C   D   E   F   G   H");


# Check for jepordy/check
def analyze_check():
	global white_king_pos;
	global black_king_pos;
	global white_check;
	global black_check;
	
	white_check = False;
	black_check = False;
	for x in range(0,8):
		for y in range(0,8):
			if(board[x][y] != None and board[x][y].to_string() == "king" and board[x][y].team == "white"):
				white_king_pos = (x,y);
			elif(board[x][y] != None and board[x][y].to_string() == "king" and board[x][y].team == "black"):
				black_king_pos = (x,y);
				
	for x in range(0,8):
		for y in range(0,8):
			if(board[x][y] != None and board[x][y].team == "black" and white_king_pos in board[x][y].get_moves(board,(x,y))):
				white_check = True;
			elif(board[x][y] != None and board[x][y].team == "white" and black_king_pos in board[x][y].get_moves(board,(x,y))):
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
	board[pos1[0]][pos1[1]] = None;
	analyze_check();
	
	# check for invalid move due to putting oneself in check; revert move if necessary
	if((player_team == "white" and white_check == True) or (player_team == "black" and black_check == True)):
		revert_last_move();
		print("Illegal move: You cannot be in check!");
		return False;
	
	# promote pawns if any reach opposite side
	if(board[pos2[0]][pos2[1]].to_string() == "pawn" and pos2[0] == 0):
		invalid_response = True;
		while(invalid_response):
			response = raw_input("Enter a piece to promote pawn to: ");
			if(response.lower() == "queen" or response.lower() == "q"):
				board[pos2[0]][pos2[1]] = Queen(player_team);
				invalid_response = False;
			elif(response.lower() == "rook" or response.lower() == "r"):
				board[pos2[0]][pos2[1]] = Rook(player_team);
				invalid_response = False;
			elif(response.lower() == "knight" or response.lower() == "k" or response.lower() == "n"):
				board[pos2[0]][pos2[1]] = Knight(player_team);
				invalid_response = False;
			elif(response.lower() == "bishop" or response.lower() == "b"):
				board[pos2[0]][pos2[1]] = Bishop(player_team);
				invalid_response = False;
			else:
				print("");
				print("XX Invalid piece name (queen,bishop,rook,knight) XX");
			
	print(validation + "\n");
	return True;


# check for checkmate / stalemate
def checkmate():
	if(player_team == "white" and black_check == True and can_move_any("black") == False):
		print( "Checkmate! You Win!");
		return True;
	if(player_team == "black" and white_check == True and can_move_any("white") == False):
		print( "Checkmate! You Win!");
		return True;
	if(player_team == "white" and white_check == True and can_move_any("white") == False):
		print( "Checkmate! You Lose!");
		return True;
	if(player_team == "black" and black_check == True and can_move_any("black") == False):
		print( "Checkmate! You Lose!");
		return True;
	if(black_check == False and can_move_any("black") == False):
		print( "Stalemate!");
		return True;
	if(white_check == False and can_move_any("white") == False):
		print( "Stalemate!");
		return True;
	return False;


# returns true if the given team has ANY valid moves available
def can_move_any(tteam):
	for i in range(0,8):
		for j in range(0,8):
			if(board[i][j] != None and board[i][j].team == tteam):
				moves = board[i][j].get_moves(board,(i,j));
				for x in range(0,len(moves)):
					piece_taken = board[moves[x][0]][moves[x][1]];
					board[moves[x][0]][moves[x][1]] = board[i][j];
					board[i][j] = None;
					analyze_check();
					board[i][j] = board[moves[x][0]][moves[x][1]];
					board[moves[x][0]][moves[x][1]] = piece_taken;
					if(tteam == "white" and white_check == False):
						return True;
					elif(tteam == "black" and black_check == False):
						return True;
	return False;


# attempt to perform a castle move, return false if failed
def castle_move(tteam,input_move):
	input_arr = input_move.split();
	if(len(input_arr) != 2 or input_arr[0].lower() != "castle" or (input_arr[1].lower() != "l" and input_arr[1].lower() != "r")):
		print("Invalid move format entered, please retry");
		return False;
	if(input_arr[1].lower() == "l" and (board[7][0] == None or board[7][0].to_string() != "rook" or board[7][0].has_moved)):
		print("Illegal move: your rook has already moved");
		return False;
	if(input_arr[1].lower() == "r" and (board[7][7] == None or board[7][7].to_string() != "rook" or board[7][7].has_moved)):
		print("Illegal move: your rook has already moved");
		return False;
	if(board[7][4] == None or board[7][4].to_string() != "king" or board[7][4].has_moved):
		print("Illegal move: your king has already moved");
		return False;
	analyze_check();
	if(white_check):
		print("Illegal move: your king is in check");
		return False;
	if(input_arr[1].lower() == "l" and (board[7][1] != None or board[7][2] != None or board[7][3] != None)):
		print("Illegal move: pieces are in the way");
		return False;
	if(input_arr[1].lower() == "r" and (board[7][5] != None or board[7][6] != None)):
		print("Illegal move: pieces are in the way");
		return False;
	
	if(input_arr[1].lower() == "r"):
		board[7][5] = King(player_team);
		board[7][4] = None;
		analyze_check();
		if(white_check):
			board[7][4] = King(player_team);
			board[7][5] = None;
			print("Illegal move: can't move though jepordized spaces");
			return False;
		board[7][6] = King(player_team);
		board[7][5] = Rook(player_team);
		board[7][7] = None;
		analyze_check();
		if(white_check):
			board[7][4] = King(player_team);
			board[7][6] = None;
			board[7][7] = Rook(player_team);
			board[7][5] = None;
			print("Illegal move: can't put yourself in check");
			return False;
		print("Move successful!");
		return True;
	
	if(input_arr[1].lower() == "l"):
		board[7][3] = King(player_team);
		board[7][4] = None;
		analyze_check();
		if(white_check):
			board[7][4] = King(player_team);
			board[7][3] = None;
			print("Illegal move: can't move though jepordized spaces");
			return False;
		board[7][2] = King(player_team);
		board[7][3] = Rook(player_team);
		board[7][0] = None;
		analyze_check();
		if(white_check):
			board[7][4] = King(player_team);
			board[7][0] = Rook(player_team);
			board[7][2] = None;
			board[7][3] = None;
			print("Illegal move: can't put yourself in check");
			return False;
		print("Move successful!");
		return True;


# Main Process
def main():
	
	endgame = False;
	initialize();
	print("");
	print("Random chess engine: by Jack Pietrok");
	print("------------------------------------");
	print("+ Make moves by entering in format: A# B#");
	print("+ (an example move would be 'C2 D4')");
	print("+ To make a 'castling' move, enter 'castle l' or 'castle r' for left and right sides respectively")
	print("");
	
	while(not endgame):
		display_board(board);
		player_move = raw_input("\nPlease enter your move:\n");
		print("");
		if(player_move.find("castle") > -1):
			if(not castle_move(player_team,player_move)):
				continue;
		else:	
			if(not validate_input(player_move)):
				continue;
			
			pos1 = get_coordinates(player_move.split(" ")[0]);
			pos2 = get_coordinates(player_move.split(" ")[1]);
			if(not move_piece(pos1,pos2)):
				continue;
			
			# At this point the player's move has been successfully completed
			board[pos2[0]][pos2[1]].has_moved = True;
		
		analyze_check();
		if(checkmate()):
			display_board(board);
			endgame = True;
			break;
		
		# Enemy get_move function goes here
		#--------------------------------------------
		enemy_move = get_move_minimax(enemy_team);
		#--------------------------------------------
		
		board[enemy_move[1][0]][enemy_move[1][1]] = board[enemy_move[0][0]][enemy_move[0][1]];
		board[enemy_move[0][0]][enemy_move[0][1]] = None;
		
		if(board[enemy_move[1][0]][enemy_move[1][1]].to_string() == "pawn" and enemy_move[1][0] == 7):
			
			# Enemy promotion function goes here
			#--------------------------------------------
			enemy_promotion = "queen";
			#--------------------------------------------
			
			if(enemy_promotion.lower() == "queen" or enemy_promotion.lower() == "q"):
				board[enemy_move[1][0]][enemy_move[1][1]] = Queen(enemy_team);
				invalid_response = False;
			elif(enemy_promotion.lower() == "rook" or enemy_promotion.lower() == "r"):
				board[enemy_move[1][0]][enemy_move[1][1]] = Rook(enemy_team);
				invalid_response = False;
			elif(enemy_promotion.lower() == "knight" or enemy_promotion.lower() == "k" or response.lower() == "n"):
				board[enemy_move[1][0]][enemy_move[1][1]] = Knight(enemy_team);
				invalid_response = False;
			elif(enemy_promotion.lower() == "bishop" or enemy_promotion.lower() == "b"):
				board[enemy_move[1][0]][enemy_move[1][1]] = Bishop(enemy_team);
				invalid_response = False;
			
		
		board[enemy_move[1][0]][enemy_move[1][1]].has_moved = True;
		print("+ Enemy moves " + board[enemy_move[1][0]][enemy_move[1][1]].to_string() + " to " + get_stringform(enemy_move[1]))
		
		analyze_check();
		if(checkmate()):
			display_board(board);
			endgame = True;
			break;
		
		if((white_check and player_team == "white") or (black_check and player_team == "black")):
			print("Check!")


# Call Main
main();