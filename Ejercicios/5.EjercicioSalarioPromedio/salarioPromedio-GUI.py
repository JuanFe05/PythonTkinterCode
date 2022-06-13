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
    reporteMayorT.config(state="normal")
    reporteMayorT.delete("1.0","end")
    reporteMayorT.config(state="disable")
    varSalarioP.set("")
    
####################################################


def principal():
    cantidadTrabajadores = simpledialog.askinteger(
        "Número estudiantes", "Ingrese la cantidad de trabajadores:")

    while cantidadTrabajadores <= 0:
        messagebox.showerror(title="Error", message="Erro, la cantidad debe ser positiva.")
        cantidadTrabajadores = simpledialog.askinteger(
            "Número estudiantes", "Ingrese la cantidad de trabajadores:")

    nombres = [None] * cantidadTrabajadores
    apellidos = [None] * cantidadTrabajadores
    salarios = [0.0] * cantidadTrabajadores

    for i in range(cantidadTrabajadores):
        nombres[i] = simpledialog.askstring("Nombre", "Escriba el nombre:")
        apellidos[i] = simpledialog.askstring("Apellido", "Escriba el apellido:")
        salario = simpledialog.askfloat("Notas", "Escribas el salario:")

        while salario < 0:
            messagebox.showerror(title="Error", message="Ingresar un salario mayor a 0")
            salario = simpledialog.askfloat("Notas", "Escribas la nota:")

        salarios[i] = salario

    prom = calcularSalarioPromedio(salarios)

    reporteT.config(state="normal")
    reporteT.insert(INSERT, prom)
    reporteT.config(state="disable")
    
    

#Interfaz Gráfica de usuario
raiz = Tk()
#raiz.resizable(0,0)
raiz.title("Salario Nominal")

#contenedor Botones
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10, padx = 10)

numeroCLabel = Label(marco1, text="Número de trabajadores:").grid(row = 0, column = 0, sticky = "w", padx = 10, pady=5)
varNumeroC = StringVar()
numeroCTb = Entry(marco1, width=10, state="disable", textvariable = varNumeroC)
numeroCTb.grid(row=0, column = 1, padx = 10, pady=5)

iniciarB = Button(marco1, text="Iniciar",width=12)
iniciarB.grid(row=1,column=0,padx=3, pady=3)
salirB = Button(marco1, text="Salir",width=12, command=salir)
salirB.grid(row=1,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Borrar",width=12, command=borrar)
borrarB.grid(row=1,column=2,padx=3, pady=3)


#contenedor Reporte trabajadores
marco2 = LabelFrame(raiz, text="Reporte de trabajadores")
marco2.config(bd=3, relief="sunken", padx=15,pady=15)
marco2.pack(pady= 10, padx = 10)

reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0, columnspan=2)

#contenedor Reporte mayore promedio
marco3 = LabelFrame(raiz, text="Reporte de trabajadores que ganan más que el promedio")
marco3.config(bd=3, relief="sunken", padx=15,pady=15)
marco3.pack(pady= 10, padx = 10)

salarioPLabel = Label(marco3, text="Salario promedio:").grid(row = 0, column = 0, sticky = "e", padx = 10, pady=5)
varSalarioP = StringVar()
salarioPTb = Entry(marco3, width=10, state="disable", textvariable = varSalarioP)
salarioPTb.grid(row=0, column = 1, padx = 10, pady=5,sticky = "w")

reporteMayorT = Text(marco3)
reporteMayorT.config(state="disable", width=50, height=10)
reporteMayorT.grid(row=1, column=0, columnspan=2)

raiz.mainloop()
