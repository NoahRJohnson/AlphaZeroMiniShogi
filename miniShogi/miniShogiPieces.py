
'''
The pieces will store information about how they move.
When asked, they will return a list of all 8 directions
on the board, as (x,y,n) offsets showing how many squares
n the piece can move in the corresponding direction. n=-1
will correspond to an infinite reach (e.g. Bishops).
'''

class Piece():
    
    def __init__(self):
        self.isPromoted = False
    
    def isPromoted(self):
        return self.isPromoted
        
    def moves(self):
        pass

class Pawn():
    
    def moves(self):
        if self.isPromoted:
            pass
        else:
            return [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
    
class King():
    
class GoldGeneral():
    
class SilverGeneral():
    
class Bishop():
    
class Rook():
    
