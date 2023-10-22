import tkinter as tk
from tkinter import ttk, messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo('Регистрация прошла успешно')

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'add' and password == '0451':
        messagebox.showinfo('Авторизация прошла успешно')

        with open('t109.py') as file:
            open(t109.py)

    else:
        messagebox.showerror('Неправильный логин или пароль')

window = tk.Tk()
window.title('Авторизация')
window.geometry('300x150')

username_label = tk.Label(window, text='Логин:')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text='Пароль:')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

login_button = tk.Button(window, text='Войти', command=login)
login_button.pack()

register_button = tk.Button(window, text='Зарегистрироваться', command=register)
register_button.pack()

window.mainloop()