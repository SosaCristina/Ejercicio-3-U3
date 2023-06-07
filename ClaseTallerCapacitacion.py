
from ClaseInscripcion import Inscripcion
class Taller:
    __id=0
    __nombreT=""
    __vacante: int
    __monto=0
    __inscripciones=None

    def __init__ (self,id,n,v,m):
        self.__id=id
        self.__nombreT=n
        self.__vacante=v
        self.__monto=m
        self.__inscripciones=[]

    def agregar_inscripcion(self,unaInscripcion):
        self.__inscripciones.append(unaInscripcion)    
        

    def getid(self):
        return self.__id
    def getnombre(self):
        return self.__nombreT
    def getvacante(self):
        return self.__vacante
    def getmonto(self):
        return self.__monto
    def actualizar_vacante(self):
        v=int(self.__vacante)-int(1)
        self.__vacante=v
    
    def __str__(self):
        return ("ID:{} - Nombre talle:{} - Cantidad de vacante:{} - Monto:{}".format(self.__id,self.__nombreT,self.__vacante,self.__monto))


        

        