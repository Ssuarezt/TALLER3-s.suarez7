import unittest
from huron import Huron

"""Punto 1 | Pruebas unitarias
En primer lugar, construya dos clases que permitan realizar tests sobre las clases de las Boas y de los Hurones. 
Construya pruebas que permitan probar el correcto funcionamiento de:

La función hacer_sonido tanto de Hurones como de Boas
La función calcular_flete tanto de Hurones como de Boas
La función alimentar en las boas."""

class test_hurones(unittest.TestCase):

    #Función hacer_sonido de Hurones
    def test_hacer_sonido_huron(self):
        #Se crea objeto de tipo Huron y se asignan valores
        huron1 = Huron("huron001", 10, 5, "España", 0.18)
        self.assertEqual(huron1.hacer_sonido(),"¡Eek Eek!")


    #Función calcular_flete de Hurones
    def test_calcular_flete_huron(self):
        #Se crea objeto de tipo Huron y se asignan valores: nombre, peso, edad, pais, impuesto
        huron2 = Huron("huron002", 8, 4, "Venezuela", 0.15)
        #self._peso * self._impuesto
        self.assertEqual(huron2.calcular_flete(),2.5)


if __name__ == '__main__':
    unittest.main()