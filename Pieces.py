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
		

class Pawn(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def can_move(self,pos):
		if(self.team == "white"):
			return [(pos[0] + 1 , pos[1] + 1) , (pos[0] - 1 , pos[1] + 1)];
		else:
			return (to_tuple[0] != 0 and to_tuple[1] != 0) and (to_tuple[0] - from_tuple[0] == -1) and (abs(to_tuple[1] - from_tuple[1]) == 1);
		
	def __repr__(self):
		return self.team + " pawn";


class Rook(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def can_move(self,from_tuple,to_tuple):
		return (from_tuple[0] == to_tuple[0] or from_tuple[1] == to_tuple[1]);
	
	def iterate(self,from_tuple,to_tuple):
		# function assumes get_moves() has passed
		direction = (to_tuple - from_tuple);
		direction = (direction[0] / linalg.norm(direction)  ,  direction[1] / linalg.norm(direction));
		return from_tuple + direction;

	def __repr__(self):
		return self.team + " rook";


class Bishop(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def can_move(self,from_tuple,to_tuple):
		return (from_tuple[0] - to_tuple[0] == from_tuple[1] - to_tuple[1]);
	
	def iterate(self,from_tuple,to_tuple):
		# function assumes get_moves() has passed
		direction = (to_tuple - from_tuple);
		direction = (direction[0] / linalg.norm(direction)  ,  direction[1] / linalg.norm(direction));
		return from_tuple + direction;

	def __repr__(self):
		return self.team + " bishop";
	

class Kight(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def can_move(self,from_tuple,to_tuple):
		return ( abs(from_tuple[0] - to_tuple[0]) == 2  and  abs(from_tuple[1] - to_tuple[1]) == 1 )   or   ( abs(from_tuple[0] - to_tuple[0]) == 1  and  abs(from_tuple[1] - to_tuple[1]) == 2 );

	def __repr__(self):
		return self.team + " knight";
	

class Queen(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = False;
	
	def can_move(self,from_tuple,to_tuple):
		return (from_tuple[0] - to_tuple[0] == from_tuple[1] - to_tuple[1]) or (from_tuple[0] == to_tuple[0] or from_tuple[1] == to_tuple[1]);
	
	def iterate(self,from_tuple,to_tuple):
		# function assumes get_moves() has passed
		direction = (to_tuple - from_tuple);
		direction = (direction[0] / linalg.norm(direction)  ,  direction[1] / linalg.norm(direction));
		return from_tuple + direction;

	def __repr__(self):
		return self.team + " queen";
	

class King(Piece):
	
	def __init__(self,te):
		Piece.__init__(self,te);
		self.can_jump = True;
	
	def can_move(self,from_tuple,to_tuple):
		return (abs(from_tuple[0] - to_tuple[0]) <= 1 and abs(from_tuple[1] - to_tuple[1]) <= 1) and (abs(from_tuple[0] - to_tuple[0]) != 0 or abs(from_tuple[1] - to_tuple[1]) != 0);
	
	def __repr__(self):
		return self.team + " king";
	

