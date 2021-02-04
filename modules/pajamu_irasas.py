
from modules.irasas import Irasas

class PajamuIrasas(Irasas):

    def __str__(self): #pakeiciam str kitaip nei tevinei klasei
        return f"Pajamos: {self.suma}"