from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="aquamarine",fg="black")
        title.pack(side=TOP,fill=X)

        #=======all variable
        self.Roll_No_var=StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        #manage frame
        manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cyan2")
        manage_Frame.place(x=20,y=100,width=400,height=580)

        m_title=Label(manage_Frame,text="Manage student",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lb1_roll=Label(manage_Frame,text="Roll No",bg="crimson",fg="white",font=("times new roman",17,"bold"))
        lb1_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lb1_name= Label(manage_Frame,text="Name", bg="crimson", fg="white", font=("times new roman", 17, "bold"))
        lb1_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name= Entry(manage_Frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1,pady=10,padx=20,sticky="w")

        lb1_email = Label(manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 17, "bold"))
        lb1_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email= Entry(manage_Frame,textvariable=self.email_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lb1_contact = Label(manage_Frame,text="contact",bg="crimson",fg="white",font=("times new roman",17,"bold"))
        lb1_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lb1_dob = Label(manage_Frame,text="D.O.B", bg="crimson", fg="white", font=("times new roman", 17, "bold"))
        lb1_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(manage_Frame,textvariable=self.dob_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lb1_address= Label(manage_Frame,text="Address", bg="crimson", fg="white", font=("times new roman", 17, "bold"))
        lb1_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(manage_Frame, width=30, height=4,font=("Arial",10,"bold"))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        lb1_gender = Label(manage_Frame,text="Gender", bg="crimson", fg="white", font=("times new roman", 17, "bold"))
        lb1_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(manage_Frame,textvariable=self.gender_var,font=("times new roman",10,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        #buttob framme
        button_Frame = Frame(manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        button_Frame.place(x=15, y=500, width=373)

        add_buttonbtn = Button(button_Frame,text="Add",font=("Arial",10,"bold"),width=5,command=self.add_students).grid(row=0,column=0,pady=10,padx=20)
        add_updatebtn = Button(button_Frame,text="Update",font=("Arial",10,"bold"),width=5,command=self.update_data).grid(row=0, column=1, pady=10, padx=20)
        add_deletebtn = Button(button_Frame, text="Delete",font=("Arial",10,"bold"),width=5,command=self.delete_data).grid(row=0, column=2, pady=10, padx=20)
        add_clearbtn = Button(button_Frame, command=self.clear,text="Clear",font=("Arial",10,"bold"),width=5).grid(row=0, column=3, pady=10, padx=20)


       #detail frame
        detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="cyan2")
        detail_Frame.place(x=450, y=100,width=550,height=580)

        lb1_search = Label(detail_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 17, "bold"))
        lb1_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")


        combo_search=ttk.Combobox(detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",10,"bold"),state="readonly")
        combo_search['values']=("Roll_no","name","contact")
        combo_search.grid(row=0, column=1, pady=10, padx=10, sticky="w")


        txt_search = Entry(detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        search_btn = Button(detail_Frame, text="Search",font=("Arial",10,"bold"),width=7,pady=4,command=self.search_data).grid(row=0, column=3, pady=10, padx=10)
        show_btn = Button(detail_Frame, text="Show All", font=("Arial",10,"bold"),width=7,pady=4,command=self.fetch_data).grid(row=0, column=4, pady=10, padx=10)

        #Table frame
        table_frame=Frame(detail_Frame,bd=4,relief=RIDGE,bg="cyan2")
        table_frame.place(x=10,y=70, width=530,height=500)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame, orient=VERTICAL)

        self.Student_table=ttk.Treeview(table_frame,columns=("roll_no","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll_no",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll_no",width=65)
        self.Student_table.column("name", width=65)
        self.Student_table.column("email", width=65)
        self.Student_table.column("gender", width=65)
        self.Student_table.column("contact", width=65)
        self.Student_table.column("dob", width=65)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_address.get('1.0',END)
                                                                         ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success","record has been inserted")
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for rows in rows:
                         self.Student_table.insert('',END,values=rows)
                con.commit()
        con.close()


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_address.get('1.0',END),
                                                                          self.Roll_No_var.get()

                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for rows in rows:
                         self.Student_table.insert('',END,values=rows)
                con.commit()
        con.close()

root = Tk()
ob = student(root)
root.mainloop()
