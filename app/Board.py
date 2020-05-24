from Tile import Tile

class Board:
    rows = ('a','b','c','d','e','f','g','h')
    cols = ('1','2','3','4','5','6','7','8')
    def __init__(self):
        self.board = {}

        for row in Board.rows:
            for col in Board.cols:
                coord = row + col
                self.board[coord] = Tile(coord)

    def get_tile_piece(self, coord) -> Tile:
        return self.board[coord].get_piece()
