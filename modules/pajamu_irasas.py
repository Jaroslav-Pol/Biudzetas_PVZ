from modules.irasas import Irasas


class PajamuIrasas(Irasas):

    def __init__(self, suma, siuntejas, tipas):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.tipas = tipas

    def __str__(self):  # pakeiciam str kitaip nei tevinei klasei
        return f"Pajamos: {self.suma}, siuntejas: {self.siuntejas}, tipas: {self.tipas}"
