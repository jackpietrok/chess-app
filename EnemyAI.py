import sys;
from copy import *;

# make a random move of those available
# # move returned is in form ((row1,col1),(row2,col2))
def get_random_move(tteam):
	dic = get_all_moves(tteam);
	rand_key = choice(dic.keys());
	rand_item = choice(dic[rand_key])
	return (rand_key,rand_item);


# Check for jepordy/check
def analyze_check(board):
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


# returns dictionary of all possible moves by given team
# format : {pos1 : pos2_1 , pos2_2 , pos2_3 , etc}
def get_all_moves(tteam):
	dic = {};
	for i in range(8):
		for j in range(8):
			if(board[i][j] != None and board[i][j].team == tteam and len(board[i][j].get_moves(board,(i,j))) > 0):
				moves = board[i][j].get_moves(board,(i,j));
				dic[(i,j)] = [];
				for x in range(0,len(moves)):
					piece_taken = board[moves[x][0]][moves[x][1]];
					board[moves[x][0]][moves[x][1]] = board[i][j];
					board[i][j] = None;
					analyze_check();
					if(not ((tteam == "white" and white_check) or (tteam == "black" and black_check))):
						dic[(i,j)].append((moves[x]));
					board[i][j] = board[moves[x][0]][moves[x][1]];
					board[moves[x][0]][moves[x][1]] = piece_taken;
				if(len(dic[(i,j)]) == 0):
					del dic[(i,j)];
	return dic;


# returns the team opposite to the given team
def flip_team(team):
	eteam = "white";
	if(team == "white"):
		eteam = "black";
	return eteam;


# returns whether the given position is in jepordy
def is_in_jepordy(pos,tteam):
	eteam = flip_team(tteam);
	if(pos in get_all_moves(eteam)):
		return True;
	return False;


# returns a list of all pieces on the given team which can attack the given space
def get_attackers(pos,tteam):
	arr = [];
	for i in range(0,8):
		for j in range(0,8):
			if(board[i][j] != None and board[i][j].team == tteam and pos in board[i][j].get_moves()):
				arr.append((i,j));
	return arr;


# analyzes pieces jepodizing/occupying the given space to determine net worth of that space
# "the returned value represents the value gained if a piece-for-piece tradeoff were to ocurr here"
def tradeoff_value(pos,tteam):
	tot = 0;
	arr = get_attackers(pos,tteam);
	arr.append(get_attackers(pos,flip_team(tteam)));
	if(board[pos[0]][pos[1]] != None):
		arr.append(pos);
	for x in range(0,len(arr)):
		piece = board[arr[x][0]][arr[x][1]];
		if(piece.team != tteam):
			tot += piece.value;
		else:
			tot -= piece.value;
	return tot;


# sums up the value of all pieces in the given array of positions
def sum_values(arr):
	tot = 0;
	for x in arr:
		tot += board[x[0]][x[1]];
	return tot;

# returns whether the given postion is being backed up by another friendly piece
def is_backed_up(pos,tteam):
	if(pos in get_all_moves(tteam)):
		return True;
	return False;


# Chooses a move based on points assigned due to various elements of the board/situation
def basic_point_system(board,tteam):
	available_moves = get_all_moves(tteam);
	keys = available_moves.keys();
	point_dic = {};
	for x in range(0,len(keys)):
		key = keys[x];
		for y in range(0,len(available_moves[key])):
			pos1 = key;
			pos2 = available_moves[key][y];
			point_dic[(pos1,pos2)] = 0;
			# things to check: pieces taken, self in jepordy, puts self in jepordy, puts enemy in check,
			# puts enemy in jepordy,
			# accounts for if your piece is in jepordy
			if(is_in_jepordy(pos1,tteam)):
				if(sum_values(get_attackers(pos1,tteam)) == sum_values(get_attackers(pos1,tteam))):
					point_dic[(pos1,pos2)] += tradeoff_value(pos1);
				elif(sum_values(get_attackers(pos1,tteam)) > sum_values(get_attackers(pos1,tteam))):
					return;


# deteermines if the given team is in checkmate
def in_checkmate(tteam):
	if(tteam == "white" and white_check == True and can_move_any("white") == False):
		return True;
	if(tteam == "black" and black_check == True and can_move_any("black") == False):
		return True;
	

# determines if the game is stalemated
def in_stalemate():
	if(white_check == False and can_move_any("white") == False):
		return True;
	if(black_check == False and can_move_any("black") == False):
		return True;
	
	
# heuristic evaluation function which examines the entire board
# + considers: piece-value, check, 
def evaluate_board():
	analyze_check();
	if(in_checkmate(enemy_team)):
		return -1000000000;
	if(in_checkmate(player_team)):
		return 1000000000;
	tot = 0;
	if((enemy_team == "black" and black_check) or (enemy_team == "white" and white_check)):
		tot -= 0.3;
	elif((player_team == "black" and black_check) or (player_team == "white" and white_check)):
		tot += 0.3;
	for i in range(0,8):
		for j in range(0,8):
			if(board[i][j] != None and board[i][j].team == player_team):
				tot -= board[i][j].value;
			if(board[i][j] != None and board[i][j].team == enemy_team):
				tot += board[i][j].value;
	
	
# recursive minimax algorithm where node = move, and max-player = enemyAI
def minimax(moves,depth,max_player):
	if(depth == 0 or in_checkmate(enemy_team) or in_checkmate(player_team) or in_stalemate()):
		return (None , evaluate_board());
	
	if(max_player == enemy_team):
		best_value = -1000000000;
		for key, value in moves.iteritems():
			origin = deepcopy(board);
			move = (key,value);
			board[value[0]][value[1]] = board[key[0]][key[1]];
			board[key[0]][key[1]] = None;
			new_moves = get_all_moves(flip_team(max_player));
			v = minimax(new_moves,depth-1,flip_team(max_player))[1];
			board = origin;
			best_value = max(best_value,v);
		return (move , best_value);
	
	if(max_player == player_team):
		best_value = 1000000000;
		for key, value in moves.iteritems():
			origin = deepcopy(board);
			move = (key,value);
			board[value[0]][value[1]] = board[key[0]][key[1]];
			board[key[0]][key[1]] = None;
			new_moves = get_all_moves(flip_team(max_player));
			v = minimax(new_moves,depth-1,flip_team(max_player));
			board = origin;
			best_value = min(best_value,v);
		return (move , best_value);
	

# move selection function which uses minimax to determine best course of action
def get_move_minimax(tteam):
	return minimax(get_all_moves(tteam),4,tteam)[0];
	