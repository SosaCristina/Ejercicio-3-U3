from ClaseInscripcion import Inscripcion
import numpy as np

class ManejadorI:
    __dimension=0
    __incremento=5
    __cantidad=0

    def __init__ (self, dimension,incremento=5):
        self.__inscripcion=np.empty(dimension,dtype=Inscripcion)
        self.__cantidad=0
        self.__dimension=dimension

    def agregar(self,unaInscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripcion.resize(self.__dimension)
        self.__inscripcion[self.__cantidad]=unaInscripcion
        self.__cantidad+=1

    def crear_inscripcion (self,unaPersona,unTaller):
        fecha=input("Ingresar fecha de inscripcion:")
        pago=False
        unaInscripcion=Inscripcion(fecha,unTaller,unaPersona,pago)
        print(unaInscripcion)
        self.agregar(unaInscripcion)

    def mostrar (self):
        for i in self.__inscripcion:
            print(i)

    def __str__(self):
        s=""
        for arre in range(self.__cantidad):
            s+= str(arre) +  "\n"
        return s                    
    


    def consultar_inscriptos(self,id):
        for i in range(self.__cantidad):
            if self.__inscripcion[i].get_taller() == id:
                print("Los alumnos inscriptos en ese taller son:{}".format(self.__inscripcion[i].get_persona()))
                     
 
    def realizar_pago(self,unaPersona):
        i=0
        bandera=False
        while i< len(self.__inscripcion) and not bandera:
            if unaPersona == self.__inscripcion[i].get_persona():
                self.__inscripcion[i].pago()
                print("Pago realizado:({})".format(self.__inscripcion[i].get_pago()))
                bandera=True
            else:
                i+=1   


    def generar_archivo(self):
        nuevo_arch=open("C:\\Users\\chili\\POO archivos\\NuevoArchivo.csv",'w')
        nuevo_arch.write("DNI de la persona - Id de taller - fecha - pago\n")
        for i in range(self.__cantidad):
            p=self.__inscripcion[i].get_persona()
            persona=p.get_dni()
            t=self.__inscripcion[i].get_taller()
            taller=t.getid()
            nuevo_arch.write("{} -     {} -   {} -   {}\n".format(persona,taller,self.__inscripcion[i].get_fecha(),self.__inscripcion[i].get_pago()))
        nuevo_arch.close
            

    def mostrar_nuevo(self):
        arch=open("C:\\Users\\chili\\POO archivos\\NuevoArchivo.csv",'r')
        print(arch.read())    
        arch.close
