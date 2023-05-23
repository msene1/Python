class Personne:
    animal = "humain"

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Bonjour,  {self.nom} {self.prenom}! "

def saluer_personne(genre):
    if genre.lower() == "homme":
        return "Vous êtes un homme !"
    elif genre.lower() == "femme":
        return "Vous êtes une femme !"
    else:
        return "Genre non reconnu."

def determiner_age(annee_naissance):
    annee_actuelle = 2023  # Année actuelle (à titre d'exemple)
    age = annee_actuelle - annee_naissance

    if age < 0:
        return "Année de naissance invalide."
    elif age <= 18:
        return "Malheureusement vous êtes mineure :("
        
    elif age >= 18:
        return "Vous êtes un majeur."


