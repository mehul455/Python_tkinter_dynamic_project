from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  # install to image module pip install pillow
from tkinter import messagebox
import mysql.connector
import pymysql


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\mehull.jpeg")
        lb_bg=Label(self.root,image=self.bg)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=170,width=320,height=470)

        img1=Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\red.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=450,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Arial",20,"bold"),fg="white",bg="black")
        get_str.place(x=75,y=100)

        """labels for username"""
        username=lb1=Label(frame,text="Username",font=("Arial",15,"bold"),fg="white",bg="black")
        username.place(x=100,y=155)

        self.txtuser=ttk.Entry(frame,font=("Arial",15,"bold"))
        self.txtuser.place(x=100,y=180,width=200)

        password = lb2 = Label(frame, text="Password", font=("Arial", 15, "bold"), fg="white", bg="black")
        password.place(x=100, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("Arial", 15, "bold"))
        self.txtpass.place(x=100, y=250, width=200)

        """Icon images"""
        img2 = Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\user3.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2,bg="black", borderwidth=0)
        lblimg2.place(x=350, y=313, width=100, height=100)

        img3 = Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\pass1.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=350, y=386, width=100, height=100)

        """login button"""
        loginbtn=Button(frame,command=self.login,text="Login", font=("Arial", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=30)

        """register button"""
        loginbtn = Button(frame, text="Create New Account?",command=self.rigister_window, font=("Arial", 10, "bold"),borderwidth=0, fg="white", bg="black",
                          activeforeground="white", activebackground="black")
        loginbtn.place(x=22, y=350, width=160)


    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
     if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error"," All Field Are Required")
     elif self.txtuser.get()=="mehul" and self.txtpass.get()=="gohil":
            messagebox.showinfo("Success","Success full")
     else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="ppmehul")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                               ))
            row=my_cursor.fetchone()
            if row==None:
               messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=student(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")



        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()




       #bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\1.jpeg")

        bg_lb1=Label(self.root,image=self.bg)
        bg_lb1.place(x=0,y=0,relwidth=1,relheight=1)

      #left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\bookss(2).jpeg")
        bg_lb1 = Label(self.root, image=self.bg1)
        bg_lb1.place(x=15, y=100,width=430,height=550)

        #main frame

        frame=Frame(self.root,bg="white")
        frame.place(x=400,y=100,width=620,height=550)

        register_lb1=Label(frame,text="REGISTER HERE",font=("Arial",20,"bold"),fg="red",bg="white")
        register_lb1.place(x=20,y=20)

        #label and entrys


        #row 1
        fname=Label(frame,text="First Name",font=("Arial",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Arial",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)


        lname = Label(frame, text="Last Name", font=("Arial", 15, "bold"), bg="white")
        lname.place(x=340, y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Arial",15))
        self.txt_lname.place(x=340,y=130,width=250)


        #row2
        contact = Label(frame, text="Contact No", font=("Arial", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("Arial", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email=Label(frame,text="Email",font=("Arial",15,"bold"),bg="white",fg="black")
        email.place(x=340,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Arial",15))
        self.txt_email.place(x=340,y=200,width=250)
        #row 3

        security_q = Label(frame, text="Select Security Question", font=("Arial", 15, "bold"), bg="white")
        security_q.place(x=50, y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Arial", 15, "bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your friend name","Your pet name")

        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)






        security_a = Label(frame, text="Security Answer", font=("Arial", 15, "bold"), bg="white")
        security_a.place(x=340, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA,font=("Arial", 15))
        self.txt_security.place(x=340, y=270, width=250)



        #row 4
        # row4

        pswd = Label(frame, text="Password", font=("Arial", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pwd = ttk.Entry(frame,textvariable=self.var_pass, font=("Arial", 15))
        self.txt_pwd.place(x=50, y=340, width=250)

        confi_pswd = Label(frame, text="Confirm Password", font=("Arial", 15, "bold"), bg="white")
        confi_pswd.place(x=340, y=310)

        self.txt_confi_pwd = ttk.Entry(frame,textvariable=self.var_confpass, font=("Arial", 15))
        self.txt_confi_pwd.place(x=340, y=340, width=250)


        #check button
        self.var_check=IntVar()
        self.ch=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("Arial", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        self.ch.place(x=50,y=380)


        #botton
        img=Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\registrationbutton.jpg")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)


        img1 = Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\l.jpg")
        img1 = img1.resize((150, 70), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", bg="white")

        b1.place(x=290, y=420, width=300)



    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms and Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="ppmehul")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User All Ready Exist,Please try another emaiil")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_fname.get(),
                                                                self.var_lname.get(),
                                                                self.var_contact.get(),
                                                                self.var_email.get(),
                                                                self.var_securityQ.get(),
                                                                self.var_securityA.get(),
                                                                self.var_pass.get()
                                                                         ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")



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



if __name__== "__main__":

    main()