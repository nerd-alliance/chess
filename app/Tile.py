from pieces import *

class Tile:
    coords = ('a',0)
    piece = None
    colour = None

    def __init__(self, coords, piece=None, colour="#FBEAD3"):
        self.coords = coords
        self.colour = colour
        if piece is not None:
            self.piece = piece

    def get_piece(self):
        return self.piece

    def __str__(self):
        return self.piece
