from menu import Menu
from planAhorro import planahorro
from manejadorAhorro import manejadorPlanAhorro

if __name__ == '__main__':
    lista = manejadorPlanAhorro()
    band = False
    while (not band):

         print(''' 
        
         --------- Menu ---------
         >> 1)   Metodo A 
         >> 2)   Metodo B
         >> 3)   Metodo C
         >> 4)   Salir
        
         ''')

         ans = str(input('>> -Ingrese Opcion: '))
         mnu = Menu()
        

         mnu.Gestopc(ans,lista)

         if(ans == '4'):

             band = True