from Coord import Coord
from Tile import Tile
from Pawn import Pawn
from Bishop import Bishop
from Castle import Castle
from Knight import Knight
from Queen import Queen
from King import King

class Board:
    cols = ('a','b','c','d','e','f','g','h')
    rows = ('8','7','6','5','4','3','2','1')

    def __init__(self):
        self.board = {}


        for row in self.rows:
            for col in self.cols:
                coord = Coord(col, row)
                b_coord = col + row
                self.board[b_coord] = Tile(coord, self.__initial_value(coord))

    def get_piece(self, coord):
        return get_piece(coord.column, coord.row)

    def get_piece(self, col, row):
        b_coord = col + row
        return self.board[b_coord].piece

    def get_piece_symbol(self, col, row):
        symbol = self.get_piece(col, row).__str__()
        if symbol == "None":
            return "-"
        else:
            return symbol

    def __initial_value(self, coord):
        if coord.row == '2':
            return Pawn("blanc", coord)
        if coord.row == '7':
            return Pawn("noir", coord)

        if coord.row == "1":
            faction = "blanc"
        elif coord.row == "8":
            faction = "noir"
        else:
            return None

        if coord.column in ("a", "h"):
            return Castle(faction, coord)
        if coord.column in ("b", "g"):
            return Knight(faction, coord)
        if coord.column in ("c", "f"):
            return Bishop(faction, coord)

        if coord.column == "d":
            return Queen(faction, coord)
        if coord.column == "e":
            return King(faction, coord)
