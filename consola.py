#Se realiza la imporacion de la clase Huron y Boa constrictor
from huron import Huron
from boa_constrictor import Boa_constrictor

"""
Boa_constrictor
nombre(str): Nombre de la Boa constrictor
peso (int): Peso de la Boa constrictor.
edad (float): Edad de la Boa constrictor
pais origen (str): pais de origen de la Boa constrictor
impuesto (float): valor del impuesto para poder importar la Boa constrictor
ratones_comidos (int): ratones_comidos por la Boa constrictor
"""
#Se crean objetos objetos de tipo Boa constrictor y se asignan valores
boa_constrictor1 = Boa_constrictor("Boa001", 50, 5, "EEUU", 0.17, 5)
boa_constrictor2 = Boa_constrictor("Boa002", 60, 6, "Europa", 0.20, 9)

#Se muestran por pantalla los valores de los objetos boa_constrictor1 y boa_constrictor2
print(f"Información de la Boa_constrictor 1 {boa_constrictor1.__dict__}")

print(f"Información de la Boa_constrictor 2 {boa_constrictor2.__dict__}")

flete_boa = boa_constrictor1.calcular_flete()
#Se realiza el calculo y se muestra por pantalla el valor del flete por la importación del animal exotico
print(f"El valor del flete que debe pagar por la importación de la boa constrictor es el siguiente: {flete_boa}")

#Se muestra el sonido que realiza la boa constrictor 
print(f"El sonido que emite la boa constrictor es el siguiente: {boa_constrictor1.hacer_sonido()}")

#Se agregan ratones comidos
boa_constrictor1.agrega_ratones_comidos()
boa_constrictor2.agrega_ratones_comidos()

#Se muestran por pantalla los nuevos valores de los objetos boa_constrictor1 y boa_constrictor2
print(f"Información de la Boa_constrictor 1 {boa_constrictor1.__dict__}")

print(f"Información de la Boa_constrictor 2 {boa_constrictor2.__dict__}")



"""
Huron
nombre(str): Nombre del huron
peso (int): Peso del huron
edad (float): Edad del huron
pais origen (str): pais de origen del huron
impuesto (float): valor del impuesto para poder importar el huron
"""


#Se crean objetos objetos de tipo huron y se asignan valores
huron1 = Huron("huron001", 10, 5, "España", 0.18)
huron2 = Huron("huron002", 8, 4, "Venezuela", 0.15)

#Se muestran por pantalla los valores de los objetos huron1 y huron2
print(f"Información del huron1 {huron1.__dict__}")

print(f"Información del huron2 {huron2.__dict__}")

#Se muestra el sonido que realiza el huron 
print(f"El sonido que emite el huron es el siguiente: {huron1.hacer_sonido()}")

flete_huron = huron1.calcular_flete()
#Se realiza el calculo y se muestra por pantalla el valor del flete por la importación del animal exotico
print(f"El valor del flete que debe pagar por la importación del huron es el siguiente: {flete_huron}")

