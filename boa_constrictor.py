#Se realiza la imporacion de la clase Animal_exotico
from animal_exotico import Animal_exotico

"""
Esta clase representa al animal boa constrictor.

nombre(str): Nombre de la Boa constrictor
peso (int): Peso de la Boa constrictor.
edad (float): Edad de la Boa constrictor
pais origen (str): pais de origen de la Boa constrictor
impuesto (float): valor del impuesto para poder importar la Boa constrictor
ratones_comidos (int): ratones_comidos por la Boa constrictor
"""
#Constructor de la clase Boa Constrictor, la cual hereda a partir de la clase ya definida de Animal_exotico de la cual hereda 
class Boa_constrictor(Animal_exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen:str, impuesto: float, ratones_comidos = 0) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
        #atributo de la clase Boa_Constrictor que permite contar cuantos ratones se ha comido 
        self.ratones_comidos = ratones_comidos


    #Método que agrega un ratón a la cuenta de ratones comidos
    def agrega_ratones_comidos(self, cantidad = 1) -> None:
        #Si el número de ratones comidos es 10, no aumenta el contador
        if self.ratones_comidos < 20:
            self.ratones_comidos += cantidad
        else:
            #Se lanzará un ValueError con el mensaje “Demasiados Ratones!”
            raise ValueError("Demasiados Ratones!")
    

    #Implementación del método hacer_sonido. La Boa hace el sonido “¡Tsss!”
    @staticmethod
    def hacer_sonido () -> str:
        return "¡Tsss!"