class planahorro:
    __codplans =0
    __modelo=""
    __version=''
    __valor=0
    __cntCuota=60
    __licitar=10
    
    def __init__(self,cod,modelo,version,valor):
        self.__codplans=cod
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValor(self):
        return self.__valor
    
    def importeCuota(self):
        valorCuota=((self.__valor//self.__cntCuota)+self.__valor)*0.1
        return valorCuota
    
    def actualizarValor(self,nvValor):
        self.__valor=nvValor
        print("El valor se actualizo")
    
    def montoLicitar(self):
        valorLicitar=self.importeCuota()*self.__licitar
        return valorLicitar
    
    def cambiarMonto(self,nvMonto):
        self.__licitar=nvMonto
        print("El monto se cambio")
        
    def __str__(self):

        return('>> Codigo: {}\n>> Modelo: {} \n>>Version del Vehiculo: {}\n>> Valor del Vehiculo: {}\n>> Cant de cuotas {}'.format(self.__codplans,self.__modelo,self.__version,self.__valor,self.__cntCuota))