import csv

archivo = open('mails.csv')
reader = csv.reader(archivo, delimiter=',')
print (reader)
bandera = True
for fila in reader:
    if(bandera==True):
        'saltear cabecera'
        bandera = False
    else:    
        x= fila[0].split(';')
        x1= x[0]
        print (x1)
        x2= x[1]
        print (x2)
        x3= x1.split("@")
        idCuenta=x3[0]
        pdominio=x3[1]
        pdominio2=pdominio.split(".")
        dominio=pdominio2[0]
        tipdom=pdominio2[1]
print (idCuenta,dominio,tipdom)