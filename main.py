from Conjunto import cnj
from menu import Menu
if __name__ == '__main__':
    lista=list(input("Ingrese los numeros:"))
    conjunto2=cnj(lista)
    lista1=list(input("Ingrese los numeros:"))
    conjunto1=cnj(lista1)
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
        

         mnu.Gestopc(ans,conjunto1,conjunto2)

         if(ans == '4'):

             band = True