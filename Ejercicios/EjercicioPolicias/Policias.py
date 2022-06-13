#Ejercicio Policias - No se conoce el número de aspirantes
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#Función Salir del aplicativo
def salir():
    raiz.destroy()

#############################
def validarGenero(generoAspirante):
    if generoAspirante.upper() == "M" or generoAspirante.upper() == "F":
        return generoAspirante
    
    elif generoAspirante.upper() != "M" or generoAspirante.upper() != "F":
        while generoAspirante:
            genero = simpledialog.askstring("Genero Aspirante", "Digite un Género Correcto (F-M) :")
            if genero.upper() == "M" or genero.upper() == "F":
                return genero
            
#############################
def validar(estaturaAspirante, edadAspirante):
    if estaturaAspirante >= 1.68 and estaturaAspirante <= 2.80 and edadAspirante >= 18 and edadAspirante <= 25:
        return True
    
    elif estaturaAspirante <= 0 or estaturaAspirante > 2.80:
        while estaturaAspirante:
            estatura = simpledialog.askfloat("Estatura", "Ingrese estatura correcta del Aspirante :")
            if estatura > 0 and estatura <= 2.80:
                return True
    
    elif edadAspirante <= 0 or edadAspirante > 100:
        while edadAspirante:
            edad = simpledialog.askinteger("Edad", "Ingrese edad correcta del Aspirante :")
            if edad > 0 and edad < 100:
                return True        
                
#############################
def evaluarAspirante(genero, estatura, edad):
    global generoAspirante
    generoAspirante = validarGenero(genero)
    validacion = validar(estatura, edad)
    
    if generoAspirante.upper() == "M" and estatura >= 1.75 and edad >= 18 and validacion == True:
        return "Aceptado"
    
    elif generoAspirante.upper() == "F" and estatura >= 1.68 and edad >= 18 and validacion == True:
        return "Aceptado"
    
    else:
        return "No Aceptado"
    
#############################
def principal():
    numeroAspirantes = 0
    
    hombresSeleccionados = 0
    estaturaPromedio = 0
    
    opcion = messagebox.askyesno(message="¿Desea Registrar Un Aspirante?", title="Opcion de usuario")
    reporte = "Nombre\tMensaje\n"
    
    while opcion:
        nombre = simpledialog.askstring("Nombre Aspirante", "Escriba el nombre del Aspirante :")
        genero = simpledialog.askstring("Genero Aspirante", "Digite el genero del Aspirante (F-M) :")
        estatura = simpledialog.askfloat("Estatura Aspirante", "Ingrese la estatura del Aspirante :")
        edad = simpledialog.askinteger("Edad Aspirante", "Ingrese la edad del Aspirante :")
        
        mensaje = evaluarAspirante(genero, estatura, edad)
        
        if mensaje == "Aceptado" and generoAspirante.upper() == "M":
            hombresSeleccionados += 1
            estaturaPromedio = (estaturaPromedio + estatura) / hombresSeleccionados
            varPromedio.set(estaturaPromedio)
        
        numeroAspirantes += 1
        varCantidad.set(numeroAspirantes)
        
        reporte = reporte + nombre + "\t" + mensaje +"\n"
        opcion = messagebox.askyesno(message="¿Desea Registrar Un Aspirante?", title="Opcion de usuario")
    
    reporteT.config(state="normal")
    reporteT.insert(INSERT, reporte)
    reporteT.config(state="disable")

#Interfaz Gráfica de usuario#################################
raiz = Tk()
raiz.title("Aspirantes a Policia")

#contenedor Botones##########################################
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10)

iniciarB = Button(marco1, text="Iniciar", command=principal)
iniciarB.grid(row=0, column=0, padx=3, pady=3)

salirB = Button(marco1, text="Salir", command=salir)
salirB.grid(row=0, column=1, padx=3, pady=3)


#contenedor Resultado#######################################
marco2 = LabelFrame(raiz, text="Reporte Aspirantes")
marco2.config(bd=3, relief="sunken")
marco2.pack(padx=10, pady=10)
reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

promedioALabel = Label(
marco2, text="Promedio de estatura de los hombres seleccionados: ")
promedioALabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")
varPromedio = StringVar()
promedioATb = Entry(marco2, textvariable=varPromedio, state="readonly")
promedioATb.grid(row=1, column=1, padx=5, pady=5, sticky="w")

cantidadALabel = Label(marco2, text="Cantidad de aspirantes evaluados: ")
cantidadALabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")
varCantidad = StringVar()
cantidadATb = Entry(marco2, textvariable=varCantidad, state="readonly")
cantidadATb.grid(row=2, column=1, padx=5, pady=5, sticky="w")

raiz.mainloop()
