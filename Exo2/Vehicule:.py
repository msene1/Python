import moto_module
import camion_module
import voiture_module

class Vehicule:
    def __init__(self):
        self.type = None
        self.modele = None

    def choisir_vehicule(self):
        print("=== Choix du Véhicule ===")
        print("1. Moto")
        print("2. Camion")
        print("3. Voiture")

        choix = input("Entrez le numéro correspondant au véhicule choisi (1-3): ")

        if choix == "1":
            self.type = "Moto"
            print("Vous avez choisi une moto.")
        elif choix == "2":
            self.type = "Camion"
            print("Vous avez choisi un camion.")
        elif choix == "3":
            self.type = "Voiture"
            print("Vous avez choisi une voiture.")
        else:
            print("Choix invalide. Veuillez réessayer.")

    def choisir_modele(self):
        if self.type:
            if self.type == "Moto":
                self.modele = moto_module.choisir_modele()
            elif self.type == "Camion":
                self.modele = camion_module.choisir_modele()
            elif self.type == "Voiture":
                self.modele = voiture_module.choisir_modele()
        else:
            print("Veuillez d'abord choisir un type de véhicule.")

    def afficher_caracteristiques(self):
        if self.modele:
            print("Type de véhicule sélectionné :", self.type)
            print("Modèle sélectionné :", self.modele["Nom"])
            for caract, valeur in self.modele.items():
                if caract != "Nom":
                    print(caract, ":", valeur)
        else:
            print("Aucun véhicule ou modèle sélectionné.")

# Exemple d'utilisation de la classe Vehicule
vehicule = Vehicule()
vehicule.choisir_vehicule()
vehicule.choisir_modele()
vehicule.afficher_caracteristiques()
