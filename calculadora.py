from tkinter import *

root = Tk()
root.title("Calculadora")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0

def obt_num(n):
    global i
    display.insert(i, n)
    i+=1
    
def obt_op(operator):
    global i
    operador = len(operator)
    display.insert(i, operator)
    i+=operador

def limpiar_display():
    display.delete(0, END)
    
def undo():
    display_estado = display.get()
    if len(display_estado):
        display_nuevo_estado = display_estado[:-1]
        limpiar_display()
        display.insert(0, display_nuevo_estado)
        
    else:
        limpiar_display()
        display.insert(0, 'Error.')
        
def calcular():
    display_estado = display.get()
    try:
        expresion =  compile(display_estado, 'app.py', 'eval')
        result = eval(expresion)
        limpiar_display()
        display.insert(0,result)
    except:
        limpiar_display()
        display.insert(0,"error")
        
    
    
# Botones numericos

Button(root, text="1", command=lambda:obt_num(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:obt_num(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:obt_num(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:obt_num(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:obt_num(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:obt_num(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:obt_num(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:obt_num(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:obt_num(9)).grid(row=4, column=2, sticky=W+E)
Button(root, text="0", command=lambda:obt_num(0)).grid(row=5, column=1, sticky=W+E)
# Botones operadores

Button(root, text="AC", command=lambda: limpiar_display).grid(row=5, column=0, sticky=W+E)

Button(root, text="%", command=lambda: obt_op("%")).grid(row=5, column=2, sticky=W+E)
Button(root, text="+", command=lambda: obt_op("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda: obt_op("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: obt_op("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: obt_op("/")).grid(row=5, column=3, sticky=W+E)
Button(root, text="exp", command=lambda: obt_op("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda: obt_op("**2")).grid(row=3, column=5, sticky=W+E)

Button(root, text="(", command=lambda: obt_op("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda: obt_op(")")).grid(row=4, column=5, sticky=W+E)

Button(root, text="🡸", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="=", command= calcular()).grid(row=5, column=4, sticky=W+E, columnspan= 2)

root.mainloop()