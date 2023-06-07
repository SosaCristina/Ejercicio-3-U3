class Persona:
    __nombre=""
    __direccion=""
    __dni=""

    def __init__(self,n,d,doc):
        self.__nombre=n
        self.__direccion=d
        self.__dni=doc

    def __str__(self):
        return "Nombre:{} - Direccion:{} - Dni:{}".format(self.__nombre,self.__direccion,self.__dni)    
    
    def get_dni(self):
        return self.__dni