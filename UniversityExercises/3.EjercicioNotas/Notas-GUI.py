from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from operator import itemgetter

#Función Salir del aplicativo
def salir():
    raiz.destroy()

def borrar():
    reporteE.config(state="normal")
    reporteE.delete("1.0","end")
    reporteE.config(state="disable")
    reporteOrdenadoT.config(state="normal")
    reporteOrdenadoT.delete("1.0","end")
    reporteOrdenadoT.config(state="disable")
    varPromedio.set("")
    varNumeroE.set("")
    varAprobados.set("")
    varReprobados.set("")
    
####################################################
def principal():
    numE = simpledialog.askinteger("Número estudiantes", "Ingrese la cantidad de estudiantes:")
    
    while numE <= 0:
        messagebox.showerror(title="Error", message="Erro, la cantidad debe ser positiva.")
        numE = simpledialog.askinteger("Número estudiantes", "Ingrese la cantidad de estudiantes:")
    
    nombres = [None] * numE
    notas = [0.0] * numE
    i = 0
    
    while i < numE:
        nombres[i] = simpledialog.askstring("Nombre", "Escriba el nombre:")
        nota = simpledialog.askfloat("Notas", "Escribas la nota:")
        
        while nota < 0 or nota > 5:
            messagebox.showerror(title="Error", message="Ingresar una nota entre 0.0 y 5.0")
            nota = simpledialog.askfloat("Notas", "Escribas la nota:")
            
        notas[i] = nota
        i += 1
        
    varNumeroE.set(numE)
    
    prom = calcularPromedio(notas)
    varPromedio.set(prom)
    
    reporte = generarReporte(nombres, notas) 
    
    ordenamientoNumericoAscendente(notas, nombres)
    reporte2 = generarReporte(nombres, notas)
    
    neAprobados = calcularAprobados(notas)
    varAprobados.set(neAprobados)
    
    neReprobados = calcularReprobados(notas)
    varReprobados.set(neReprobados)
    
    
    reporteE.config(state="normal")
    reporteE.insert(INSERT, reporte)
    reporteE.config(state="disable")
    
    reporteOrdenadoT.config(state="normal")
    reporteOrdenadoT.insert(INSERT, reporte2)
    reporteOrdenadoT.config(state="disable")
    

####################################################
def calcularPromedio(notas):
    tPromedio = 0
    ctrNotas = 0
    
    while ctrNotas < len(notas):
        tPromedio += notas[ctrNotas]
        ctrNotas += 1
        
    tPromedio /= len(notas)
    return tPromedio

#####################################################
def generarReporte(nombres, notas):
    c = 0
    r = ""

    while c < len(notas):
        r += nombres[c] + "\t" + str(notas[c]) + "\n"
        c += 1
    
    return r

#####################################################
def ordenamientoNumericoAscendente(c, n):
    tempC = 0
    tempN = ""
    i = 0

    while i < len(c) - 1:
        j = 0

        while j < len(c) - 1 - i:
            if c[j] > c[j+1]:
                tempC = c[j]
                c[j] = c[j+1]
                c[j+1] = tempC

                tempN = n[j]
                n[j] = n[j+1]
                n[j+1] = str(tempN)

            j += 1
        i += 1

#####################################################
def calcularAprobados(notas):
    neAp = 0
    c = 0
    
    while c < len(notas):
        if notas[c] >= 3.0:
            neAp += 1
        
        c += 1
        
    return neAp
    
#####################################################
def calcularReprobados(notas):
    neRep = 0
    c = 0

    while c < len(notas):
        if notas[c] < 3.0:
            neRep += 1

        c += 1

    return neRep

#Interfaz Gráfica de usuario
raiz = Tk()
#raiz.resizable(0,0)
raiz.title("Notas Estudiantes")

#contenedor Botones
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10, padx = 10)

numeroELabel = Label(marco1, text="Número de estudiantes:").grid(row = 0, column = 0, sticky = "w", padx = 10, pady=5)
varNumeroE = StringVar()
numeroETb = Entry(marco1, width=10, state="disable", textvariable = varNumeroE)
numeroETb.grid(row=0, column = 1, padx = 10, pady=5)

iniciarB = Button(marco1, text="Iniciar", width=12, command=principal)
iniciarB.grid(row=1,column=0,padx=3, pady=3)
salirB = Button(marco1, text="Salir",width=12, command=salir)
salirB.grid(row=1,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Borrar",width=12, command=borrar)
borrarB.grid(row=1,column=2,padx=3, pady=3)


#contenedor Reporte Estudiantes
marco2 = LabelFrame(raiz, text="Reporte de Estudiantes")
marco2.config(bd=3, relief="sunken", padx=15,pady=15)
marco2.pack(pady= 10, padx = 10)

reporteE = Text(marco2)
reporteE.config(state="disable", width=50, height=10)
reporteE.grid(row=0, column=0, columnspan=2)

#contenedor Reporte Ordenados
marco3 = LabelFrame(raiz, text="Reporte de Estudiantes Ordenado")
marco3.config(bd=3, relief="sunken", padx=15,pady=15)
marco3.pack(pady= 10, padx = 10)

reporteOrdenadoT = Text(marco3)
reporteOrdenadoT.config(state="disable", width=50, height=10)
reporteOrdenadoT.grid(row=0, column=0, columnspan=2)

promedioLabel = Label(marco3, text="Promedio del Curso:").grid(row = 1, column = 0, sticky = "e", padx = 10, pady=5)
varPromedio = StringVar()
promedioTb = Entry(marco3, width=10, state="disable", textvariable = varPromedio)
promedioTb.grid(row=1, column = 1, padx = 10, pady=5,sticky = "w")

aprobadosLabel = Label(marco3, text="Número de Estudiantes Aprobados:").grid(row = 2, column = 0, sticky = "e", padx = 10, pady=5)
varAprobados = StringVar()
aprobadosTb = Entry(marco3, width=10, state="disable", textvariable = varAprobados)
aprobadosTb.grid(row=2, column = 1, padx = 10, pady=5,sticky = "w")
aprobadosLabel = Label(marco3, text="Número de Estudiantes Reprobados:").grid(row = 3, column = 0, sticky = "e", padx = 10, pady=5)
varReprobados = StringVar()
reprobadosTb = Entry(marco3, width=10, state="disable", textvariable = varReprobados)
reprobadosTb.grid(row=3, column = 1, padx = 10, pady=5,sticky = "w")

raiz.mainloop()
