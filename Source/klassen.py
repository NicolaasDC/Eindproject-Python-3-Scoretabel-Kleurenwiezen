class Kleurenwiezen():

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

    def update_score(self, speler, spel, vrager, gelukt, overslagen=0):
        puntenverdeling_vrager_gelukt = {
            "Samen 8": {"vrager": [7, 10, 13, 16, 19, 30], "niet_vrager": [-7, -10, -13, -16, -19, -30]},
            "Solo 5": {"vrager": [9, 12, 15, 21, 21, 21, 21, 21, 21], "niet_vrager": [-3, -4, -5, -7, -7, -7, -7, -7, -7]},
            "Samen 9": {"vrager": [10, 13, 16, 19, 30], "niet_vrager": [-10, -13, -16, -19, -30]},
            "Solo 6": {"vrager": [12, 15, 21], "niet_vrager": [-4, -5, -7]},
            "Samen 10": {"vrager": [13, 16, 19, 30], "niet_vrager": [-13, -16, -19, -30]},
            "Solo 7": {"vrager": [15, 21], "niet_vrager": [-5, -7]},
            "Samen 11": {"vrager": [16, 19, 30], "niet_vrager": [-16, -19, -30]},
            "Kleine miserie": {"vrager": [18], "niet_vrager": [-6]},
            "Samen 12": {"vrager": [19, 30], "niet_vrager": [-19, -30]},
            "Solo 8": {"vrager": [21], "niet_vrager": [-7]},
            "Samen 13": {"vrager": [30], "niet_vrager": [-30]},
            "Abondance 9": {"vrager": [33], "niet_vrager": [-11]},
            "Troel voor 8": {"vrager": [16, 16, 16, 16, 16, 30], "niet_vrager": [-16, -16, -16, -16, -16, -30]},
            "Troel voor 9": {"vrager": [16, 16, 16, 16, 30], "niet_vrager": [-16, -16, -16, -16, -30]},
            "Grote miserie": {"vrager": [36], "niet_vrager": [-12]},
            "Abondance 10": {"vrager": [42], "niet_vrager": [-14]},
            "Abondance 11": {"vrager": [60], "niet_vrager": [-20]},
            "Blote miserie": {"vrager": [75], "niet_vrager": [-25]},
            "Abondance 12": {"vrager": [120], "niet_vrager": [-40]},
            "Solo slim": {"vrager": [240], "niet_vrager": [-80]}
        }

        puntenverdeling_vrager_mislukt ={
            "Samen 8": {"vrager": [0, -10, -13, -16, -19, -22, -25, -28], "niet_vrager": [0, 10, 13, 16, 19, 22, 25, 28]},
            "Solo 5": {"vrager": [0, -12, -15, -18, -21],"niet_vrager": [0, 4, 5, 6, 7]},
            "Samen 9": {"vrager": [0, -13, -16, -19, -22, -25, -28, -31], "niet_vrager": [0, 13, 16, 19, 22, 25, 28, 31]},
            "Solo 6": {"vrager": [0, -15, -18, -21, -24, -27], "niet_vrager": [0, 5, 6, 7, 8, 9]},
            "Samen 10": {"vrager": [0, -16, -19, -22, -25, -28, -31, -34, -37], "niet_vrager": [0, 16, 19, 22, 25, 28, 31, 34, 37]},
            "Solo 7": {"vrager": [0, -18, -21, -24, -27, -30, -33], "niet_vrager": [0, 6, 7, 8, 9, 10, 11]},
            "Samen 11": {"vrager": [0, -19, -22, -25, -28, -31, -34, -37], "niet_vrager": [0, 19, 22, 25, 28, 31, 34, 37]},
            "Kleine miserie": {"vrager": [-18], "niet_vrager": [6]},
            "Samen 12": {"vrager": [0, -22, -25, -28, -31, -34, -37, -40], "niet_vrager": [0, 22, 25, 28, 31, 34, 37, 40]},
            "Solo 8": {"vrager": [0, -21, -24, -27, -30, -33, -36, -39], "niet_vrager": [0, 7, 8, 9, 10, 11, 12, 13]},
            "Samen 13": {"vrager": [0, -30, -33, -36, -39, -42, -45, -48], "niet_vrager": [0, 30, 33, 36, 39, 42, 45, 48]},
            "Abondance 9": {"vrager": [33], "niet_vrager": [-11]},
            "Troel voor 8": {"vrager": [-16, -16, -16, -16, 16, -16, -16, -16], "niet_vrager": [16, 16, 16, 16, 16, 16, 16, 16]},
            "Troel voor 9": {"vrager": [-16, -16, -16, -16, 16, -16, -16, -16], "niet_vrager": [16, 16, 16, 16, 16, 16, 16, 16]},
            "Grote miserie": {"vrager": [-36], "niet_vrager": [12]},
            "Abondance 10": {"vrager": [-42], "niet_vrager": [14]},
            "Abondance 11": {"vrager": [-60], "niet_vrager": [20]},
            "Blote miserie": {"vrager": [-75], "niet_vrager": [25]},
            "Abondance 12": {"vrager": [-120], "niet_vrager": [40]},
            "Solo slim": {"vrager": [-240], "niet_vrager": [80]}
        }

        if speler == self.speler1:
            if vrager == True:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['vrager'][overslagen]
            if vrager == False:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['niet_vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['niet_vrager'][overslagen]

        if speler == self.speler2:
            if vrager == True:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['vrager'][overslagen]
            if vrager == False:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['niet_vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['niet_vrager'][overslagen]

        if speler == self.speler3:
            if vrager == True:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['vrager'][overslagen]
            if vrager == False:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['niet_vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['niet_vrager'][overslagen]

        if speler == self.speler4:
            if vrager == True:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['vrager'][overslagen]
            if vrager == False:
                if gelukt == True:
                    self.scores[speler] += puntenverdeling_vrager_gelukt[spel]['niet_vrager'][overslagen]
                if gelukt == False:
                    self.scores[speler] += puntenverdeling_vrager_mislukt[spel]['niet_vrager'][overslagen]