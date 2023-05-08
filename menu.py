import sys
from manejadorViajero import manejadorViajero
from Viajero import viajero

class Menu:
    def __init__(self):
        self.elecciones = {
            "1" :self.cntTotalMillas,
            "2": self.acumMillas,
            "3" :self.canjMillas,
            "4": self.mayorMillas,
            "5": self.exit
        }
    def mostrarMenu(self):
        print("1: Consultar Cantidad de millas")
        print("2: Acumular millas")
        print("3: Canjear millas")
        print("4: Mayor Millas")
        print("5: Exit")
    
    def run(self,listaviajero):
        numViajero=int(input(("Ingrese el numero de viajero frecuente: ")))
        while True:
            self.mostrarMenu()
            eleccion = input("Elija una opcion:")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion(listaviajero,numViajero)
            else:
                print("No es una eleccion valida".format(eleccion))
    
    def cntTotalMillas(self,listaviajero,numViajero):
        unViajero=listaviajero.getUnViajero(numViajero-1)
        print(unViajero.cantidadTotalMillas())
        
    def acumMillas(self,listaviajero,numViajero):
        unViajero=listaviajero.getUnViajero(numViajero-1)
        acumu=int(input("Ingrese la cantidad de puntos a acumular: "))
        print("La nueva cantidad de millas es de:",unViajero.acumularMillas(acumu))
        
    def canjMillas(self,listaviajero,numViajero):
        unViajero=listaviajero.getUnViajero(numViajero-1)
        canje=int(input("Ingrese la cantidad de puntos a canjear: "))
        unViajero.canjearMillas(canje)
        
    def mayorMillas(self,listaviajero,numViajero):
        aux=listaviajero.getListaViajeros()[0]
        for i in range(len(listaviajero.getListaViajeros())):
            if(listaviajero.getListaViajeros()[i]>aux):
                aux=listaviajero.getListaViajeros()[i]
        print(aux)

    
    def exit(self,listaviajero,numViajero):
        print("Adios.")
        sys.exit(0)