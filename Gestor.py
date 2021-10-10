from tkinter import *
class Gestor:
    def __init__(self,tokens,consola) -> None:
        self.__tokens = tokens
        self.__info = []
        self.__consola = consola
        self.cant = 0
        self.llenar()

    def llenar(self):
        i=0
        while i<len(self.__tokens):
            actual = self.__tokens[i]
            if actual.getTipo() == "Tk_claves":
                campos = []
                i+=3
                actual = self.__tokens[i]
                while actual.getTipo()!="Tk_CierraC":
                    if actual.getTipo() != "Tk_Coma":
                        campos.append(actual.getLexema().replace("\"","").strip())
                    i+=1
                    actual = self.__tokens[i]
                self.__info.append(campos)
            elif actual.getTipo() == "Tk_registros":
                registro = []
                i+=4
                actual = self.__tokens[i]
                while actual.getTipo()!="Tk_CierraC":
                    if actual.getTipo() != "Tk_Coma" and actual.getTipo() != "Tk_CierraL" and actual.getTipo() != "Tk_AbreL":
                        registro.append(actual.getLexema().replace("\"","").strip())
                    if actual.getTipo() == "Tk_CierraL":
                        self.__info.append(registro)
                        self.cant+=1
                        registro = []
                    i+=1
                    actual = self.__tokens[i]
            elif actual.getTipo() == "Tk_imprimir":
                self.imprimir(self.__tokens[i+2].getLexema().replace("\"",""))
            elif actual.getTipo() == "Tk_imprimirln":
                self.imprimirln(self.__tokens[i+2].getLexema().replace("\"",""))
            elif actual.getTipo() == "Tk_conteo":
                self.conteo()
            elif actual.getTipo() == "Tk_promedio":
                self.promedio(self.__tokens[i+2].getLexema().replace("\"",""))
            elif actual.getTipo() == "Tk_contarsi":
                self.contarsi(self.__tokens[i+2].getLexema().replace("\"",""),float(self.__tokens[i+4].getLexema()))
            elif actual.getTipo() == "Tk_datos":
                self.datos()
            
            i+=1
        print(self.__info)
    def imprimir(self,cadena):
        self.__consola.insert(INSERT,cadena)
    def imprimirln(self,cadena):
        self.__consola.insert(INSERT,cadena+"\n")
    def conteo(self):
        self.__consola.insert(INSERT,str(self.cant)+"\n")
    def promedio(self,campo):
        i=0
        promedio = 0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        for j in range(1,len(self.__info)):
            promedio+= float(self.__info[j][i])
        promedio = promedio/i
        self.__consola.insert(INSERT,str(promedio)+"\n")  
    def contarsi(self,campo,valor):
        cantidad = 0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        for j in range(1,len(self.__info)):
            if valor == float(self.__info[j][i]):
                cantidad+=1 
        self.__consola.insert(INSERT,str(cantidad)+"\n")  
    def datos(self):
        self.__consola.insert(INSERT,">>>")  
        for linea in self.__info[0]:  
            self.__consola.insert(INSERT,str(linea)+"\t\t")
        
        for i in range(1,len(self.__info)):
            self.__consola.insert(INSERT,"\n>>>") 
            for j in range(len(self.__info[i])):  
                self.__consola.insert(INSERT,self.__info[i][j]+"\t\t")   
        self.__consola.insert(INSERT,"\n")  
          