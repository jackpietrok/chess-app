import sys;

# PIECE VALUES


# make a random move of those available
# # move returned is in form ((row1,col1),(row2,col2))
def get_random_move(tteam):
	dic = get_all_moves(tteam);
	rand_key = choice(dic.keys());
	rand_item = choice(dic[rand_key])
	return (rand_key,rand_item);


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


# returns whether the given position is in jepordy
def is_in_jepordy(pos,tteam):
    eteam = "white";
    if(tteam == "white"):
        eteam = "black";
    if(pos in get_all_moves(eteam)):
        return True;
    return False;


# returns a list of ALL pieces which can attack the given space
def get_attackers(pos):
    arr = [];
    for i in range(0,8):
        for j in range(0,8):
            if(board[i][j] != None and pos in board[i][j].get_moves()):
                arr.append((i,j));
    return arr;


# analyzes pieces jepodizing/occupying the given space to determine net worth of that space
# "the returned value represents the value gained if a piece-for-piece tradeoff were to ocurr here"
def tradeoff_value(pos,tteam):
    tot = 0;
    arr = get_attackers(pos);
    if(board[pos[0]][pos[1]] != None):
        arr.append(pos);
    for x in range(0,len(arr)):
        piece = board[arr[x][0]][arr[x][1]]
        if(piece.team != tteam):
            tot += piece.value;
        else:
            tot -= piece.value
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
        key = keys[x]
        for y in range(0,len(available_moves[key])):
            pos1 = key;
            pos2 = available_moves[key][y];
            # things to check: pieces taken, self in jepordy, puts self in jepordy, puts enemy in check,
            # puts enemy in jepordy,
            
            # accounts for if your piece is in jepordy
            if(is_in_jepordy(pos1,tteam)):
                
        
        