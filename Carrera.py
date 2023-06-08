class Carreras:
    __codF= ''
    __codC= ''
    __nom= ''
    __fecha= ''
    __dur= ''
    __tit= ''
    def __init__(self, codF, codC, nom, fecha, dur, tit):
        self.__codF = codF
        self.__codC = codC
        self.__nom = nom
        self.__fecha = fecha
        self.__dur = dur
        self.__tit = tit
    
    def getCodF(self):
        return self.__codF
    
    def getNom(self):
        return self.__nom
    
    def getDur(self):
        return self.__dur
    
    def __str__(self):
        return ("CodigoF: {} \n CodigoC: {} \n Nombre: {} \n Fecha: {} \n Duracion: {} \n Titulo: {}".format(self.__codF,self.__codC,self.__nom,self.__fecha,self.__dur, self.__tit ))