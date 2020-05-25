class Piece:
    def __init__(self, faction, coord):
        valid_factions = ("blanc", "noir")
        if faction.lower() not in Piece.valid_factions:
            raise ValueError(f"{faction} is not a valid faction. Valid factions are {Piece.valid_factions}")
        else:
            self.faction = faction.lower()
        self.coord = coord

    def get_faction(self):
        return self.faction

    def get_coord(self):
        return self.coord

    def move(self, coord, dry_run=False):
        if coord in self.get_valid_moves():
            if not dry_run:
                self.coord = coord
            return True
        else:
            return False

    def get_valid_moves(self):
        """
        Exists so that move() does not syntax fail.
        However should be overwritten by extending piece,
        currently will force move() to return False
        """
        return []
