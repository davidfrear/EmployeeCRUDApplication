from tkinter import *
from tkinter import messagebox
import mysql.connecter

def insertData():
    # read the data provided by user
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if (id == "" or name == "" or dept == ""):
        messagebox.showwarning("Cannort Insert", "All the fields are required!")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", passwd="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("insert into empDetails values('''+id+''','''+name+''','''+dept+'''')")
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        messagebox.showinfo("Insert Status", "Data Inserted Successfully")
        myDB.close()

def updateData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if (id == "" or name == "" or dept ""):
        messagebox.showwarning("Cannot Update", "All the fields are required!")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", passwd="YOUR_PASSWORD", database="employee")
        myCur = myBD.cursor()
        myCur.execute("Update empDetails set empName='''+name+''',empDept='''+dept+'''where empId='''+id+'''")
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        messagebox.showinfo("Update Status", "Data Updated Successfully")
        myDB.close()

def getData():
    if (enterId.get() == ""):
        messagebox.showwarning("Fetch Status", "Please provide the emp ID to fetch the data")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", passwd="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("Select * from emptDetails where empID='''+enterId.get()+'''")
        rows = myCur.fetchall()

        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])

        myDB.close()

def deleteData():
    if (enterId.get() == ""):
        messagebox.showwarning("Cannot Delete", "Please provide the Emp ID to delete the data")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", passwd="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("delete from empDetails where empID='''+enterId.get()'''")
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        messagebox.showinfo("Delete Status", "Data Deleted Successfully")

        myDB.close()

def show():
    myDB = mysql.connector.connect(host="localhost", user="root", passwd="YOUR_PASSWORD", database="employee")
    myCur = myDB.cursor()
    myCur.execute("select * from empDetails")
    rows = myCur.fetchall()
    showData.delete(0, showData.size())

    for row in rows:
        addData = str(row[0]) + '' + row[1] + '' + row[2]
        showData.insert(showData.size() + 1, addData)

    myDB.close()

def resetField():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")

window=Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

#creating all the labels
empId=Label(window,text="Employee ID",font=("Serif",12))
empId.place(x=20,y=30)
empName=Label(window,text="Employee Name",font=("Serif",12))
empName.place(x=20,y=60)
empDept=Label(window,text="Employee Dept",font=("Serif",12))
empDept.place(x=20,y=90)

#creating Entry boxes respective to the labels
enterId=Entry(window)
enterId.place(x=170,y=30)
enterName=Entry(window)
enterName.place(x=170,y=60)
enterDept=Entry(window)
enterDept.place(x=170,y=90)

#creating all the buttons
insertBtn=Button(window,text="Insert",font=("Sans",12),bg="white",command=insertData)
insertBtn.place(x=20,y=160)
updateBtn=Button(window,text="Update",font=("Sans",12),bg="white",command=updateData)
updateBtn.place(x=80,y=160)
getBtn=Button(window,text="Fetch",font=("Sans",12),bg="white",command=getData)
getBtn.place(x=150,y=160)
deleteBtn=Button(window,text="Delete",font=("Sans",12),bg="white",command=deleteData)
deleteBtn.place(x=210,y=160)
resetBtn=Button(window,text="Reset",font=("Sans",12),bg="white",command=resetFields)
resetBtn.place(x=20,y=210)

#time to add a listbox
showData=Listbox(window)
showData.place(x=330,y=30)

window.mainloop()