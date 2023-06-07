from ClaseTallerCapacitacion import Taller 
import numpy as np
import csv

class ManejadorT:
    __dimension=0
    __incremento=5
    __cantidad=0

    def __init__ (self, dimension,incremento=5):
        self.__tallerC=np.empty(dimension,dtype=Taller)
        self.__cantidad=0
        self.__dimension=dimension

    def agregar(self,unTaller):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__tallerC.resize(self.__dimension)
        self.__tallerC[self.__cantidad]=unTaller
        self.__cantidad+=1

    def crear_taller(self):
        archivo=open("C:\\Users\\chili\\POO archivos\\Talleres.csv")
        reader=csv.reader(archivo,delimiter=",")
        bandera=True
        for fila in reader:
            if bandera:
                "saltear cabecera"
                bandera=not bandera
            else:              
                id=fila[0]
                nombre=fila[1]
                vacante=fila[2]
                monto=fila[3]
                unTaller=Taller(id,nombre,vacante,monto)
                self.agregar(unTaller)
        archivo.close        


    
    def mostrar (self):
        for t in self.__tallerC:
            print(t)

    def __str__(self):
        s=""
        for arre in range(self.__cantidad):
            s+= str(arre) +  "\n"
        return s                    

                    

    def verificar_vacante(self,id):
        i=0
        indice=0
        bandera=False
        while i<len(self.__tallerC) and not bandera:
            if int(id) == int(self.__tallerC[i].getid()):
                bandera=True
                if int(self.__tallerC[i].getvacante()) > int(0):
                    print("Hay vancante disponible")
                    self.__tallerC[i].actualizar_vacante()
                    indice=i
                else:
                    print("No hay vacante disponible")
                    

            else:  
                i+=1
        return self.__tallerC[indice]
    

    def buscar_taller(self,id):
        i=0
        indice=0
        bandera=False
        while i<len(self.__tallerC) and not bandera:
            if int(id) == int(self.__tallerC[i].getid()):
                indice=i
                bandera=True
            else: i+=1
        return self.__tallerC[indice]
    
    
        