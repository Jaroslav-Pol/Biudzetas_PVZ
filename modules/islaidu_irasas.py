
from modules.irasas import Irasas

class IslaiduIrasas(Irasas):

    def __init__(self, suma, apmokejimo_budas, preke_paslauga):
        super().__init__(suma)
        self.apmokejimo_budas = apmokejimo_budas
        self.preke_paslauga = preke_paslauga

    def __str__(self): #pakeiciam str kitaip nei tevinei klasei
        return f"Islaidos: {self.suma}, apmokejimo budas: {self.apmokejimo_budas}, igyta preke/paslauga {self.preke_paslauga}"
