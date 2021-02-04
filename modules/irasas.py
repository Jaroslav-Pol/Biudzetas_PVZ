class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        #skirtas objekto atvaizdavimui pvz kai
        # printinam
        return f'Irasas {self.tipas}: {self.suma}'