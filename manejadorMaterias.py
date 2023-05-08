from materias import materia
import csv

class manejadorMateria:
    def __init__(self):
        self.__listaMateria = []
        archivo=open('materiasAprobadas.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if (bandera==True):
                bandera=False
            else:
                unaMateria=materia(int(fila[0]),fila[1],fila[2],int(fila[3]),fila[4])
                self.agregarMateria(unaMateria)
        archivo.close()
    
    def agregarMateria(self,unaMateria):
        self.__listaMateria.append(unaMateria)
    
    def getLista(self):
        return self.__listaMateria