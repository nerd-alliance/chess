class Piece:
    valid_factions = ("blanc", "noir")
    def __init__(self, faction, coord):
        if faction.lower() not in Piece.valid_factions:
            raise ValueError(f"{faction} is not a valid faction. Valid factions are {Piece.valid_factions}")
        else:
            self.faction = faction.lower()
        self.coord = coord

    def get_faction(self):
        return self.faction

    def get_coord(self):
        return self.coord
