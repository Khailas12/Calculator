import tkinter

root = tkinter.Tk()
root.title("Calculator")

label_result = tkinter.Label(root, text="") 
label_result.grid(row=0,columnspan=10)

expression = ""

def add(value):
    global expression
    expression += value
    label_result.config(text=expression)

def clear():
    global expression
    expression = ""
    label_result.config(text=expression)

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = expression
            expression = ""
    label_result.config(text=result)
    expression = str(result)

def back():
    global expression
    expression = expression[0:len(expression)-1]
    label_result.config(text=expression)


def key_handler(event):
    global expression
    print(event.keysym)

    if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        add(event.keysym)

    elif event.keysym == "plus":
        add("+")

    elif event.keysym == "minus":
        add("-")

    elif event.keysym == "asterisk":
        add("*")

    elif event.keysym == "slash":
        add("/")
        
    elif event.keysym.lower() == "c":
        clear()
    
    elif event.keysym == "period":
        add("-")
    elif event.keysym in ("Return" "equal"):
        calculate()

    elif event.keysym == "BackSpace":
        expression = expression[0:len(expression)-1]
        label_result.config(text=expression)


root.bind("<Key>", key_handler)


button_back = tkinter.Button(root, text="Back", height=2, width=3, command=lambda: back())
button_back.grid(row=0, column=3, columnspan=4)

#first row
button_1 = tkinter.Button(root, text="7", width=3, height=2, command=lambda: add("7"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="8", width=3, height=2, command=lambda: add("8"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="9", width=3, height=2, command=lambda: add("9"))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/", width=3, height=2, command=lambda: add("/"))
button_divide.grid(row=1, column=3)


#second row
button_4 = tkinter.Button(root, text="4", width=3, height=2, command= lambda :add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", width=3, height=2, command= lambda :add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", width=3, height=2, command= lambda :add("6"))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="*", width=3, height=2, command="*")
button_multiply.grid(row=2, column=3)


#Third Row
button_7 = tkinter.Button(root, text="1", width=3, height=2, command= lambda :add("1"))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="2", width=3, height=2, command= lambda :add("2"))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="3",width=3, height=2, command= lambda :add("3"))
button_9.grid(row=3, column=2)

button_subtract = tkinter.Button(root, text="-", width=3, height=2, command= lambda :add("-"))
button_subtract.grid(row=3, column=3)


#row 4
button_clear = tkinter.Button(root, text="C", width=3, height=2, command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(root, text="0", width=3, height=2, command= lambda :add("0"))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", width=3, height=2, command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", width=3, height=4, command=lambda: add("+"))
button_add.grid(row=4, column=3, rowspan=3)


#row 5
button_equals = tkinter.Button(root, text="=", width=12, command=lambda: calculate())
button_equals.grid(row=5, rowspan=2,column=0, columnspan=3)

root.mainloop()
print("done")    # personal pereference
