from planAhorro import planahorro
import csv

class manejadorPlanAhorro:
    def __init__(self):
        self.__listaAhorro = []
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            unPlan = planahorro(int(fila[0]),fila[1],fila[2],int(fila[3]))
            self.agregarPlanAhorro(unPlan)
            print(unPlan)
        archivo.close()
    
    def getLista(self):
        return self.__listaAhorro
    
    def agregarPlanAhorro(self,unPlan):
        self.__listaAhorro.append(unPlan)
    
    def getUnPlanAhorro(self,indice):
        return self.__listaAhorro[indice]

    def getPlanBarato(self,valor):
        for i in range(len(self.__listaAhorro)):
            unPlan = self.getUnPlanAhorro(i)
            if(unPlan.importeCuota()<valor):
                barato=unPlan
                print("Un Plan mas barato que el valor:",valor," es:" , barato)
        
        