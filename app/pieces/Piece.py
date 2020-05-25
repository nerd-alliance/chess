class Piece:
    def __init__(self, faction, coord):
        valid_factions = ("blanc", "noir")
        if faction.lower() not in Piece.valid_factions:
            raise ValueError(
                f"{faction} is not a valid faction.\n"
                f"Valid factions are {Piece.valid_factions}."
            )
        elif not isinstance(faction, str):
            raise TypeError(
                "'faction' argument must be of type string.\n"
                f"Type {type(faction)} detected."
            )
        else:
            self.faction = faction.lower()

        if not isinstance(coord, dict):
            raise TypeError(
                "'coord' argument must be of type dict.\n"
                f"Type {type(coord)} detected."
            )
        elif not len(coord) == 2:
            raise ValueError(
                "Given coord is not a valid coord.\n"
                "Coords are a dict -> {'alpha': [a-h], 'numeric': [1-8]}"
            )
        else:
            self.coord = coord

    def get_faction(self):
        return self.faction

    def get_coord(self):
        return self.coord

    def move(self, coord, dry_run=False) -> boolean:
        if coord in self.get_valid_moves():
            if not dry_run:
                self.coord = coord
            return True
        else:
            return False

    def get_valid_moves(self) -> list:
        """
        Exists so that move() does not syntax fail.
        However should be overwritten by extending piece,
        currently will force move() to return False
        """
        return []
