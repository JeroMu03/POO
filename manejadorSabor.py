import csv
from sabor import Sabor
class manejaSaborr:
    
    def __init__(self):
        self.__sabores=[]
    
    def agregarSabor(self,unSabor):
        self.__sabores.append(unSabor)
    
    def cargaCsv(self):
        path=r"C:\Users\jeron\Documents\Facultad\Segundo Año\POO\Unidad 3\Ejercicio2\sabores.csv"
        archivo=open(path)
        reader=csv.reader(archivo, delimiter=',')
        for fila in reader:
            unSabor = Sabor(fila[0],fila[1],fila[2])
            self.agregarSabor(unSabor)
        archivo.close()
    
    def test(self):
        for i in range(len(self.__sabores)):
            print(self.__sabores[i])
    
    def busqSabor(self,nom):
        i=0
        band=None
        while (i<=len(self.__sabores) and self.__sabores[i].getNom() != nom):
            i=i+1
        if(i<len(self.__sabores)):
            band=self.__sabores[i]
            return band