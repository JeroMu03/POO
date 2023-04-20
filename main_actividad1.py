from Mail import email
from manejadorMail import Manejadormail
def salir():
    print("Adios")

def crearMail():
    print("Ingrese Nombre y apellido:")
    nya=input()
    print("Ingrese Id de su mail:")
    idcuen=input()
    print("Ingrese dominio:")
    domi=input()
    print("Ingrese tipo del dominio:")
    tipdom=input()
    print("Ingrese su contraseña:")
    contra=input()
    mail1=email(idcuen,domi,tipdom,contra)
    print("Estimado ", nya, " te enviaremos tus mensajes a la direccion", mail1.retornaEmail())
def cambiarContraseña():
    print("Cambiar contraseña, ingrese actual:")
    contraact=input()
    print("Ingrese nueva contraseña:")
    nvcontra=input()
def crearMailDirec():
    print("Ingrese direccion de correo:")
    nvcorreo=input()
    print("Ingrese contraseña para el correo:")
    contranvcorreo=input()
    mail2=email.nuevaCuenta(nvcorreo,contranvcorreo)
    print(mail2.retornaEmail())
def crearMailcsv():
    listamail= Manejadormail()
    listamail.agregarMailcsv()
    for email in listamail:
        print(email)
switcher ={
    0:salir,
    1:crearMail,
    2:cambiarContraseña,
    3:crearMailDirec,
    4:crearMailcsv,
}
def switch(argument):
    func = switcher.get (argument, lambda:print("Opcion Incorrecta"))

if __name__ == "__main__":
    bandera=False
    while not bandera:
        print("\nMENU OPCIONES")
        print("0 Salir")
        print("1 Crear Mail")
        print("2 Cambiar Contraseña")
        print("3 Crear Mail con Direccion")
        print("4 Crear Mail con csv")
        opcion= int(input("Opcion:"))
        switch(opcion)
        bandera = int(opcion) == 0
    