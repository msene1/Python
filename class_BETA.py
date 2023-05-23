class Voiture:
    marque = "Toyota"  # Attribut de classe

    def __init__(self, couleur): #class
        self.couleur = couleur  # Attribut d'instance

    def afficher_info(self):
        print("Marque :", Voiture.marque)
        print("Couleur :", self.couleur)

voiture1 = Voiture("rouge")
print(voiture1.marque)   # Affiche "Toyota"
print(voiture1.couleur)  # Affiche "rouge"
