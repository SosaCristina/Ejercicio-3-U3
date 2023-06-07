class Inscripcion:
    __fecha=""
    __pago=bool
    __taller=None
    __persona=None

    def __init__(self,f,taller, persona,p=False):
        self.__fecha=f
        self.__pago=p
        self.__taller=taller
        self.__persona=persona

    def __str__(self):
        return ("Fecha:{} - Pago:{} - Taller:{} - Persona:{}".format(self.__fecha,self.__pago,self.__taller,self.__persona))    

    def get_pago(self):
        return self.__pago
    def get_fecha(self):
        return self.__fecha
    def get_taller(self):
        return self.__taller
    def get_persona(self):
        return self.__persona
    def pago (self):
        self.__pago=True
        return self.__pago