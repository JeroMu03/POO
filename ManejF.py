import csv
import Facultad

class ManejadorFac:
    def __init__(self):
        self.fac=[]

    def CargaFacu(self):
        archivo=open('facultades.csv')
        reader=csv.reader(archivo,delimiter=',')
        i=0
        bandera=True
        for fila in reader:
            if bandera == True:
                i=fila[0]
                codF=fila[0]
                nomF=fila[1]
                dire=fila[2]
                loc=fila[3]
                tel=fila[4]
                facu=Facultad.Facultades(codF,nomF,dire,loc,tel)
                print(facu)
                self.fac.append(facu)
                bandera=False
            else:
                if i==fila[0]:
                    facu.agregarCarrera(fila)
                else:
                    i=fila[0]
                    codF=fila[0]
                    nomF=fila[1]
                    dire=fila[2]
                    loc=fila[3]
                    tel=fila[4]
                    facu=Facultad.Facultades(codF,nomF,dire,loc,tel)
                    print(facu)
                    self.fac.append(facu)
        archivo.close()
        
    def MostrarLista(self):
        for carrera in self.fac:
            print(carrera)
    
    def BusqCod(self,cod):
        i=0
        while(i<=len(self.fac) and self.fac[i].getCod() != cod):
            i=i+1
        if(i<len(self.fac)):
            self.fac[i].facuEnc()

    def BusqCarrera(self,nom):
        i=0
        band=False
        while(i<=len(self.fac) and band==False):
            band=self.fac[i].busqCarr(nom)
            i=i+1
        if(i<len(self.fac)):
            print("Facultad donde se cursa: ",self.fac[i-1].getNom())
            print("Localidad: ",self.fac[i-1].getLoc())
