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
def ejecutar(opcion, opciones):
    opciones[opcion][1]()
def mostrar_menu(opciones):
     print("\nMENU OPCIONES")
     for clave in sorted(opciones):
         print(f'{clave}) {opciones[clave][0]}')
def leeropcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
def generar_menu(opciones, salida):
    opcion=None
    while opcion != salida:
        mostrar_menu(opciones)
        opcion= leeropcion(opciones)
        ejecutar_opcion(opcion, opciones)
def menu():
    opciones ={
    '0':('0 Salir', salir),
    '1':('1 Crear Mail',crearMail),
    '2':('2 Cambiar Contraseña',cambiarContraseña),
    '3':('3 Crear Mail con Direccion',crearMailDirec),
    '4':('4 Crear Mail con csv',crearMailcsv),
    }
    generar_menu(opciones,'0')
if __name__ == "__main__":
    crearMailDirec()
    menu()
    