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
        fila =0
        columna =0
        while i < len(entrada):
            actual = entrada[i] #actual ya es un caracter
            if self.__estado == 0:#Estado inicial
                if actual.isalpha():#Enviar a estado para palabras reservadas
                    self.__lexema+=actual
                    self.__estado = 1
                    columna+=1
                    print("Letra")
                    i+=1
                elif actual.isdigit():#Enviar a estado para numeros
                    self.__lexema+=actual
                    self.__estado=2
                    columna+=1
                    i+=1
                elif actual == "\"":#Enviar a estado de Cadena
                    self.__lexema+=actual
                    self.__estado=3
                    columna+=1
                    i+=1
                elif actual == "#":#Enviar a estado para comentario de linea
                    self.__lexema+=actual
                    self.__estado=4
                    columna+=1
                    i+=1
                elif not self.__simbolo.get(actual) == None:#Enviar a estado de símbolos 
                    self.__lexema+=actual
                    self.__estado=5
                    columna+=1
                    #Dudando en quitar i+=1
                elif actual == "\'":#Enviar a estado para comentario multi linea
                    self.__lexema+=actual
                    self.__estado=6
                    columna+=1
                    i+=1
                elif actual == '\n':
                    fila+=1
                    columna = 0
                    i+=1
                elif actual == '\t' or actual == ' ' or actual == '\r'  : #omitir simbolos
                    columna +=1
                    i+=1
                else:
                    print("El símbolo: "+actual+" no pertenece al lenguaje") #aniadir a errores Lexicos
                    self.__estado=0
                    self.__lexema=""
                    columna+=1
                    i+=1
            elif self.__estado == 1:#Estado para palabras reservadas
                if actual.isalpha():
                    self.__lexema+=actual
                    self.__estado = 1
                    columna+=1
                    print("Letra")
                    i+=1
                else:
                    self.__estado = 0 #Aceptarmos la letra (Comprobar si es reservada)(estado=0 y lexema ="" añiadir en el método de tokens)
                    print("Aceptamos la palabra")
            elif self.__estado == 2:#Estado para numeros
                if actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=2
                    columna+=1
                    i+=1
                elif actual ==".":#Para aceptar decimales
                    self.__lexema+=actual
                    self.__estado=7
                    columna+=1
                    i+=1
                else:
                    self.__estado = 0 #Acá aceptamos un número entero
                    print("numero entero")
            elif self.__estado == 3:#Estado de cadenas, LNR
                if actual.isalpha() or actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=3
                    columna+=1
                    i+=1
                elif actual == "\"":#Termina la cadena
                    self.__lexema+=actual
                    self.__estado=5
                    columna+=1
                    #Dudando en quitar i+=1
                else:
                    self.__lexema+=actual
                    self.__estado=3
                    columna+=1
                    i+=1
            elif self.__estado == 4: #Estado de comentarios
                if actual.isalpha() or actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=4
                    columna+=1
                    i+=1
                elif actual == "\n":#Aceptamos el comentario, revisar (aniadir token)
                    self.__estado=0
                    print("aceptarmos el comentario")
                else:
                    self.__lexema+=actual
                    self.__estado=4
                    i+=1
            elif self.__estado == 5:
                if actual == "\"":
                    print("añadir token cadena")
                    self.__estado = 0
                    i+=1
                elif actual == "\'":
                    print("aniadir token de comentario multilinea")
                    self.__estado =0
                    i+=1
                else:
                    print("añadir token de simbolo")
                    self.__estado =0
                    i+=1
            elif self.__estado == 6:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 8
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
            elif self.__estado == 7:
                if actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=9
                    columna+=1
                    i+=1
                else:
                    self.__estado=0
                    print("no hay numero luego de punto")
            elif self.__estado == 8:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 10
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
            elif self.__estado == 9:
                if actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=9
                    columna+=1
                    i+=1
                else:
                    self.__estado=0#aaadir token
                    print("Aceptamos numero decimal")
            elif self.__estado == 10:
                if actual.isalpha() or actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=10
                    columna+=1
                    i+=1
                elif actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 11
                    columna+=1
                    i+=1
                else:
                    self.__lexema+=actual
                    self.__estado=10
                    columna+=1
                    i+=1
            elif self.__estado == 11:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 12
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
            elif self.__estado == 12:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 5
                    columna+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0