from tkinter import *
from tkinter import ttk   # ttk is used for tkinter combobox. (Exp:gender   *male (or) *female)
from tkinter import  messagebox
from db import  Database

# databse connection:
db=Database("Employee.db")

dinesh=Tk()    #  dinesh : tkinter obj
dinesh.title("Employee Management system")

#window size
dinesh.geometry("1366x768+0+0")

#background color
dinesh.config(bg="#2c3e50")

dinesh.state("zoomed") # full screen

#variable names:
name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

# 1.Entry frame:

#head line:
entries_frame=Frame(dinesh,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management system", font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky="w")  #padx:padding x axis ; pady:padding y axis

#label creation: (name label)
lblname=Label(entries_frame,text="Name",font=("calibri",16),bg="#535c68",fg="white")
lblname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
#textbox for name label
txtname=Entry(entries_frame,textvariable=name,font=("calibri",16),width=30)  #textvariable : name - variable name
txtname.grid(row=1,column=1,padx=10,pady=10,sticky="w")  # sticky="w" : elements are placed in left side. 'w'- west side


#label creation: (age label)
lblage=Label(entries_frame,text="Age",font=("calibri",16),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
#textbox for age label
txtage=Entry(entries_frame,textvariable=age,font=("calibri",16),width=30)    #textvariable : age - variable age
txtage.grid(row=1,column=3,padx=10,pady=10,sticky="w")


#label creation: (Date of Join-doj label)
lbldoj=Label(entries_frame,text="Date of Join",font=("calibri",16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
#textbox for Doj label
txtdoj=Entry(entries_frame,textvariable=doj,font=("calibri",16),width=30)     ##textvariable : Doj - variable doj
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

#label creation: (email label)
lblEmail=Label(entries_frame,text="Email",font=("calibri",16),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
#textbox for email label
txtEmail=Entry(entries_frame,textvariable=email,font=("calibri",16),width=30)    ##textvariable : email - variable email
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

#label creation: (Gender label)
lblgender=Label(entries_frame,text="Gender",font=("calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
#combobox choices:
combogender=ttk.Combobox(entries_frame,font=("calibri",16),width=28,textvariable="gender",state="readonly") # "readonly" is used for select only in the items.it doesn't take anything.
combogender['values']=("Male","Female","Others")                        # textvariable : gender
combogender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

#label creation: (contact)
lblcontact=Label(entries_frame,text="Contact No",font=("calibri",16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
#textbox for contact label
txtcontact=Entry(entries_frame,textvariable=contact,font=("calibri",16),width=30)    ##textvariable : contact - variable email
txtcontact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

#label creation: (Address)
lbladdress=Label(entries_frame,text="Address",font=("calibri",16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
#text box:
txtaddress=Text(entries_frame,width=85,height=5,font=("calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")   #columnspan : used to merge all element.

# select for db rows in 2.table frame
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row) #tv-treeview
    global row
    row=data["values"]
    #print(row)

    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END, row[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

# button functions:
def add_Employee():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtEmail.get()=="" or combogender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please fill all the details..!")
        return  # it is used for don't go next line
    db.insert(txtname.get(), txtage.get(),txtdoj.get(),txtEmail.get(),combogender.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted..!")
    clear_Employee()
    displayall()

def update_Employee():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtEmail.get()=="" or combogender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please fill all the details..!")
        return  # it is used for don't go next line
    db.update(row[0],txtname.get(), txtage.get(),txtdoj.get(),txtEmail.get(),combogender.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Updated..!")
    clear_Employee()
    displayall()

def delete_Employee():
    db.remove(row[0])
    clear_Employee()
    displayall()

def clear_Employee():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END) # 1.0 is starting line , END is endvlaue - it clear end values.

# button - add emp
btn_frame=Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=18,sticky="w")                                                     #bd=border

# button - add emp
btnadd=Button(btn_frame,command=add_Employee,text="Add details",width=15,font=("calibri",16,"bold"),bg="#16a085",fg="white",bd=0).grid(row=0,column=0)

# button - update emp
btnupdate=Button(btn_frame,command=update_Employee,text="update details",width=15,font=("calibri",16,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=1,padx=10)

# button - Delete emp
btnDelete=Button(btn_frame,command=delete_Employee,text="delete details",width=15,font=("calibri",16,"bold"),bg="#c0392b",fg="white",bd=0).grid(row=0,column=2,padx=10)

# button - Clear emp
btnclear=Button(btn_frame,command=clear_Employee,text="clear details",width=15,font=("calibri",16,"bold"),bg="#f39c12",fg="white",bd=0).grid(row=0,column=3,padx=10)



# 2.Table frame:
tree_frame=Frame(dinesh,bg="#ecf0f1")
tree_frame.place(x=0,y=480,width=1600,height=520)

style=ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",18),
                rowheight=50) # Modify the font of the body
style.configure("mystyle.Treeview.Heading",font=("calibri",15)) # modify the font of the headings

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview") # tv-treeview obj , 8 column  , Treeview is inbuild function

#headings: for table frame
tv.heading("1", text="ID")
tv.column("1",width=3)

tv.heading("2", text="Name")
tv.column("2",width=10)

tv.heading("3", text="Age")
tv.column("3",width=5)

tv.heading("4", text="D.O.B")
tv.column("4",width=10)

tv.heading("5", text="Email")

tv.heading("6", text="Gender")
tv.column("6",width=10)

tv.heading("7", text="Contact")
tv.column("7",width=6)

tv.heading("8", text="Address")

tv['show']= 'headings'
tv.bind("<ButtonRelease-1>", getData) # click event for db items
tv.pack(fill=X)

displayall()
dinesh.mainloop()