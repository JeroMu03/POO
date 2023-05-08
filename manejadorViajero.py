from Viajero import viajero
import csv

class manejadorViajero:
    def __init__(self):
        self.__listaViajeros=[]
    
    def agregarViajero(self, unViajero):
        self.__listaViajeros.append(unViajero)
    
    def getListaViajeros(self):
        return self.__listaViajeros
    
    def mostrarViajeros(self):
        for viajeros in self.__listaViajeros():
            viajeros.mostrarMillas
            
    def agregarViajeroCSV(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if(bandera==True):
                'saltear cabecera'
                bandera = False
            else:
                unViajero=viajero(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
                self.agregarViajero(unViajero)
        archivo.close()
    
    def getUnViajero(self,indice):
        return self.__listaViajeros[indice]