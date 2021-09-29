import Token 

class analizador:
    def __init__(self) -> None:
        self.__lexema=""
        self.__estado =0
        self.__tokens = []
        self.__errores = []
        self.__simbolo = {"=":"igual",";":"PuntoComa","{":"AbreLlave","[":"AbreCorchete","]":"CierraCorchete","}":"CierraLLave",",":"Coma","(":"AbreParen",")":"CierraParen"}


    def analizar(self,entrada):
        i=0
        while i < len(entrada):
            actual = entrada[i] #actual ya es un caracter
            if self.__estado == 0:
                if actual.isalpha():
                    self.__lexema+=actual
                    self.__estado = 1
                    print("Letra")
                    i+=1
                elif actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=2
                    i+=1
                elif actual == "\"":
                    self.__lexema+=actual
                    self.__estado=3
                    i+=1
                elif actual == "#":
                    self.__lexema+=actual
                    self.__estado=4
                    i+=1
                elif not self.__simbolo.get(actual) == None:
                    self.__lexema+=actual
                    self.__estado=5
                    i+=1
                elif actual == "\'":
                    self.__lexema+=actual
                    self.__estado=6
                    i+=1
                else:
                    print("El símbolo: "+actual+" no pertenece al lenguaje")
                    self.__estado=0
                    self.__lexema=""
                    i+=1
            elif self.__estado == 1:
                if actual.isalpha():
                    self.__lexema+=actual
                    self.__estado = 1
                    print("Letra")
                    i+=1
                else:
                    self.__estado = 0
            elif self.__estado == 2:
                print("Espacio")
            elif self.__estado == 3:
                print("Espacio")
            elif self.__estado == 4:
                print("Espacio")
            elif self.__estado == 5:
                print("Espacio")
            elif self.__estado == 6:
                print("Espacio")
            elif self.__estado == 7:
                print("Espacio")
            elif self.__estado == 8:
                print("Espacio")
            elif self.__estado == 9:
                print("Espacio")
            elif self.__estado == 10:
                print("Espacio")
            elif self.__estado == 11:
                print("Espacio")
            elif self.__estado == 12:
                print("Espacio")