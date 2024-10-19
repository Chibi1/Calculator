import tkinter as tk
from tkinter import *
import time
expression = ""

def press(num:str):
    global expression
    expression = expression + num
    equation.set(expression)
   
def equalpress():
    try:
        global expression, equation
        total= str(eval(expression))
        equation.set(total)
               
    except:
        equation.set(" error ")
        expression = ""

def clear_field():
    global expression, equation
    expression = ""
    equation.set("")
 
       
def create_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.configure(background="light green")
    root.geometry("265x330")
    global equation
    equation = StringVar()
    expression_field = Entry(root, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
   
    # create number buttons
    row = 1
    col = 0
    num_buttons = [
        "7", "8", "9", 
        "4", "5", "6",
        "1", "2", "3",
        "0",
    ]
    for button_text in num_buttons:
        button = tk.Button(root, text=button_text, command=lambda num=button_text: press(num), width=4, height=2)
        button.grid(row=row, column=col)
        col +=1
        if col > 2:
            col=0
            row +=1
    
    plus = tk.Button(root, text=' + ',command=lambda: press("+"), height=1, width=7)
    plus.grid(row=1, column=3)

    minus = tk.Button(root, text=' - ',command=lambda: press("-"), height=1, width=7)
    minus.grid(row=2, column=3)
    
    multiply = tk.Button(root, text=' * ',command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=3, column=3)
    
    divide = tk.Button(root, text=' / ',command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=0)
 
    equal = tk.Button(root, text=' = ',command=equalpress, height=1, width=7)
    equal.grid(row=5, column=1)

    clear_button = tk.Button(root, text=' Clear ',command=clear_field, height=1, width=7)
    clear_button.grid(row=5, column=2)

    Decimal= tk.Button(root, text='.',command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=5, column=3)


    timer_display = tk.Label(root, text="00:00", width=16, height=2, font=("Arial", 20))
    timer_display.grid(row=row+4, column=0, columnspan=4) 


    clock_formats = ["12-hour clock", "24-hour clock"]

    clock_format_var = StringVar()
    clock_format_var.set(clock_formats[0])
    clock_format_dropdown = OptionMenu(root, clock_format_var, *clock_formats)
    clock_format_dropdown.grid(row=row+5, column=0, columnspan=4)


    def update_clock():
        
        if clock_format_var.get() == "12-hour clock":
            current_time = time.strftime("%I:%M:%S %p")
        else:
            current_time = time.strftime("%H:%M:%S")
        timer_display.config(text=current_time)
        root.after(1000, update_clock)

    update_clock()

    
    clock_format_var.set(clock_formats[0])
    clock_format_dropdown = OptionMenu(root, clock_format_var, *clock_formats)
    clock_format_dropdown.grid(row=row+6, column=0, columnspan=4)

    def change_clock_format(*args):

        if clock_format_var.get() == "12-hour clock":
            current_time = time.strftime("%I:%M:%S %p")
        else:
            current_time = time.strftime("%H:%M:%S")

        timer_display.config(text=current_time)

        clock_format_var.trace("w", change_clock_format)

    

    def change_color(color):
       root.configure(background=color)

    color_button = tk.Button(root, text="Yellow", command=lambda:change_color("light yellow"))
    color_button.grid(row=row+7, column=1, columnspan=2)

    color_button = tk.Button(root, text="Pink", command=lambda:change_color("light pink"))
    color_button.grid(row=row+7, column=2, columnspan=2)

    color_button = tk.Button(root, text="Blue", command=lambda:change_color("light blue"))
    color_button.grid(row=row+7, column=0, columnspan=2)


    root.mainloop()
    

create_gui()
    
