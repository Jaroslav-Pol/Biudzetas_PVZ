from modules.biudzetas import Biudzetas
from modules.pajamu_irasas import PajamuIrasas

biudzetas = Biudzetas()

# prideti_pajamu_irasa(25)
# prideti_pajamu_irasa(500)
# prideti_islaidu_irasa(200)
# parodyti_ataskaita()
# gauti_balansa()

biudzetas.prideti_pajamu_irasa(25, 'Kazkas', "Skola")
biudzetas.prideti_pajamu_irasa(500, naujas_tipas="Avansas")
biudzetas.prideti_islaidu_irasa(200, "Grynais", "Batonas")
biudzetas.parodyti_ataskaita()
biudzetas.gauti_balansa()
