class cnj:
    def __init__(self,conjunto):
        self.__conjunto = set(conjunto)
    
    def mostrar(self):
        print(self.__conjunto)
        
    def addConjunto(self,lista):
        self.__conjunto.add(lista)
        print(self.__conjunto)
        
    def __add__(self,other):
        return self.__conjunto|other.__conjunto
    
    def __sub__(self,other):
        return self.__conjunto&other.__conjunto
    
    def __eq__(self,other):
     return self.__conjunto==other.__conjunto