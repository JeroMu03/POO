from Conjunto import cnj
class Menu:

    __Switch = None
    
    def __init__(self):
        self.__Switch = {
            '1' : self.opc1,
            '2' : self.opc2,
            '3' : self.opc3,
        }

    def getSwitch(self):

        return(self.__Switch)

    def Gestopc(self,opc,conjunto1,conjunto2):

        func =self.__Switch.get(opc, lambda: print("Opción no válida"))
        func(conjunto1,conjunto2)

    def opc1(self,conjunto1,conjunto2):
        print("La suma de ambos conjuntos es: {}".format(conjunto1+conjunto2))
  
    def opc2(self,conjunto1,conjunto2):
        print("La resta de ambos conjuntos es: {}".format(conjunto1-conjunto2))
    
    def opc3(self,conjunto1,conjunto2):
        if(conjunto1 == conjunto2):
            print("Los conjuntos son iguales")
        else:
            print("Conjuntos distintos")
