from Coord import Coord

class Board:
    def __init__(self):
        self.board = {}
        cols = ('a','b','c','d','e','f','g','h')
        rows = ('1','2','3','4','5','6','7','8')

        for row in rows:
            for col in cols:
                b_coord = col + row
                self.board[b_coord] = None

    def get_piece(self, coord):
        b_coord = coord.column + coord.row
        return self.board[b_coord]
