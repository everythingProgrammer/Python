import sqlite3
import tkinter as tk
mainWindow = tk.Tk()
mainWindow.title("Student Entry ")
Name_Label = tk.Label(text="Enter Name", pady =(10))
Name_Field = tk.Entry( )
Name_Label.pack( )
Name_Field.pack()
College_Label = tk.Label(text="College Name" , pady =(10))
College_Field = tk.Entry()
College_Label.pack()
College_Field.pack()
Phone_Label = tk.Label(text="Enter Phone Number", pady =(10)).pack()
Phone_Field = tk.Entry()
Phone_Field.pack()

connection = sqlite3.connect('student.db')
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
def enterData():
    try:
        Name = Name_Field.get()
        College = College_Field.get()
        Phone = Phone_Field.get()
        # if(!isDigit(Phone)):
        #     Result.config(text= "Phone must be digit ")
        if len(Name) <= 0 or len(College) <= 0  :
            Result.config(text = "Fields cannot be blank")
        else:
            connection.execute("INSERT INTO " + "student_table"+ " ( " +
                               STUDENT_NAME + ", " +
                               STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
                               ", " + STUDENT_PHONE +
                               " ) VALUES ( '" + Name + "', '" + College + "', " +
                               "'" + "Dehradun. Uttrakhand" + "', "+ Phone + " ); ")
            connection.commit()
    except ValueError:
        print("An Exception Occured query not executed ")
        Result.config(text="Invalid Entry ")
def doQuit():
    exit(0)

b1 = tk.Button(mainWindow, text = "Enter Value", command=lambda: enterData())
b1.pack()
b2 = tk.Button(mainWindow, text = "Quit", command = lambda: doQuit())
b2.pack()
Result = tk.Label(mainWindow, text= "", pady= (10))
Result.pack()
mainWindow.mainloop()
