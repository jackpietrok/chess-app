import sys;
from numpy import *;

class Piece:
	
	def __init__(self,te):
		self.team = te;
		
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
	
	def get_moves(self,pos):
		if(self.team == "white"):
			return [(pos[0] + 1 , pos[1] + 1) , (pos[0] + 1 , pos[1] - 1)];
		else:
			return [(pos[0] - 1 , pos[1] + 1) , (pos[0] - 1 , pos[1] - 1)];
		
	def __repr__(self):
		return self.team + " pawn";


# Rook piece (castle)
class Rook(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def get_moves(self,pos):
		arr = [];
		for y in range(0,7):
			if(y != pos[1]):	
				arr += (pos[0] , y);
			if(y != pos[0]):
				arr += (y , pos[1]);
		return arr;
	
	def iterate(self,from_tuple,to_tuple):
		# function assumes get_moves() has passed
		direction = (to_tuple - from_tuple);
		direction = (direction[0] / linalg.norm(direction)  ,  direction[1] / linalg.norm(direction));
		return from_tuple + direction;

	def __repr__(self):
		return self.team + " rook";


# Bishop piece (priest)
class Bishop(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def get_moves(self,pos):
		arr = [];
		count = 1;
		for i in range(pos[1],7):
			arr += (pos[0]+count,pos[1]+count);
			arr += (pos[0]-count,pos[1]-count);
			count += 1;
	
	def iterate(self,from_tuple,to_tuple):
		# function assumes get_moves() has passed
		direction = (to_tuple - from_tuple);
		direction = (direction[0] / linalg.norm(direction)  ,  direction[1] / linalg.norm(direction));
		return from_tuple + direction;

	def __repr__(self):
		return self.team + " bishop";
	

# Knight piece (horse)
class Kight(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def get_moves(self,from_tuple,to_tuple):
		return ( abs(from_tuple[0] - to_tuple[0]) == 2  and  abs(from_tuple[1] - to_tuple[1]) == 1 )   or   ( abs(from_tuple[0] - to_tuple[0]) == 1  and  abs(from_tuple[1] - to_tuple[1]) == 2 );

	def __repr__(self):
		return self.team + " knight";
	

# Queen piece
class Queen(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def get_moves(self,from_tuple,to_tuple):
		return (from_tuple[0] - to_tuple[0] == from_tuple[1] - to_tuple[1]) or (from_tuple[0] == to_tuple[0] or from_tuple[1] == to_tuple[1]);
	
	def iterate(self,from_tuple,to_tuple):
		# function assumes get_moves() has passed
		direction = (to_tuple - from_tuple);
		direction = (direction[0] / linalg.norm(direction)  ,  direction[1] / linalg.norm(direction));
		return from_tuple + direction;

	def __repr__(self):
		return self.team + " queen";
	

# King piece
class King(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def get_moves(self,from_tuple,to_tuple):
		return (abs(from_tuple[0] - to_tuple[0]) <= 1 and abs(from_tuple[1] - to_tuple[1]) <= 1) and (abs(from_tuple[0] - to_tuple[0]) != 0 or abs(from_tuple[1] - to_tuple[1]) != 0);
	
	def __repr__(self):
		return self.team + " king";
	

