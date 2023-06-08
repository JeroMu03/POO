class Sabor:
    __idSabor=0
    __ing=""
    __nombSab=""
    
    def __init__(self,idSabor,ing,nombSab):
        self.__idSabor=idSabor
        self.__ing=ing
        self.__nombSab=nombSab
    
    def getNom(self):
        return self.__nombSab
    
    def __str__(self):
        return ("Codigo sabor: {} \n Nombre: {}".format(self.__idSabor, self.__nombSab))
    