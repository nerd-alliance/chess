class Tile:

    coord = None
    piece = None

    def __init__(self, coord, piece = None):
        # TODO: test if corrd is of type Coord
        self.coord = coord
        self.piece = piece
