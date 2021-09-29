import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
from Automata import analizador
class App:
    def __init__(self,root:tk.Toplevel) -> None:
        #Variables
        self.entrada= ""
        #Ventana
        root.title("Proyecto 2 - 202004724")
        root.config(bg="skyblue")
        #Frames
            #ToolBar
        toolBar = tk.Frame(root,width=700,height=50,bg="grey").grid(row=0,padx=5,pady=5)
            #Cuadro donde irá el código
        codeFrame = tk.Frame(root,width=700,height=300,bg="grey")
        codeFrame.grid(row=1,padx=5,pady=5)
            #Consola
        consoleFrame = tk.Frame(root,width=100,height=100,bg="grey")
        consoleFrame.grid(row=2,padx=5,pady=5)
        
        #Menu
        menubar = Menu(root)
            #Carga y Salir
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.carga)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
            #Analizar
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Analizar", command=self.analizar)
        '''        '''
        menubar.add_cascade(label="Analizar Archivo", menu=editmenu)
            #Reportes
        reportMenu = Menu(menubar, tearoff=0)
        reportMenu.add_command(label="Reporte de Tokens", command=self.donothing)
        reportMenu.add_command(label="Reporte de Errores", command=self.donothing)
        reportMenu.add_command(label="Árbol de Derivación", command=self.donothing)
        menubar.add_cascade(label="Reportes", menu=reportMenu)
        root.config(menu=menubar)

        
        #Botones
        
        buttons = tk.Frame(toolBar,width=700,height=50,bg="grey")
        buttons.grid(row=0,padx=5,pady=5)
        self.label = tk.Label(buttons,text="BIENVENIDO A MI PRORAMA :D",relief=RAISED).grid(row=0,column=0,padx=5,pady=5)
        
        # Consola
        self.text = Text(codeFrame,width=86,height=20)
        self.text.grid(row=0,column=0,padx=5,pady=5)
        # Consola
        self.console = Text(consoleFrame,width=86,height=15)#Ver para que sea solo lectura
        self.console.grid(row=0,column=0,padx=5,pady=5)

    def carga(self):
        try:
            path = filedialog.askopenfilename(filetypes=[('Texto plano', '*.lfp')])
            self.entrada = open(path,"r").read()
            self.text.delete("1.0",END)
            self.text.insert(INSERT,self.entrada)
            messagebox.showinfo("Carga","Carga de archivo exitosa")
        except:
            messagebox.showerror("Error","Error al cargar el archivo")
    def analizar(self):
        text = self.text.get("1.0",END)#Imprime por linneas separado por \n, SUSCEPTIBLE A CAMBIOS POR QUE ES CONSOLA
        for a in text:
            self.console.insert(INSERT,">>>"+a+"\n")
        analizar = analizador()
        analizar.analizar(text)
        messagebox.showwarning("OJO","No hay analizador xd")
    def donothing():
        filewin = tk.Toplevel(root)
        button = tk.Button(filewin, text="Do nothing button")
        button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()