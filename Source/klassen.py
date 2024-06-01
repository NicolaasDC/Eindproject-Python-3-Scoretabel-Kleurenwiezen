
class Speler:

    def __init__(self, naam, punten=0):
        self.naam = naam
        self.punten = punten

    def __repr__(self):
        return f"{self.__class__.__name__}({self.naam!r}, {self.punten!r})"

    def __str__(self):
        return f"{self.naam!r}, punten: {self.punten}"