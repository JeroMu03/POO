from helado import hel
from manejadorSabor import manejaSaborr
class manejadorHel:
    def __init__(self):
        self.__listahel = []
        self.__sabores=[]
    
    def agregarHelado(self,unHelado):
        self.__listahel.append(unHelado)

    def agregarSabor(self,lista,nom):
        band=lista.busqSabor(nom)
        print("a")
        print(band)
        if(band!=None):
            self.__sabores.append(band)
        else:
            print("No se encontro el sabor")
    
    def cerrarPedido(self,gramos):
        unHelado=hel(gramos,self.__sabores)
        print(unHelado)
        self.agregarHelado(unHelado)
        self.__sabores=[]
    
    def test(self):
        for i in range(len(self.__listahel)):
            print(self.__listahel[i])