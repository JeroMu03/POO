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
    def cantidadTotalMillas(self):
        return(self.__millas)
    def acumularMillas(self,reco):
        self.__millas=self.__millas+reco
        return(self.__millas)
    def canjearMillas(self,canj):
        if(self.__millas>=canj):
            self.__millas=self.__millas-canj
            print("Millas canjeadas")
            print("Millas restantes:",self.__millas)
        else:
            print("No se dispone de las millas suficientes")