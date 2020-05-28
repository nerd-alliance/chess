class Coord:
    row = None
    column = None

    def __init__(self, inRow, inColumn):
        if inRow in ('1','2','3','4','5','6','7','8'):
            row = inRow
        else:
            raise ValueError(
                f"{str(inRow)} is not a valid row.\n"
                "Valid rows are '1','2','3','4','5','6','7','8'."
            )

        if inColumn in ('a','b','c','d','e','f','g','h'):
            column = inColumn
        else:
            raise ValueError(
                f"{str(inColumn)} is not a valid column.\n"
                "Valid columns are 'a','b','c','d','e','f','g','h'."
            )
