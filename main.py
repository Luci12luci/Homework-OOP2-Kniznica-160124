class Kniha:
    def __init__(self, nazov, autor, ISBN, dostupna (boolean), rok vydania):
       self.nazov = nazov
       self.autor = autor
       self.ISBN = ISBN
       self.dostupna = True
       self.rokVydania = rokVydania

    def vypozicaj(self):
        self.dostupa = False

class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def pozicaj_knihu(self, isbn_knihy):
        for kniha in self.zoznam_knih:
            if (kniha.isbn == isbn_knihy):
                kniha.vypozicaj()


