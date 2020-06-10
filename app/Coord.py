class Coord:
    row = None
    column = None

    def __init__(self, column, row):
        if row in ('1','2','3','4','5','6','7','8'):
            self.row = row
        else:
            raise ValueError(
                f"{str(row)} is not a valid row.\n"
                "Valid rows are '1','2','3','4','5','6','7','8'."
            )

        if column in ('a','b','c','d','e','f','g','h'):
            self.column = column
        else:
            raise ValueError(
                f"{str(column)} is not a valid column.\n"
                "Valid columns are 'a','b','c','d','e','f','g','h'."
            )
