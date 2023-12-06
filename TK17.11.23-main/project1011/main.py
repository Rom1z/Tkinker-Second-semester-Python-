import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from tkinter import END

def GetValue(event):
    #e1.delete(0, END)
    #e2.delete(0, END)
    #e3.delete(0, END)
    #e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    #e1.insert(0, select['id'])
    #e2.insert(0, select['empname'])
    #e3.insert(0, select['mobile'])
    #e4.insert(0, select['salary'])


def add():
    window = Tk()
    window.geometry("300x200")

    lbl1 = Label(window, text="ФИО").place(x=100, y=20)
    lbl2 = Label(window, text="Номер").place(x=100, y=80)

    def close():
        window.destroy()

    def Add():
        # studid = e1.get()
        studname = e2.get()
        coursename = e3.get()
        # feee = e4.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor = mysqldb.cursor()

        try:
            sql = "INSERT INTO  data (name,phone) VALUES (%s, %s)"
            val = (studname, coursename)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            # messagebox.showinfo("information", "Employee inserted successfully...")
            # e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            # e4.delete(0, END)
            # e1.focus_set()
            # show()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

        refresh()
        window.destroy()


    btn1 = Button(window, text="Добавить", command=Add).place(x=100, y=130)
    btn2 = Button(window, text="Отмена", command=close).place(x=180, y=130)

    e2 = Entry(window)
    e2.place(x=170, y=20, width=100)

    e3 = Entry(window)
    e3.place(x=170, y=80, width=100)

    window.mainloop()

def updateCheck():
    print()

def update():
    window1 = Tk()
    window1.geometry("300x200")

    lbl1 = Label(window1, text="ФИО").place(x=100, y=40)
    lbl2 = Label(window1, text="Номер").place(x=100, y=80)
    #lbl3 = Label(window1, text="id").place(x=100, y=0)

    e1 = Entry(window1)
    e1.place(x=170, y=40, width=100)

    e2 = Entry(window1)
    e2.place(x=170, y=80, width=100)


    def update():
        studid = listBox.set(listBox.selection(), '#1')
        studname = e1.get()
        coursename = e2.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor = mysqldb.cursor()

        try:
            sql = "Update data set name= %s, phone= %s where id= %s"
            val = (studname, coursename, studid)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            e1.delete(0, END)
            e2.delete(0, END)
            #e3.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

        refresh()
        window1.destroy()

    def close():
        refresh()
        window1.destroy()

    btn1 = Button(window1, text="Изменить", command=update).place(x=100, y=130)
    btn2 = Button(window1, text="Отмена", command=close).place(x=180, y=130)

    window1.mainloop()

def deltabl():
    for i in listBox.get_children():
        listBox.delete(i)

def refresh():
    deltabl()
    show()


def delete():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="python")
    mycursor = mysqldb.cursor()

    try:
        sql = f'delete from data where id = {listBox.set(listBox.selection(), '#1')}'
        #val = (studid)
        mycursor.execute(sql)
        mysqldb.commit()
        lastid = mycursor.lastrowid

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

    refresh()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="python")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,name,phone FROM data")
    records = mycursor.fetchall()
    print(records)

    for i, (id, stname, course) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course))
        mysqldb.close()


root = Tk()
root.geometry("850x500")

Button(root, text="Добавить", command=add, height=3, width=13).place(x=30, y=250)
Button(root, text="Изменить", command=update, height=3, width=13).place(x=140, y=250)
Button(root, text="Уд0лить", command=delete, height=3, width=13).place(x=250, y=250)


cols = ('id', 'name', 'phone')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=10)

root.configure(bg="GRAY")
show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()