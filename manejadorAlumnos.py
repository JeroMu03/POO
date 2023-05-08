import numpy as np
from alumnos import Alumnos
import csv

class ManejadorAlumnos:
    def _init_(self):
        self.listaalumnos = np.empty((0,), dtype=Alumnos)

    def CargaArreglo(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera=True
        for datos in reader:
            if bandera:
                #salta cabecera
                bandera = not bandera
            else:
                dni = int(datos[0])
                apellido = datos[1]
                nombre = datos[2]
                carrera = datos[3]
                año = int(datos[4])
                unAlumno= Alumnos(dni, apellido, nombre, carrera, año)
                self = np.append(self, unAlumno)
        print(self.alumnos)
    
    def getLista(self):
        return self.alumnos