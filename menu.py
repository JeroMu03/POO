from manejadorMaterias import manejadorMateria
from materias import materia
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

    def Gestopc(self,opc,lista,listaalum):

        func =self.__Switch.get(opc, lambda: print("Opción no válida"))
        func(lista,listaalum)

    def opc1(self,lista,listaalum):
        dnib=int(input("Ingrese DNI a buscar:"))
        i=0
        cntapla=0
        cntsinapla=0
        promapla=0
        promsinaplazo=0
        for i in range(len(lista.getLista())):
            if(dnib==lista.getLista()[i].getdni()):
                print("Encontre")
                if(lista.getLista()[i].getNota()<4):
                    promapla=promapla+lista.getLista()[i].getNota()
                    cntapla=cntapla+1
                else:
                    promapla=promapla+lista.getLista()[i].getNota()
                    promsinaplazo=promsinaplazo+lista.getLista()[i].getNota()
                    cntapla=cntapla+1
                    cntsinapla=cntsinapla+1
        promsinaplazo=promsinaplazo/cntsinapla
        promapla=promapla/cntapla
        print("El promedio sin aplazos es de: {} \n El promedio con aplazos es de: {}".format(promsinaplazo,promapla))
  
    def opc2(self,lista,listaalum):
        materia=str(input("Ingrese materia a buscar:"))
        a=0
        for i in range(len(lista.getLista())):
            if(lista.getLista()[i].getMat()==materia):
                a=1
                if(lista.getLista()[i].getNota()>=7 and lista.getLista()[i].getaprobacion()=='P'):
                    b=0
                    while(i<len(listaalum) and lista.getLista()[i].getdni()!=listaalum[b].getdni()):
                        b+1
                    if(b<len(listaalum.getLista())):
                        print("El alumno: {} \n DNI: {} \n Fecha: {} \n Nota {} \n Anio: {}".format(listaalum[b].getnombre(), listaalum[b].getdni(), lista.getLista()[i].getFecha(), lista.getLista()[i].getNota(), lista.getLista()[i].getAnio()))
        if(a==0):
            print("No se encontro la materia")
        
    def opc3(self,conjunto1,conjunto2):
        if(conjunto1 == conjunto2):
            print("Los conjuntos son iguales")
        else:
            print("Conjuntos distintos")