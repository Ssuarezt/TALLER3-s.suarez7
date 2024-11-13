from boa_constrictor import Boa_constrictor

"""Punto 3 | Prueba y error
Construya una pequeña clase de Guarderia, que tenga a su disposición 2 Boas y 2 hurones. 
Esta clase debe tener la función de alimentar_boa, esta recibirá una de las boas y llamará la función de alimentar en cada una.
Configure con una estructura try-except, de modo que cuando el método de alimentar a la boa se retorne un mensaje que diga 
“La boa está llena” mientras que cuando se pueda alimentar retorne un mensaje que diga “Éxito”. 
También tenga en consideración el caso en que la boa no haya sido asociada y la boa recibida sea None, 
en este caso retorne un mensaje que diga “Esta Boa no existe!”"""

#Clase Guarderia, con boas y hurones 
class Guarderia():
    def __init__(self, lista_boas:list, lista_hurones:list):
        self.lista_boas = lista_boas
        self.lista_hurones = lista_hurones

    #Función de alimentar_boa
    def alimentar_boa(self) -> None:
        #llamará la función de alimentar en cada una
        for boa in self.lista_boas:
            if boa is None:
                raise ValueError("Esta Boa no existe!")
            
            Boa_constrictor.agrega_ratones_comidos(boa)

    


