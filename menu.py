from planAhorro import planahorro
from manejadorAhorro import manejadorPlanAhorro
import sys

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

    def Gestopc(self,opc,lista):

        func =self.__Switch.get(opc, lambda: print("Opción no válida"))
        func(lista)

    def opc1(self,lista):

        for i in range(len(lista.getLista())):
            unPlan=lista.getLista()[i]
            print(unPlan)
            nvValor=input("Ingrese el valor nuevo:")
            unPlan.actualizarValor(nvValor)

  
    def opc2(self,lista):
        valorb=int(input("Ingrese valor a buscar:"))
        i=0
        print(lista.getLista()[i].getValor())
        while((i<len(lista.getLista())) and (lista.getLista()[i].getValor()!=valorb)):
            i+=1
        if (i<len(lista.getLista())):
            print(lista.getLista()[i])
        else:
            print("No se encontro")
    
    def opc3(self,lista):
        valor=int(input("Ingrese valor:"))
        lista.getPlanBarato()
        