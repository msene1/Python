def choisir_modele():
    print("=== Choix du Modèle de Moto ===")
    print("1. Modèle Moto A (Puissance : 150)")
    print("2. Modèle Moto B (Puissance : 200)")
    print("3. Modèle Moto C (Puissance : 250)")

    choix = input("Entrez le numéro correspondant au modèle choisi (1-3): ")

    if choix == "1":
        return {"Nom": "Modèle Moto A", "Puissance": 150}
    elif choix == "2":
        return {"Nom": "Modèle Moto B", "Puissance": 200}
    elif choix == "3":
        return {"Nom": "Modèle Moto C", "Puissance": 250}
    else:
        return None
