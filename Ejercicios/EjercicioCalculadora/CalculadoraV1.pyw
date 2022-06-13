# Carga módulo tk (widgets estándar)
import parser
from tkinter import *  
from tkinter import ttk
from tkinter import font

root = Tk()
root.title("CalculadoraV1")

######Entrada######
display = Entry(root, font=("Calibri 20"))
display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

######Funciones######
indice = 0

def get_numbers(numero):
    global indice
    display.insert(indice, numero)
    indice += 1
    
def get_operations(operador):
    global indice
    operator_length = len(operador) #longitud de operador
    display.insert(indice, operador)
    indice += operator_length
    
def clear_display():
    display.delete(0, END)
    
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")
        
def calcular():
    display_state = display.get()
    try:
        expresion_matematica = parser.expr(display_state).compile()
        resultado = eval(expresion_matematica)
        clear_display()
        display.insert(0, resultado)
    except expression as identifier:
        clear_display()
        display.insert(0, "Error")

######Botones######
Button(root, text="1", width=5, height=2, command=lambda:get_numbers(1)).grid(row=4, column=0, padx=5, pady=5)
Button(root, text="2", width=5, height=2, command=lambda:get_numbers(2)).grid(row=4, column=1, padx=5, pady=5)
Button(root, text="3", width=5, height=2, command=lambda:get_numbers(3)).grid(row=4, column=2, padx=5, pady=5)
Button(root, text="4", width=5, height=2, command=lambda:get_numbers(4)).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="5", width=5, height=2, command=lambda:get_numbers(5)).grid(row=3, column=1, padx=5, pady=5)
Button(root, text="6", width=5, height=2, command=lambda:get_numbers(6)).grid(row=3, column=2, padx=5, pady=5)
Button(root, text="7", width=5, height=2, command=lambda:get_numbers(7)).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="8", width=5, height=2, command=lambda:get_numbers(8)).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="9", width=5, height=2, command=lambda:get_numbers(9)).grid(row=2, column=2, padx=5, pady=5)
Button(root, text="0", width=14, height=2, command=lambda:get_numbers(0)).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

Button(root, text="(", width=5, height=2, command=lambda:get_operations("(")).grid(row=1, column=4, padx=5, pady=5)
Button(root, text=")", width=5, height=2, command=lambda:get_operations(")")).grid(row=2, column=4, padx=5, pady=5)
Button(root, text=".", width=5, height=2, command=lambda:get_operations(".")).grid(row=5, column=4, padx=5, pady=5)
Button(root, text="exp", width=5, height=2, command=lambda:get_operations("**")).grid(row=4, column=4, padx=5, pady=5)
Button(root, text="^2", width=5, height=2, command=lambda:get_operations("**2")).grid(row=3, column=4, padx=5, pady=5)

Button(root, text="+", width=5, height=2, command=lambda:get_operations("+")).grid(row=1, column=3, padx=5, pady=5)
Button(root, text="-", width=5, height=2, command=lambda:get_operations("-")).grid(row=2, column=3, padx=5, pady=5)
Button(root, text="x", width=5, height=2, command=lambda:get_operations("*")).grid(row=3, column=3, padx=5, pady=5)
Button(root, text="/", width=5, height=2, command=lambda:get_operations("/")).grid(row=4, column=3, padx=5, pady=5)
Button(root, text="%", width=5, height=2, command=lambda:get_operations("%")).grid(row=1, column=2, padx=5, pady=5)

Button(root, text="AC", width=5, height=2, command=lambda:clear_display()).grid(row=1, column=0, padx=5, pady=5)

Button(root, text="←", width=5, height=2, command=lambda:undo()).grid(row=1, column=1, padx=5, pady=5)

Button(root, text="=", width=14, height=2, command=lambda:calcular()).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()