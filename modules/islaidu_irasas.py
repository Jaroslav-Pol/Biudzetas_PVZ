
from modules.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __str__(self): #pakeiciam str kitaip nei tevinei klasei
        return f"Islaidos: {self.suma}"
