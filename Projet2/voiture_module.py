def choisir_modele(type_vehicule):
    print("=== Choix du Modèle ===")
    if type_vehicule == "Moto":
        print("1. Modèle Moto A")
        print("2. Modèle Moto B")
        print("3. Modèle Moto C")
        choix = input("Entrez le numéro correspondant au modèle choisi (1-3): ")
        if choix == "1":
            return {"Nom": "Modèle Moto A", "Puissance": 150}
        elif choix == "2":
            return {"Nom": "Modèle Moto B", "Puissance": 200}
        elif choix == "3":
            return {"Nom": "Modèle Moto C", "Puissance": 250}
    elif type_vehicule == "Camion":
        print("1. Modèle Camion A")
        print("2. Modèle Camion B")
        print("3. Modèle Camion C")
        choix = input("Entrez le numéro correspondant au modèle choisi (1-3): ")
        if choix == "1":
            return {"Nom": "Modèle Camion A", "Capacité de chargement": 5000}
        elif choix == "2":
            return {"Nom": "Modèle Camion B", "Capacité de chargement": 7500}
        elif choix == "3":
            return {"Nom": "Modèle Camion C", "Capacité de chargement": 10000}
    elif type_vehicule == "Voiture":
        print("1. Modèle Voiture A")
        print("2. Modèle Voiture B")
        print("3. Modèle Voiture C")
        choix = input("Entrez le numéro correspondant au modèle choisi (1-3): ")
        if choix == "1":
            return {"Nom": "Modèle Voiture A", "Consommation": 8.5}
        elif choix == "2":
            return {"Nom": "Modèle Voiture B", "Consommation": 10.2}
        elif choix == "3":
            return {"Nom": "Modèle Voiture C", "Consommation": 12.0}
    else:
        return None
def choisir_modele():
    print("=== Choix du Modèle de Voiture ===")
    print("1. Modèle Voiture A (Consommation : 8.5 L/100km)")
    print("2. Modèle Voiture B (Consommation : 10.2 L/100km)")
    print("3. Modèle Voiture C (Consommation : 12.0 L/100km)")

    choix = input("Entrez le numéro correspondant au modèle choisi (1-3): ")

    if choix == "1":
        return {"Nom": "Modèle Voiture A", "Consommation": 8.5}
    elif choix == "2":
        return {"Nom": "Modèle Voiture B", "Consommation": 10.2}
    elif choix == "3":
        return {"Nom": "Modèle Voiture C", "Consommation": 12.0}
    else:
        return None
