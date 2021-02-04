from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, nauja_suma, naujas_siuntejas="Darbovete", naujas_tipas='Atlyginimas'):
        irasas = PajamuIrasas(nauja_suma, naujas_siuntejas, naujas_tipas)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, nauja_suma, naujas_apmokejimo_budas="Kortele", nauja_preke_paslauga='Maistas'):
        irasas = IslaiduIrasas(nauja_suma, naujas_apmokejimo_budas, nauja_preke_paslauga)
        self.zurnalas.append(irasas)

    def parodyti_ataskaita(self):
        print("pajamu/islaidu sarasas")
        for irasas in self.zurnalas:
            print(irasas)

    def gauti_balansa(self):
        print('Balansas: ')
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        print(balansas)
