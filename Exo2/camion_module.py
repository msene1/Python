def choisir_modele():
    print("=== Choix du Modèle de Camion ===")
    print("1. Modèle Camion A (Capacité de chargement : 5000 kg)")
    print("2. Modèle Camion B (Capacité de chargement : 7500 kg)")
    print("3. Modèle Camion C (Capacité de chargement : 10000 kg)")

    choix = input("Entrez le numéro correspondant au modèle choisi (1-3): ")

    if choix == "1":
        return {"Nom": "Modèle Camion A", "Capacité de chargement": 5000}
    elif choix == "2":
        return {"Nom": "Modèle Camion B", "Capacité de chargement": 7500}
    elif choix == "3":
        return {"Nom": "Modèle Camion C", "Capacité de chargement": 10000}
    else:
        return None
