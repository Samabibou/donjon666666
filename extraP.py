from base import *

class Guerrier(Personnage):
    def __init__(self, nom: str, pv_max: int, force: int, armure: int):
        super().__init__(nom, pv_max, force)
        self.armure = armure

    def attaquer(self, cible: "Personnage"):
        print(f"{self.nom} charge avec son armure !")
        super().attaquer(cible)


class Mage(Personnage):
    def __init__(self, nom: str, pv_max: int, force: int, mana: int):
        super().__init__(nom, pv_max, force)
        self.mana = mana

    def lancer_sort(self, cible: "Personnage"):
        if self.mana >= 10:
            self.mana -= 10
            cible.pv = cible.pv - self.force * 2
            self.historique.append(f"{self.nom} lance un sort sur {cible.nom}")
        else:
            self.attaquer(cible)


class Inventaire:
    def __init__(self):
        self.objets = []

    def ajouter(self, objet: str):
        self.objets.append(objet)


def descente(hero: Personnage, monstres: list[Personnage]) -> bool:
    inventaire = Inventaire()
    for monstre in monstres:
        print(f"--- {hero.nom} affronte {monstre.nom} ---")
        while hero.est_vivant() and monstre.est_vivant():
            hero.attaquer(monstre)
            if monstre.est_vivant():
                monstre.attaquer(hero)
        if not hero.est_vivant():
            print(f"{hero.nom} est tombé au combat...")
            return False
        print(f"{monstre.nom} est vaincu !")
        inventaire.ajouter(f"Butin de {monstre.nom}")
    print(f"{hero.nom} a traversé le donjon !")
    return True