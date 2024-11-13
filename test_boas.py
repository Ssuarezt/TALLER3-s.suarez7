import unittest
from boa_constrictor import Boa_constrictor


"""Punto 1 | Pruebas unitarias
En primer lugar, construya dos clases que permitan realizar tests sobre las clases de las Boas y de los Hurones. 
Construya pruebas que permitan probar el correcto funcionamiento de:

La función hacer_sonido tanto de Hurones como de Boas
La función calcular_flete tanto de Hurones como de Boas
La función alimentar en las boas."""


class test_boas(unittest.TestCase):
        
    #Función hacer_sonido de Boas
    def test_hacer_sonido_boa(self):
        #Se crea objeto de tipo Boa constrictor y se asignan valores
        boa_constrictor1 = Boa_constrictor("Boa001", 50, 5, "EEUU", 0.17, 5)
        self.assertEqual(boa_constrictor1.hacer_sonido(),"¡Tsss!")
       

    #Función alimentar las boas
    def test_alimentar_boa(self):
        #Se crea objeto de tipo Boa constrictor y se asignan valores: nombre, peso, edad, pais, impuesto, ratones comidos
        boa_constrictor2 = Boa_constrictor("Boa002", 60, 6, "Europa", 0.20, 10)
        try:
            boa_constrictor2.agrega_ratones_comidos()
        except Exception as e:
            raise ValueError (f"Error al alimentar la boa {e}")


    #Función calcular_flete de Boas
    def test_calcular_flete_boa(self):
        #Se crea objeto de tipo Boa constrictor y se asignan valores: nombre, peso, edad, pais, impuesto, ratones comidos
        boa_constrictor1 = Boa_constrictor("Boa001", 50, 5, "EEUU", 0.17, 5)
        #self._peso * self._impuesto
        self.assertEqual(boa_constrictor1.calcular_flete(),12.5)
 
 
if __name__ == '__main__':
    unittest.main()