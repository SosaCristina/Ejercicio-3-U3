from ManejadorPersona import ManejadorP
from ManejadorInscripcion import ManejadorI
from ManejadorTaller import ManejadorT

from ClaseInscripcion import Inscripcion
from ClasePersona import Persona
from ClaseTallerCapacitacion import Taller
import numpy as np
import csv

if __name__=="__main__":
    unaPersona=ManejadorP()
    unaPersona.crear_persona()
    #print(unaPersona)
   
    archivo=open("C:\\Users\\chili\\POO archivos\\Talleres.csv")
    reader=csv.reader(archivo,delimiter=",")
    total=sum(1 for line in reader)
    #print(total)
    archivo.close
    unTaller=ManejadorT(total-1)
    unTaller.crear_taller()
    #unTaller.mostrar()
    
    unaInscripcion=ManejadorI(3,5)
    opcion=0
    def menu():
        opc=int(input("MENU - Seleccione una opcion\n"+
       "1)Realizar inscripcion\n"+
       "2)Consultar inscriptos \n"+
       "3)Registrar pago\n"+
       "4)Guardar inscripcion\n"+
       "5)Finalizar\n"))
        return opc
    while opcion!=5:
        opcion=menu()
        if opcion==1:
            id=input("Ingresar ID del Taller al que se desea inscribir: ")
            verif=unTaller.verificar_vacante(id)
            if verif != None:
                dni=input("Ingresar DNI de persona para inscribir: ")
                p=unaPersona.buscar_dni(dni)
                unaInscripcion.crear_inscripcion(p,verif)
                verif.agregar_inscripcion(unaInscripcion)
                #unaInscripcion.mostrar
        if opcion==2:
            i=input("Ingresar ID del Taller al que se desea consultar inscriptos: ")
            id=unTaller.buscar_taller(i)
            unaInscripcion.consultar_inscriptos(id) 
        if opcion==3:
            dni=input("Ingresar DNI de persona para realizar pago: ")
            p=unaPersona.buscar_dni(dni)
            unaInscripcion.realizar_pago(p)
        if opcion==4:
            unaInscripcion.generar_archivo()
            arch=open("C:\\Users\\chili\\POO archivos\\NuevoArchivo.csv",'r')
            print(arch.read())    
            arch.close

       
    