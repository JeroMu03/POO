from Mail import email
if __name__=='__main__':
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
    print("Cambiar contraseña, ingrese actual:")
    contraact=input()
    print("Ingrese nueva contraseña:")
    nvcontra=input()
    mail1.nuevaContraseña(contraact,nvcontra)
    print("Ingrese direccion de correo:")
    nvcorreo=input()
    print("Ingrese contraseña para el correo:")
    contranvcorreo=input()
    mail2=mail1.nuevaCuenta(nvcorreo,contranvcorreo)
    print(mail2.retornaEmail())
    