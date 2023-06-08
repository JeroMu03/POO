import ManejF
if __name__=='__main__':
    a=ManejF.ManejadorFac()
    a.CargaFacu()
    print("Ingresar codigo de carrera:")
    #cod=input("Ingrese codigo:")
    #a.BusqCod(cod)
    nom=input("Ingresar nombre carrera: ")
    a.BusqCarrera(nom)