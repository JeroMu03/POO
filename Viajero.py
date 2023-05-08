class viajero:
    __num=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas=0
    def __init__(self,num,dni,nombre,apellido,millas):
            self.__num=num
            self.__dni=dni
            self.__nombre=nombre
            self.__apellido=apellido
            self.__millas=millas
            
    def getMillas(self):
        return self.__millas
            
    def cantidadTotalMillas(self):
        return(self.__millas)
    
    def acumularMillas(self,reco):
        self.__millas=self+reco
        return(self.__millas)
    
    def canjearMillas(self,canj):
        if(self.__millas>=canj):
            self.__millas=self-canj
            print("Millas canjeadas")
            print("Millas restantes:",self.__millas)
        else:
            print("No se dispone de las millas suficientes")
            
    def __gt__(self,other):
        return(self.__millas>other.__millas)
    
    def __add__(self,other):
        return(self.__millas+other)
    
    def __sub__(self,other):
        return(self.__millas-other)
    
    def __str__(self):
        return ("El viajero con mayor cantidad de puntos {}".format(self.__nombre))
    
    def __eq__(self,other):
        return (self.__millas == int(other))