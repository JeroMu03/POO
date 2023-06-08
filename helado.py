class hel:
    __gramos=0
    __precio=0.0
    __sabores=list
    
    def __init__(self,gramos,sabores):
        self.__gramos=gramos
        self.__precio=self.detPrecio(gramos)
        self.__sabores=sabores
    
    def detPrecio(self,gramos):
        precio=0
        if gramos == 100:
            precio = 200
        if gramos == 150:
            precio = 250
        if gramos == 250:
            precio = 400
        if gramos == 500:
            precio = 700
        if gramos == 1000:
            precio = 1300
        return precio

    def __str__(self):
        return ("Gramos: {} \n Precio: {} \n Sabores: {}".format(self.__gramos, self.__precio,self.__sabores))
        