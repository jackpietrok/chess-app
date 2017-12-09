import sys;

class Piece:
	
	def __init__(self,te):
		self.team = te;
		self.has_moved = False;
		
	def switch_team(self):
		if(team == "white"):
			team = "black";
		else:
			team = "white";
		

# Pawn piece
class Pawn(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def get_moves(self,board,pos):
		arr = [];
		row = pos[0];
		col = pos[1];
		if(self.team == "black"):
			if(col != 0 and (board[row+1][col-1] != None and board[row+1][col-1].team != "white")):
				arr += (row+1,col-1);
			if(col != 7 and (board[row+1][col+1] != None and board[row+1][col+1].team != "white")):
				arr += (row+1,col+1);
			if(board[row+1][col] == None):
				arr += (row+1,col);
			if((not self.has_moved) and board[row+2][col] == None):
				arr += (row+2,col);
		else:
			if(col != 0 and (board[row-1][col-1] != None and board[row-1][col-1].team != "black")):
				arr += (row-1,col-1);
			if(col != 7 and (board[row-1][col+1] != None and board[row-1][col+1].team != "black")):
				arr += (row-1,col+1);
			if(board[row-1][col] == None):
				arr += (row-1,col);
			if((not self.has_moved) and board[row-2][col] == None):
				arr += (row-2,col);
		return arr;
		
	def __repr__(self):
		return self.team + " pawn";


# Rook piece (castle)
class Rook(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def get_moves(self,board,pos):
		arr = [];
		row = pos[0];
		col = pos[1];
		for x in range(row-1,-1,-1):
			if(board[x][col] != None):
				if(board[x][col].team != self.team):
					arr += (x,col);
				break;
			else:
				arr += (x,col);
		for x in range(row+1,7):
			if(board[x][col] != None):
				if(board[x][col].team != self.team):
					arr += (x,col);
				break;
			else:
				arr += (x,col);
		for x in range(col-1,-1,-1):
			if(board[row][x] != None):
				if(board[row][x].team != self.team):
					arr += (row,x);
				break;
			else:
				arr += (row,x);
		for x in range(col+1,7):
			if(board[row][x] != None):
				if(board[row][x].team != self.team):
					arr += (row,x);
				break;
			else:
				arr += (row,x);
		return arr;

	def __repr__(self):
		return self.team + " rook";


# Bishop piece (priest)
class Bishop(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def get_moves(self,board,pos):
		arr = [];
		row = pos[0];
		col = pos[1];
		temp = pos;
		while(temp[0] != 0 and temp[1] != 0):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] -= 1;
				temp[1] -= 1;
		while(temp[0] != 0 and temp[1] != 7):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] -= 1;
				temp[1] += 1;
		while(temp[0] != 7 and temp[1] != 0):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] += 1;
				temp[1] -= 1;
		while(temp[0] != 7 and temp[1] != 7):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] -= 7;
				temp[1] -= 7;
		return arr;

	def __repr__(self):
		return self.team + " bishop";
	

# Knight piece (horse)
class Kight(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def get_moves(self,board,pos):
		arr = [];
		row = pos[0];
		col = pos[1];
		for i in range(row-2,row+3,4):
			for j in range(col-1,col+2,2):
				if(i >= 0 and i <= 7 and j <= 7 and j >= 0 and (board[i][j] == None or board[i][j].team != self.team)):
					arr += (i,j);
		for i in range(row-1,row+2,2):
			for j in range(col-2,col+3,4):
				if(i >= 0 and i <= 7 and j <= 7 and j >= 0 and (board[i][j] == None or board[i][j].team != self.team)):
					arr += (i,j);
		return arr;

	def __repr__(self):
		return self.team + " knight";


# Queen piece
class Queen(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	# This one's a monster (rook and bishop combined)
	def get_moves(self,board,pos):
		arr = [];
		row = pos[0];
		col = pos[1];
		temp = pos;
		for x in range(row-1,-1,-1):
			if(board[x][col] != None):
				if(board[x][col].team != self.team):
					arr += (x,col);
				break;
			else:
				arr += (x,col);
		for x in range(row+1,7):
			if(board[x][col] != None):
				if(board[x][col].team != self.team):
					arr += (x,col);
				break;
			else:
				arr += (x,col);
		for x in range(col-1,-1,-1):
			if(board[row][x] != None):
				if(board[row][x].team != self.team):
					arr += (row,x);
				break;
			else:
				arr += (row,x);
		for x in range(col+1,7):
			if(board[row][x] != None):
				if(board[row][x].team != self.team):
					arr += (row,x);
				break;
			else:
				arr += (row,x);
		while(temp[0] != 0 and temp[1] != 0):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] -= 1;
				temp[1] -= 1;
		while(temp[0] != 0 and temp[1] != 7):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] -= 1;
				temp[1] += 1;
		while(temp[0] != 7 and temp[1] != 0):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] += 1;
				temp[1] -= 1;
		while(temp[0] != 7 and temp[1] != 7):
			if(board[temp[0]][temp[1]] != None):
				if(board[temp[0]][temp[1]] != self.team):
					arr += temp;
				break;
			else:
				arr += temp;
				temp[0] -= 7;
				temp[1] -= 7;
		return arr;

	def __repr__(self):
		return self.team + " queen";
	

# King piece
class King(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def get_moves(self,board,pos):
		arr = [];
		row = pos[0];
		col = pos[1];
		for i in range(row-1,row+2):
			for j in range(col-1,col+2):
				if((i == row and j == col) or i < 0 or i > 7 or j < 0 or j > 7):
					continue;
				elif(board[i][j] == None or board[i][j].team != self.team):
					arr += (i,j);
		return arr;
	
	def __repr__(self):
		return self.team + " king";
	

