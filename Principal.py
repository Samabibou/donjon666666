class Stickers :
    def __init__(self, nom, serie, taille, prix):
        self.nom = nom
        self.serie = serie
        self.taille = taille
        self._prix = prix

autocollant_1 = Stickers("Sukuna", "JJK", "S", 0.20)