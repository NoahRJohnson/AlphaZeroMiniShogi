
'''
The pieces will store information about how they move.
When asked, they will return a list of their moves, 
as (x,y,n) showing the direction (x,y), and n: how
many squares the piece can move in the corresponding direction. 

n = 0 means the piece cannot move in that direction.
n = 1 means the piece can move one square in that direction.
n = -1 corresponds to an infinite reach (e.g. Bishops).
'''

class Piece():
    
    def __init__(self, color):
        pass
    
    def moves(self):
        pass
    
    def promote(self):
        self.isPromoted = True
    
    def dePromote(self):
        self.isPromoted = False
        
    def isPromoted(self):
        return self.isPromoted
        
    def self.getColor(self):
        return self.color
        
    def getName(self):
        return self.name

    
    
class King(Piece):
    
    def __init__(self, color):
        self.isPromoted = False
        self.color = color
        if (color == 1):
            self.name = "King General"
        else:  # black piece
            self.name = "Jeweled General"
    
    # Kings can't promote
    def promote(self):
        pass
        
    def moves(self):
        return [(1,1,1), (1,0,1), (1,-1,1), (0,-1,1),
                    (-1,-1,1), (-1,0,1), (-1,1,1), (0,1,1)]

class GoldGeneral(Piece):
    
    def __init__(self, color):
        self.isPromoted = False
        self.name = "Gold General"
        self.color = color
    
    # Gold Generals can't promote
    def promote(self):
        pass
        
    def moves(self):
        return [(1,1,1), (1,0,1), (1,-1,0), (0,-1,1),
                    (-1,-1,0), (-1,0,1), (-1,1,1), (0,1,1)]
    
class SilverGeneral(Piece):
    
    def __init__(self, color):
        self.isPromoted = False
        self.name = "Silver General"
        self.color = color
    
    def promote(self):
        self.isPromoted = True
        self.name = "Promoted Silver General"
        
    def dePromote(self):
        self.isPromoted = False
        self.name = "Silver General"
        
    def moves(self):
        if self.isPromoted:
            return [(1,1,1), (1,0,1), (1,-1,0), (0,-1,1),
                    (-1,-1,0), (-1,0,1), (-1,1,1), (0,1,1)]
        else:
            return [(1,1,1), (1,0,0), (1,-1,1), (0,-1,0),
                    (-1,-1,1), (-1,0,0), (-1,1,1), (0,1,1)]
    
class Bishop(Piece):
    
    def __init__(self, color):
        self.isPromoted = False
        self.name = "Bishop"
        self.color = color
    
    def promote(self):
        self.isPromoted = True
        self.name = "Dragon Horse"
        
    def dePromote(self):
        self.isPromoted = False
        self.name = "Bishop"
        
    def moves(self):
        if self.isPromoted:
            return [(1,1,-1), (1,0,1), (1,-1,-1), (0,-1,1),
                    (-1,-1,-1), (-1,0,1), (-1,1,-1), (0,1,1)]
        else:
            return [(1,1,-1), (1,0,0), (1,-1,-1), (0,-1,0),
                    (-1,-1,-1), (-1,0,0), (-1,1,-1), (0,1,0)]
    
class Rook(Piece):
    
    def __init__(self, color):
        self.isPromoted = False
        self.name = "Rook"
        self.color = color
    
    def promote(self):
        self.isPromoted = True
        self.name = "Dragon King"
        
    def dePromote(self):
        self.isPromoted = False
        self.name = "Rook"
        
    def moves(self):
        if self.isPromoted:
            return [(1,1,1), (1,0,-1), (1,-1,1), (0,-1,-1),
                    (-1,-1,1), (-1,0,-1), (-1,1,1), (0,1,-1)]
        else:
            return [(1,1,0), (1,0,-1), (1,-1,0), (0,-1,-1),
                    (-1,-1,0), (-1,0,-1), (-1,1,0), (0,1,-1)]

class Pawn(Piece):

    def __init__(self, color):
        self.isPromoted = False
        self.name = "Pawn"
        self.color = color
    
    def promote(self):
        self.isPromoted = True
        self.name = "Promoted Pawn"
        
    def dePromote(self):
        self.isPromoted = False
        self.name = "Pawn"
        
    def moves(self):
        if self.isPromoted:
            return [(1,1,1), (1,0,1), (1,-1,0), (0,-1,1),
                    (-1,-1,0), (-1,0,1), (-1,1,1), (0,1,1)]
                    
        else:
            return [(1,1,0), (1,0,0), (1,-1,0), (0,-1,0),
                    (-1,-1,0), (-1,0,0), (-1,1,0), (0,1,1)]
