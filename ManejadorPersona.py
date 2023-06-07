from ClasePersona import Persona
import csv

class ManejadorP:
    __listapersonas=[]
    def __init__ (self):
        self.__listapersonas=[]
 
    def agregar (self,unaPersona):
        self.__listapersonas.append(unaPersona)
    def crear_persona (self):
        archivo=open("C:\\Users\\chili\\POO archivos\\Persona.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            nom=fila[0]
            dom=fila[1]
            dni=fila[2]
            unaPersona=Persona(nom,dom,dni)
            
            self.agregar(unaPersona)
        archivo.close    

    def __str__ (self):
        s=""
        for lista in self.__listapersonas:
            s+= str(lista) + "\n"
        return s    
    
    def buscar_dni(self,dni):
        
        i=0
        indice=0
        bandera=False
        while i< len(self.__listapersonas) and not bandera:
            if self.__listapersonas[i].get_dni() == dni:
                bandera=True
                indice=i
            else:
                i+=1
             
        return self.__listapersonas[indice]            
