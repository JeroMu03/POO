from manejadorSabor import manejaSaborr
from manejadorHelados import manejadorHel

if __name__ == '__main__':
    listaHel= manejadorHel()
    listaSab= manejaSaborr()
    listaSab.cargaCsv()
    listaSab.test()
    for b in range(3):
        band="FIN"
        i=1
        gramos=int(input("Ingrese los gramos:"))
        sabor=input("Ingrese sabor que va a pedir:")
        listaHel.agregarSabor(listaSab,sabor)
        sabor=input("Ingrese sabor que va a pedir:")
        listaHel.agregarSabor(listaSab,sabor)
        sabor=input("Ingrese sabor que va a pedir:")
        listaHel.agregarSabor(listaSab,sabor)
        sabor=input("Ingrese sabor que va a pedir:")
        listaHel.agregarSabor(listaSab,sabor)
        listaHel.cerrarPedido(gramos)
    listaHel.test()