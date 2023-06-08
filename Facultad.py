import Carrera
class Facultades:
    __cod= 0
    __nom= ''
    __dire= ''
    __loc= ''
    __tel= ''
    __carr= list
    def __init__(self, cod, nom, dire, loc, tel):
        self.__cod = cod
        self.__nom = nom
        self.__dire = dire
        self.__loc = loc
        self.__tel = tel
        self.__carr=[]
        
    def agregarCarrera(self, fila):
        unaCarrera=Carrera.Carreras(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        self.__carr.append(unaCarrera)
        
    def getCod(self):
        return self.__cod
    
    def facuEnc(self):
        print("Nombre facultad:",self.__nom)
        print("Carreras:")
        self.mostrarCarreras()
        
    def busqCarr(self, nom):
        i=0
        band=False
        while (i<=len(self.__carr) and self.__carr[i].getNom() != nom):
            i=i+1
        if (i<=len(self.__carr)):
            print("Codigo de carre:",self.getCodCarra(i))
            band=True
        return band
    
    def getCodCarra(self,i):
        return self.__cod + self.__carr[i].getCodF()
            
    def mostrarCarreras(self):
        for i in range(len(self.__carr)):
            print("Nombre carrera:",self.__carr[i].getNom())
            print("Duracion de la carrera:",self.__carr[i].getDur())
    
    def getNom(self):
        return self.__nom
    
    def getLoc(self):
        return self.__loc
    
    def __str__(self):
        return ("Codigo: {}, Nombre: {}, Direccion: {}, Localidad: {}, Telefono: {}, Carrera {}".format(self.__cod, self.__nom, self.__dire, self.__loc, self.__tel, self.__carr))