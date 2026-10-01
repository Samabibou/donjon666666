class Personnage:
    def __init__(self, nom: str, pv_max: int, force: int):
        self.nom = nom
        self.pv_max = pv_max
        self._pv = pv_max
        self.force = force
        self.historique = []

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, valeur: int):
        self._pv = max(0, min(self.pv_max, valeur))

    def attaquer(self, cible: "Personnage"):
        cible.pv = cible.pv - self.force
        self.historique.append(f"{self.nom} attaque {cible.nom}")

    def est_vivant(self) -> bool:
        return self.pv > 0