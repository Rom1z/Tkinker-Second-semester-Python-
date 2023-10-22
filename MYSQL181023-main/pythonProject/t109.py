import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['col1'])
    e3.insert(0, select['col2'])
    e4.insert(0, select['col3'])

def Add():
    studid = e1.get()
    col1 = e2.get()
    col2 = e3.get()
    col3 = e4.get()

    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db31"
    )
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO new_table (id, col1, col2, col3) VALUES (%s, %s, %s, %s)"
        val = (studid, col1, col2, col3)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Data inserted successufully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def Delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db31"
    )
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from new_table where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Data delete successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def Show():
    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db31"
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id, col1, col2, col3 FROM new_table")
    records = mycursor.fetchall()
    print(records)

    for i, (id, col1, col2, col3) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, col1, col2, col3))
        mysqldb.close()

def refreshtable():
    listBox.delete(*listBox.get_children())
    Show()


root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Test BD", fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="ID").place(x=10, y=10)
Label(root, text="Col1").place(x=10, y=40)
Label(root, text="Col2").place(x=10, y=70)
Label(root, text="Col3").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="Refresh", command=refreshtable, height=3, width=13).place(x=460, y=130)
Button(root, text="Delete", command=Delete, height=3, width=13).place(x=250, y=130)

cols = ('id', 'col1', 'col2', 'col3')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

Show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()