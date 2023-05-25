class Adresse:  

    def __init__(self, rue, numero, ville, code_postal):
        self.rue = rue
        self.numero = numero
        self.ville = ville
        self.code_postal = code_postal

    def adresse(self):
        return f"Vous habitez {self.rue} au {self.numero} dans la ville {self.ville} {self.code_postal}!"