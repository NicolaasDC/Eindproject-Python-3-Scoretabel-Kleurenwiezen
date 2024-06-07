
class Kleurenwiezen:

    def __init__(self, speler1, speler2, speler3, speler4):
        self.speler1 = speler1
        self.speler2 = speler2
        self.speler3 = speler3
        self.speler4 = speler4
        self.scores = {speler1: 0, speler2: 0, speler3: 0, speler4: 0}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.speler1!r}, {self.speler2!r}, {self.speler3!r}, {self.speler4!r})"

    def score(self):
        return f"{self.scores!r}"

    def update_score(self, spel, speler, vrager, gelukt, overslagen=0):
        puntenverdeling_vrager_gelukt = {
            "Samen 8": {"vrager": [7, 10, 13, 16, 19, 30], "niet_vrager": [-7, -10, -13, -16, -19, -30]},
            "Solo 5": {"vrager": [9, 12, 15, 21, 21, 21, 21, 21, 21], "niet_vrager": [-3, -4, -5, -7, -7, -7, -7, -7, -7]},
            "Samen 9": {"vrager": [10, 13, 16, 19, 30], "niet_vrager": [-10, -13, -16, -19, -30]},
            "Solo 6": {"vrager": [12, 15, 21, 21, 21, 21, 21, 21], "niet_vrager": [-4, -5, -7, -7, -7, -7, -7, -7]},
            "Samen 10": {"vrager": [13, 16, 19, 30], "niet_vrager": [-13, -16, -19, -30]},
            "Solo 7": {"vrager": [15, 21, 21, 21, 21, 21, 21], "niet_vrager": [-5, -7, -7, -7, -7, -7, -7]},
            "Samen 11": {"vrager": [16, 19, 30], "niet_vrager": [-16, -19, -30]},
            "Kleine miserie": {"vrager": [18], "niet_vrager": [-6]},
            "Samen 12": {"vrager": [19, 30], "niet_vrager": [-19, -30]},
            "Solo 8": {"vrager": [21, 21, 21, 21, 21], "niet_vrager": [-7, -7, -7, -7, -7]},
            "Samen 13": {"vrager": [30], "niet_vrager": [-30]},
            "Abondance 9": {"vrager": [33], "niet_vrager": [-11]},
            "Troel voor 8": {"vrager": [16, 16, 16, 16, 16, 30], "niet_vrager": [-16, -16, -16, -16, -16, -30]},
            "Troel voor 9": {"vrager": [16, 16, 16, 16, 30], "niet_vrager": [-16, -16, -16, -16, -30]},
            "Grote miserie": {"vrager": [36], "niet_vrager": [-12]},
            "Abondance 10": {"vrager": [42], "niet_vrager": [-42]},
            "Abondance 11": {"vrager": [60], "niet_vrager": [-20]},
            "Blote miserie": {"vrager": [75], "niet_vrager": [-75]},
            "Abondance 12": {"vrager": [120], "niet_vrager": [-40]},
            "Soloslim": {"vrager": [240], "niet_vrager": [-80]}
        }

        puntenverdeling_vrager_mislukt ={
            "Samen 8": {"vrager": [-10, -10, -13, -16, -19, -22], "niet_vrager": [10, 10, 13, 16, 19, 22]},
            "Solo 5": {"vrager": [-12, -12, -15, -18, -21, -24],"niet_vrager": [4, 5, 6, 7, 8]},
            "Samen 9": {"vrager": [-13, -13, -16, -19, -22, -25], "niet_vrager": [13, 16, 19, 22, 25]},
            "Solo 6": {"vrager": [-15, -15, -18, -21, -24, -27], "niet_vrager": [5, 6, 7, 8, 9]},
            "Samen 10": {"vrager": [-16, -16, -19, -22, -25], "niet_vrager": [16, 19, 22, 25]},
            "Solo 7": {"vrager": [-18, -18, -21, -24, -27, -30], "niet_vrager": [6, 7, 8, 9, 10]},
            "Samen 11": {"vrager": [-19, -19, -22, -25, -28, -31], "niet_vrager": [19, 22, 25, 28, 31]},
            "Kleine miserie": {"vrager": [-18], "niet_vrager": [6]},
            "Samen 12": {"vrager": [-22, -22, -25, -28, -31, -34], "niet_vrager": [19, 22, 25, 28, 31, 34]},
            "Solo 8": {"vrager": [-21, -21, -24, -27, -30, -33], "niet_vrager": [7, 8, 9, 10, 11]},
            "Samen 13": {"vrager": [-30, -30, -33, -36, -39, -42, -45 ], "niet_vrager": [30, 30, 33, 36, 39, 42, 45]},
            "Abondance 9": {"vrager": [33], "niet_vrager": [-11]},
            "Troel voor 8": {"vrager": [-16], "niet_vrager": [16]},
            "Troel voor 9": {"vrager": [-16], "niet_vrager": [16]},
            "Grote miserie": {"vrager": [-36], "niet_vrager": [12]},
            "Abondance 10": {"vrager": [-42], "niet_vrager": [42]},
            "Abondance 11": {"vrager": [-60], "niet_vrager": [20]},
            "Blote miserie": {"vrager": [-75], "niet_vrager": [75]},
            "Abondance 12": {"vrager": [-120], "niet_vrager": [40]},
            "Soloslim": {"vrager": [-240], "niet_vrager": [80]}
        }