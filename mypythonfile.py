import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def login():
    myusername = e1.get()
    mypassword = e2.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="collegemanagement")
    mycursor=mysqldb.cursor()
    sql = "Select * from users  where username= %s and password= %s "
    val = (myusername,mypassword)
    mycursor.executemany(sql, (val,))
    row_count = mycursor.rowcount
    if row_count == 0:
        messagebox.showinfo("information", "Fail...")  
    else:
        messagebox.showinfo("information", "Success...") 
        root.destroy()

    mycursor.close()   



    mysqldb.rollback()
    mysqldb.close()



root = Tk()
root.geometry("800x500")
global e1
global e2

tk.Label(root, text="User Name").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
e1 = Entry(root)
e1.place(x=140, y=10)
e2 = Entry(root)
e2.place(x=140, y=40)
Button(root, text="Login",command = login,height=3, width= 13).place(x=30, y=130)
root.mainloop()

