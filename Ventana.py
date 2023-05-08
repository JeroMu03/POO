class Ventana:
    __titulo =''
    __xsupizq=0
    __ysupizq=0
    __xinfder=500
    __yinfder=500
    def __init__(self,titulo):
        self.__titulo=titulo
        
    def mostrar(self):
        print("(",self.__xsupizq,",",self.__ysupizq,")",",","(",self.__xinfder,",",self.__yinfder,")")
            
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        alto= self.__yinfder-self.__ysupizq
        return alto
    
    def ancho(self):
        ancho= self.__xinfder-self.__xsupizq
        return ancho