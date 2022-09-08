import random
class Card:
    def __init__(self, valoare, culoare, imgPathWhite, imgPathBlack):
        self.valoare = valoare
        self.culoare = culoare
        self.imgPathWhite = imgPathWhite
        self.imgPathBlack = imgPathBlack

    def __str__(self):
        return str(self.valoare) + " de " + str(self.culoare)

# a = Card(7, "trefla")
# print(a)


class Deck:
    #constructorul clasei
    def __init__(self):
        self.carti = []
        self.creare()

    #metoda prin care adaugam cartile
    def creare(self):
        for cul in ["trefla", "inima", "frunza", "romb"]:
            for val in range(2, 14):
                # paths for card images
                imgPathWhite = f"Assets\\cards\\white\{val}_{cul}.png"
                imgPathBlack = f"Assets\cards\\black\{val}_{cul}.png"
                self.carti.append(Card(val, cul, imgPathWhite, imgPathBlack))

    #metoda de afisare
    def __str__(self):
        for carte in self.carti:
            print(carte)

    #metoda prin care amestecam cartile
    def shuffle(self):
        for i in range(len(self.carti) - 1, 0, -1):
            r = random.randint(0, i)
            self.carti[i], self.carti[r] = self.carti[r], self.carti[i]

    #metoda prin care eliminam din pachet cartea impartita la un jucator
    def drawCard(self):
        return self.carti.pop()
