from Viajero import viajero
from manejadorViajero import manejadorViajero
from menu import Menu
if __name__ == '__main__':
    listaviajero=manejadorViajero()
    listaviajero.agregarViajeroCSV()
    print(range(listaviajero))
    m= Menu()
    m.run(listaviajero)