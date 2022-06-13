from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


def salir():
    raiz.destroy()
    
def borrar():
    reporteT.config(state="normal")
    reporteT.delete("1.0",END)
    reporteT.config(state="disable")
    varCantidad.set("")
    
###########################################################
def principal():
    reporte = ""
    cantidad = 0
    ciudades = []
    temperaturas = []
    
    respuesta = messagebox.askyesno(message="¿Desea Registrar Una Ciudad?", title="Opcion de usuario")
    
    while respuesta == True:
        ciudad = simpledialog.askstring("Nombre Ciudad", "Escriba el nombre de la Ciudad:")
        ciudades.append(ciudad)
        tgc = simpledialog.askfloat("Temperatura", "Ingrese la Temperatura (°C):")
        temperaturas.append(tgc)
        
        while tgc < -30 or tgc > 100:
            messagebox.showerror(title="Error", message="Temperatura debe estar entre -30° y 100°")
            tgc = simpledialog.askfloat("Temperatura", "Ingrese la Temperatura (°C):")
            
        temperaturas[cantidad] = calcularAjuste(tgc)
        cantidad += 1
        
        respuesta = messagebox.askyesno(message="¿Desea Registrar Una Ciudad?", title="Opcion de usuario")
    
    if len(ciudades) > 0:
        ordenamientoBurbuja(temperaturas, ciudades)
        reporte = generarReporte(ciudades, temperaturas)
        
    varCantidad.set(cantidad)
    
    reporteT.config(state="normal")
    reporteT.insert(INSERT, reporte)
    reporteT.config(state="disable")
    
###########################################################
def calcularAjuste(temperaturaGC):
    temperaturaF = 1.8 * temperaturaGC + 32
    
    if temperaturaGC >= 18 and temperaturaGC <= 25:
        temperaturaF = temperaturaF - 2
        
    elif temperaturaGC < 18:
        temperaturaF = temperaturaF - 3
        
    elif temperaturaGC > 25:
        temperaturaF = temperaturaF - 5
        
    return temperaturaF
    
###########################################################
def generarReporte(ciudades, temperaturas):
    r = "Ciudad Temperatura °F"
    contador = 0
    
    while contador < len(temperaturas):
        if temperaturas[contador] < 80:
            r = r + "\n" + str(ciudades[contador]) + "\t" + str(temperaturas[contador])
        
        contador += 1
    
    return r

###########################################################
def ordenamientoBurbuja(t, c):
    tempT = 0
    tempC = ""
    i = 0
    
    while i < len(t) - 1:
        j = 0
        
        while j < len(t) - 1 - i:
            if t[j] > t[j+1]:
                tempT = t[j]
                t[j] = t[j+1]
                t[j+1] = tempT

                tempC = c[j]
                c[j] = c[j+1]
                c[j+1] = str(tempC)
            
            j += 1
        i += 1

#*********INICIO**********
raiz = Tk()
raiz.title("Registro de temperaturas")
raiz.resizable(0,0)

#Contenedor1
ventana1 = Frame(raiz,bd=5, relief="sunken")
ventana1.pack(padx=10, pady=10)
bIniciar = Button(ventana1,text="Iniciar", command=principal)
bIniciar.grid(row=0, column=0, padx = 10, pady=10)
bBorrar = Button(ventana1,text="Borrar", command=borrar)
bBorrar.grid(row=0, column=1,padx = 10, pady=10)
bSalir = Button(ventana1,text="Salir", command=salir)
bSalir.grid(row=0, column=2,padx = 10, pady=10)


#Contenedor3
ventana3 = LabelFrame(raiz,text="Reporte de ciudades con temperatura inferior a 80°F ",bd=5, relief="sunken")
ventana3.pack(padx=10, pady=10)

reporteT = Text(ventana3)
reporteT.config(width=40,height=10, state="disable")
reporteT.grid(row=0, column=0,columnspan=2, padx=5, pady=5)
cantidadLabel = Label(ventana3, text="Cantidad de ciudades registradas: ").grid(row=1, column=0)
varCantidad = StringVar()
cantidadTb = Entry(ventana3, textvariable= varCantidad,state="disable")
cantidadTb.grid(row=1, column=1)

raiz.mainloop()

#*********FIN**********
