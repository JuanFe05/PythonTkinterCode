from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#Variables:
# sueldoDesc = descuento
# tipo, tipoEmp = tipo de empleado
# sueldo, sueldoEmp = sueldo del empleado
# bonific, bonificacion = bonificación
# n = numero de empleados

######Función Salir del aplicativo######


def salir():
    raiz.destroy()

######Función Calcular descuento######


def calcularDescuento(sueldoDesc):
    totalDesc = sueldoDesc * 0.08
    return totalDesc

######Función Calcular Bonificación######


def calcularBonificacion(tipo, sueldo):
    if tipo == 1:
        bonific = sueldo * 0.06
    else:
        bonific = sueldo * 0.09
    return bonific

######Función para Calcular salario Neto######


def calcularSalario(tipoEmp, sueldoEmp):
    bonificacion = calcularBonificacion(tipoEmp, sueldoEmp)
    descuento = calcularDescuento(sueldoEmp)

    salarioNeto = sueldoEmp + bonificacion - descuento
    return salarioNeto

######Porceso principal######


def principal():
    n = int(numeroETb.get())
    totalNomina = 0
    reporte = "Nombre - TipoEmpleado - SalarioNeto\n"

    for numEmpleados in range(n):
        nombre = simpledialog.askstring(
            "Nombre Empleado", "Escriba el nombre del empleado :")
        tipo = simpledialog.askinteger(
            "Tipo Empleado", "Digite el tipo de empleado (1-2) :")
        sueldo = simpledialog.askfloat(
            "Sueldo Empleado", "Ingrese el sueldo del empleado :")

        salarioNeto = calcularSalario(tipo, sueldo)

        totalNomina = totalNomina + salarioNeto
        reporte = reporte + nombre + "\t" + \
            str(tipo) + "\t" + str(salarioNeto) + "\n"

    reporte = reporte + "\n\nEl total de la nomina es: " + str(totalNomina)
    reporteT.config(state="normal")
    reporteT.insert(INSERT, reporte)
    reporteT.config(state="disable")


######Interfaz Gráfica de usuario######
raiz = Tk()
raiz.resizable(0, 0)
raiz.title("Ejercicio Nomina")

######contenedor Botones######
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10)

numeroELabel = Label(marco1, text="Número de empleados:").grid(
    row=0, column=0, sticky="w", padx=10, pady=5)
numeroETb = Entry(marco1, width=10)
numeroETb.grid(row=0, column=1, padx=10, pady=5)

generarReporteB = Button(marco1, text="Generar Reporte", command=principal)
generarReporteB.grid(row=1, column=0, padx=3, pady=3)

salirB = Button(marco1, text="Salir", width=12, command=salir)
salirB.grid(row=1, column=1, padx=3, pady=3)

######contenedor Resultado######
marco2 = LabelFrame(raiz, text="Reporte empleados")
marco2.config(bd=3, relief="sunken", padx=15, pady=15)
marco2.pack()

reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0)

raiz.mainloop()
