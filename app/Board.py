from Coord import Coord

class Board:
    cols = ('a','b','c','d','e','f','g','h')
    rows = ('8','7','6','5','4','3','2','1')

    def __init__(self):
        self.board = {}

        for row in self.rows:
            for col in self.cols:
                b_coord = col + row
                self.board[b_coord] = f"{col}, {row}"

    def get_piece(self, coord):
        return get_piece(coord.column, coord.row)

    def get_piece(self, col, row):
        b_coord = col + row
        return self.board[b_coord]
