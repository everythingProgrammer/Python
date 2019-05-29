import tkinter as tk
mainWindow = tk.Tk()
mainWindow.title("Sample Window")
First_Label = tk.Label(mainWindow, text= "Parameter1 ",pady = (10))
First_Label.pack()
para1 = tk.Entry(mainWindow)
para1.pack()

Second_Label = tk.Label(mainWindow, text= "Parameter2 ", pady = (10))
Second_Label.pack()

para2 = tk.Entry(mainWindow)
para2.pack()

in1 = 0;
in2 = 0;

def addition():
    try:
        in1 = int(para1.get())
        in2 = int(para2.get())
        if (in2 > 0):
            o1 = in1 + in2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")


def substract():
    try:
        in1 = int(para1.get())
        in2 = int(para2.get())
        if (in2 > 0):
            o1 = in1 - in2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")


def multiply():
    try:
        in1 = int(para1.get())
        in2 = int(para2.get())
        if (in2 > 0):
            o1 = in1 * in2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")

def divide():
    try:
        in1 = int(para1.get())
        in2 = int(para2.get())
        if (in2 > 0):
            o1 = in1 / in2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")




button = tk.Button(mainWindow, text = "+", command = lambda: addition(), pady= (20))
button.pack()

button = tk.Button(mainWindow, text = "-", command= lambda: substract(), pady= (20))
button.pack()

button = tk.Button(mainWindow, text = "*", command= lambda: multiply(), pady= (20))
button.pack()

button = tk.Button(mainWindow, text = "/", command= lambda: divide(), pady= (20))
button.pack()

Result = tk.Label(mainWindow, text= "Final Result", pady= (10))
Result.pack()
mainWindow.mainloop()
