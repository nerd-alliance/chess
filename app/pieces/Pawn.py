from .Piece import Piece

class Pawn(Piece):

    def get_valid_moves(self, board) -> list:
        """
        Returns a list of valid coords that the pawn can move to.
        """

        valid_moves = []

        # If white pawn is still in initial row
        if self.faction == "blanc" and self.coord.row == '2':
            pass

        elif self.faction == "noir" and self.coord.row == '7':
            # If black pawn is still in initial row
            pass

        else:
            pass

        ##0 TODO: Add valid moves for if a diagonal piece can be taken

        return valid_moves

    def __piece_in_location(self, coord, board):
        """
        If there is a piece in the given location of the given board.
        Returns boolean
        """
        if board.get_piece(coord) is None:
            return False
        else:
            return True

    def __str__(self):
        return "P"
