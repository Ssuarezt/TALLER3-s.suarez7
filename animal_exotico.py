
from animal import Animal

"""
    Esta clase representa a un animal exotico.

    Atributos:
        nombre(str): Nombre del animal exotico.
        peso (int): Peso del animal exotico.
        edad (float): Edad del animal exotico.
        pais origen (str): pais de origen del animal exotico
        impuesto (float): valor del impuesto para poder importar el animal exotico
"""
# Constructor de la clase Animal_exotico, la cual hereda a partir de la clase ya definida de Animal
class Animal_exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen:str, impuesto: float) -> None:
        super().__init__(nombre, peso, edad)
        #atributos de la clase Animal_exotico (pais_origen (str) e impuestos (float))
        self.pais_origen = pais_origen
        self.impuesto = impuesto

    #Methods
    def hacer_sonido(self) -> str:
        pass


    """método llamado calcular_flete que multiplica los impuestos por el peso del animal 
    para saber cuál es el costo de importar a este animal"""
    def calcular_flete (self) -> float:
        if self.peso > 0:
            return round(self.peso * self.impuesto,2)
        else:
            print("peso debe ser mayor que cero")
    
    # Getters y Setters
    @property
    def pais_origen(self) -> str:
        """ Devuelve el valor del atributo privado 'pais_origen' """
        return self.__pais_origen
    
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'pais_origen'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__pais_origen = value
        else:
            raise ValueError('Expected str')
        
    @property
    def impuesto(self) -> float:
        """ Devuelve el valor del atributo privado 'impuesto' """
        return self.__impuesto
    
    @impuesto.setter
    def impuesto(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'impuesto'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self.__impuesto = value
        else:
            raise ValueError('Expected float')

