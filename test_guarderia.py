import unittest
from boa_constrictor import Boa_constrictor
from huron import Huron
from guarderia import Guarderia

class test_guarderia(unittest.TestCase):

    def test_alimentar_boa(self):
        #Se crea objeto de tipo Boa constrictor y se asignan valores: nombre, peso, edad, pais, impuesto, ratones comidos
        boa_constrictor1 = Boa_constrictor("Boa001", 50, 5, "EEUU", 0.17, 5)
        boa_constrictor2 = Boa_constrictor("Boa002", 60, 6, "Europa", 0.20, 10)
        huron1 = Huron("huron001", 10, 5, "España", 0.18)
        huron2 = Huron("huron002", 8, 4, "Venezuela", 0.15)
        lista_boas = [boa_constrictor1,boa_constrictor2]
        lista_hurones = [huron1, huron2]
        guarederia = Guarderia(lista_boas, lista_hurones)
        print(f"Información de la guarderia {guarederia.__dict__}")
        
        try:
            resultado = Guarderia.alimentar_boa(guarederia)
            print(f"Éxito {resultado}")
        except ValueError as e:
            print(f"La boa está llena {e}")        

if __name__ == '__main__':
    unittest.main()