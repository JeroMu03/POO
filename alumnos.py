class Alumnos:
    __dni=0
    __apellido=""
    __nombre=""
    __carrera=""
    __cursa=0
    
    def __init__(self,dni,apellido,nombre,carrera,cursa):
        self.__dni=dni
        self.__apellido=nombre
        self.__nombre=nombre
        self.__carrera=carrera
        self.__cursa=cursa
        
    def getnombre(self):
        return self.__nombre
    
    def getcursa(self):
        return self.__cursa
    
    def getdni(self):
        return self.__dni
        