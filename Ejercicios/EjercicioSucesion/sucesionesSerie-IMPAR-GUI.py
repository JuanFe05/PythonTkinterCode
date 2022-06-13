from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#Función Salir del aplicativo
def salir():
    raiz.destroy()

def borrar():
    reporteT.config(state="normal")
    reporteT.delete("1.0","end")
    reporteT.config(state="disable")
    
########Funcion Calcular Susecion 1########
def calcularSucesion1(n):
    t = 1
    v = 1
    s1 = "Sucesion 1: "
    
    while t <= n:
        if (v % 7 == 0 and v % 9 == 0):
            s1 = s1 + str(v) + " "
            t = t + 1
    
        v = v + 1
        
    return s1

########Funcion Calcular Susecion 2########
def calcularSucesion2(n):
    t = 1
    s2 = "Sucesion 2: "

    while t <= n:
        s2 = s2 + str(2 * t + 1)
        t = t + 1

    return s2

########Funcion Calcular serie 1########
def calcularSerie(n):
    ct = 0
    d = 2
    t = 0
    vs = 0

    while ct < n:
        t = 1 / d
        d = d * 2
            
        if (ct % 2 == 0):
            vs = vs + t
            
        else:
            vs = vs - t
            
        ct = ct + 1

    return vs
    
########Funcion principal########
def principal():
    n = simpledialog.askinteger("número", "Ingrese un numero positivo :")
    reporte = ""
    
    while n <= 0:
        n = simpledialog.askinteger("número", "Ingrese un numero positivo :")
        
    su1 = calcularSucesion1(n)
    valorS1 = calcularSerie(n)
    su2 = calcularSucesion2(n)
    
    reporte = reporte + str(su1) + "\n" + str(su2) + "\n" + str(valorS1)
    
    reporteT.config(state="normal")
    reporteT.insert(INSERT, reporte)
    reporteT.config(state="disable")
        

#Interfaz Gráfica de usuario
raiz = Tk()
raiz.resizable(0,0)
raiz.title("Sucesiones y Serie - IMPAR")

#contenedor Botones
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10, padx = 10)

numeroTLabel = Label(marco1, text="Número de terminos:").grid(row = 0, column = 0, sticky = "w", padx = 10, pady=5)
varNumeroT = StringVar()
numeroTTb = Entry(marco1, width=10, state="disable", textvariable= varNumeroT)
numeroTTb.grid(row=0, column = 1, padx = 10, pady=5)

inicioB = Button(marco1, text="Mostrar resultados", command=principal)
inicioB.grid(row=1,column=0,padx=3, pady=3)
salirB = Button(marco1, text="Salir",width=12, command=salir)
salirB.grid(row=1,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Borrar",width=12, command=borrar)
borrarB.grid(row=1,column=2,padx=3, pady=3)


#contenedor Reporte
marco2 = LabelFrame(raiz, text="Resultados")
marco2.config(bd=3, relief="sunken", padx=15,pady=15)
marco2.pack(pady= 10, padx = 10)

reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0, columnspan=2)



raiz.mainloop()
