class materia:
    __dni=0
    __nommat=""
    __fecha=""
    __nota=0
    __aprobacion=''
    
    def __init__(self,dni,nommat,fecha,nota,aprobacion):
        self.__dni=dni
        self.__nommat=nommat
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
    
    def getaprobacion(self):
        return self.__aprobacion
    
    def getNota(self):
        return self.__nota
    
    def getFecha(self):
        return self.__fecha
    
    def getMat(self):
        return self.__nommat
    
    def getdni(self):
        return self.__dni
    