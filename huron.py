#importa la clase Animal_exotico
from animal_exotico import Animal_exotico
"""
Esta clase representa al animal huron.

nombre(str): Nombre del huron
peso (int): Peso del huron
edad (float): Edad del huron
pais origen (str): pais de origen del huron
impuesto (float): valor del impuesto para poder importar el huron

"""
#Constructor de la clase Huron, la cual hereda a partir de la clase ya definida de Animal_exotico 
class Huron(Animal_exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen:str, impuesto: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
        
    #Implementación del método hacer_sonido. El Hurón hace “¡Eek Eek!”
    @staticmethod
    def hacer_sonido () -> str:
        return "¡Eek Eek!"