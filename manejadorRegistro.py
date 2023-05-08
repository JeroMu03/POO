from registro import registro
import csv

class manejadorRegistro:
    
    def __init__(self):
        self.listaRegistro=[[]]
    
    def agregarRegistro(self,dia,unReg):
        self.__listaRegistro(dia).append(unReg)
        
    def agregarRegistroCSV(self):
        archivo = open('registro.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for dias in range(31):
            for fila in reader:
                if(bandera==True):
                    'saltear cabecera'
                    bandera = False
                else:
                    unRegistro=registro(fila[1],fila[2],fila[3])
                    self.__listaRegistro(dias).append(unRegistro)
                    self.__listaRegistro.append([])
        archivo.close() 
    
    
                
                    
