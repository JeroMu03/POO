from Mail import email
import csv

class Manejadormail:
    def __init__(self):
        self.__listaMail = []
    
    def agregarMail(self, unMail):
        self.__listaMail.append(unMail)

    def agregarMailcsv(self):
        archivo = open('mails.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if(bandera==True):
                'saltear cabecera'
                bandera = False
            else:    
                x= fila[0].split(';')
                x1= x[0]
                x2= x[1]
                x3= x1.split("@")
                idCuenta=x3[0]
                pdominio=x3[1]
                pdominio2=pdominio.split(".")
                dominio=pdominio2[0]
                tipdom=pdominio2[1]        
                unMail=email(idCuenta, dominio,tipdom,x2)
                self.agregarMail(unMail)
        archivo.close()
        