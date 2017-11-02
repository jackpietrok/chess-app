import sys;

class Piece:
	
	def __init__(self,ty,te):
		self.type = ty;
		self.team = te;
		
	def switch_team(self):
		if(team == "white"):
			team = "black";
		else:
			team = "white";
		

class Pawn(Piece):
	
	def get_moves(self,from_tuple,to_tuple):
		if(self.team == "white"):
			return (to_tuple[0] - from_tuple[0] == 1) and (abs(to_tuple[1] - from_tuple[1]) == 1);
		else:
			return (to_tuple[0] - from_tuple[0] == -1) and (abs(to_tuple[1] - from_tuple[1]) == 1);
		
	def __repr__(self):
		return self.team + " pawn";

class Rook(Piece):
	
	def get_moves(self,from_tuple,to_tuple):
		return (from_tuple[0] == to_tuple[0] or from_tuple[1] == to_tuple[1]);
	
	def __repr__(self):
		return self.team + " rook";

class Bishop(Piece):
	
	def get_moves(self,from_tuple,to_tuple):
		return (from_tuple[0] - to_tuple[0] == from_tuple[1] - to_tuple[1]);
	
	def __repr__(self):
		return self.team + " bishop";
	
class Kight(Piece):
	
	def get_moves(self,from_tuple,to_tuple):
		return ( abs(from_tuple[0] - to_tuple[0]) == 2  and  abs(from_tuple[1] - to_tuple[1]) == 1 )   or   ( abs(from_tuple[0] - to_tuple[0]) == 1  and  abs(from_tuple[1] - to_tuple[1]) == 2 );
	
	def __repr__(self):
		return self.team + " knight";
	
class Queen(Piece):
	
	def get_moves(self,from_tuple,to_tuple):
		return (from_tuple[0] - to_tuple[0] == from_tuple[1] - to_tuple[1]) or (from_tuple[0] == to_tuple[0] or from_tuple[1] == to_tuple[1]);
	
	def __repr__(self):
		return self.team + " queen";
	
class King(Piece):
	
	def get_moves(self,from_tuple,to_tuple):
		return (abs(from_tuple[0] - to_tuple[0]) <= 1 and abs(from_tuple[1] - to_tuple[1]) <= 1) and (abs(from_tuple[0] - to_tuple[0]) != 0 or abs(from_tuple[1] - to_tuple[1]) != 0);
	
	def __repr__(self):
		return self.team + " king";
	

