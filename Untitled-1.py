class minovia:
    __belleza = 1000
    __doritos = 0
    def inic(self, x1,y2):
        self.__belleza += x1
        self.__doritos += y2
    def mostrarDatos(self):
        print("(belleza,doritos)=(",self.__belleza,',',self.__doritos,"))")
    
if __name__=='__main__':
    mar = minovia()
    mar.inic(1000,5)
    mar.mostrarDatos()
