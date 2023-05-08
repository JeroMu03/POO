from manejadorMaterias import manejadorMateria
from materias import materia
from menu import Menu
from manejadorAlumnos import ManejadorAlumnos

if __name__ == '__main__':
    lista = manejadorMateria()
    listaalum=ManejadorAlumnos()
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
        

         mnu.Gestopc(ans,lista,listaalum)

         if(ans == '4'):

             band = True