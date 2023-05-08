class email:
    __idCuenta = ''
    __dom = ''
    __tipdom = ''
    __contraseña=''
    def __init__(self,idCuenta,dom,tipdom,contraseña):
        self.__idCuenta=idCuenta
        self.__dom=dom
        self.__tipdom=tipdom
        self.__contraseña=contraseña
    def retornaEmail(self):
        return(self.__idCuenta+'@'+self.__dom+'.'+self.__tipdom)
    def getDominio(self):
        return(self.__dom)
    def getContra(self):
        return(self.__contraseña)
    def nuevaContraseña(self,verifcon,ncontra):
        if(verifcon==self.__contraseña):
            self.__contraseña=ncontra
            print("Contraseña cambiada con exito")
        else:
            print("Contraseña actual incorrecta")
    def nuevaCuenta(self,direccion,contraseña):
        x= direccion.split("@")
        idCuenta=x[0]
        pdominio=x[1]
        pdominio2=pdominio.split(".")
        dominio=pdominio2[0]
        tipdom=pdominio2[1]
        nueva_instancia=self.__class__(idCuenta,dominio,tipdom,contraseña)
        return nueva_instancia