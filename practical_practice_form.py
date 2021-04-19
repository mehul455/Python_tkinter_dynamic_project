from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
root=Tk()
root.geometry("500x500")
root.title("Registration Form")
#variables
id=IntVar()
firstname=StringVar()
lastname=StringVar()
contact=StringVar()
n = tk.StringVar()
radio=IntVar()
#database
def submit():
    if firstname.get()=="" or lastname.get() or contact.get() or n.get() or radio.get():
        messagebox.showinfo("Erorr","all fileds are require")
    else:

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pp_practical"
        )
        cur = con.cursor()

        cur.execute("insert into practical values(%s,%s,%s,%s,%s,%s)", (id.get(),
            firstname.get(),
                                                                       lastname.get(),
                                                                       contact.get(),
                                                                       n.get(),
                                                                       radio.get()
                                                                          ))
        con.commit()
        con.close()
        messagebox.showinfo("success", "record has been inserted")



lb1=Label(root,text="Mehuls Company",fg="black",bg="white")
lb1.grid(row=0,column=4,pady=10)

lable1=Label(root,text="First Name")
lable1.grid(row=1)
entry1=Entry(root,textvariable=firstname)
entry1.grid(row=1,column=2,pady=10)

lable2=Label(root,text="Last Name")
lable2.grid(row=2)
entry2=Entry(root,textvariable=lastname)
entry2.grid(row=2,column=2,pady=10)

lable3=Label(root,text="Contact")
lable3.grid(row=3)
entry3=Entry(root,textvariable=contact)
entry3.grid(row=3,column=2,pady=10)


lable4=Label(root,text="Language")
lable4.grid(row=4)
language=ttk.Combobox(root,textvariable=n)
language['values']=("python","java")
language.grid(row=4,column=2,pady=10)


btn=Button(root,text="click",fg="white",bg="black",command=submit)
btn.place(x=100,y=250)



r=Radiobutton(text="Male",variable="radio",value=1,)
r.grid(row=5)
r=Radiobutton(text="Female",variable="radio",value=2)
r.grid(row=6)


root.mainloop()