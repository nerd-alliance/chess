from .Piece import Piece
from ../Coord import Coord

class Pawn(Piece):

    def get_valid_moves(self, board) -> list:
        """
        Returns a list of valid coords that the pawn can move to.
        """

        valid_moves = []

        # If white pawn is still in initial row
        if self.faction == "blanc" and self.coord.row == '2':
            if not __piece_in_location(Coord('3', self.coord.column), board):
                valid_moves.append(Coord('3', self.coord.column))
            if not __piece_in_location(Coord('4', self.coord.column), board):
                valid_moves.append(Coord('4', self.coord.column))

        elif self.faction == "noir" and self.coord.row == '7':
            # If black pawn is still in initial row
            if not __piece_in_location(Coord('6', self.coord.column), board):
                valid_moves.append(Coord('6', self.coord.column))
            if not __piece_in_location(Coord('5', self.coord.column), board):
                valid_moves.append(Coord('5', self.coord.column))

        else:
            single_ahead = int(self.coord.row) + self.forward
            if (
                str(single_ahead) in ('1','2','3','4','5','6','7','8')
                and
                not __piece_in_location(Coord(single_ahead, self.coord.column), board)
            ):
                valid_moves.append(Coord(str(single_ahead), self.coord.column))

        ##0 TODO: Add valid moves for if a diagonal piece can be taken

        return valid_moves

    def __piece_in_location(self, location, board):
        """
        If there is a piece in the given location of the given board.
        Returns boolean
        """
        if board.get_piece(location) is None:
            return False
        else:
            return True

    def __str__(self):
        return "P"
