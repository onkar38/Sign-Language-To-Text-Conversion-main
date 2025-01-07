from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import subprocess


def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'onkar' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
        clear_window()
        new_page()
    else:
        messagebox.showerror('Error', 'Login Failed')


def start_comunication():
    import tkinter as tk
    import subprocess
    subprocess.call(['python','D:\pblSE\Sign-Language-To-Text-Conversion-main\Sign-Language-To-Text-Conversion-main\Application.py'])

def clear_window():
    # Destroy all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()
def new_page():
    root.configure(background='#0096DC')

    register_faces_btn = Button(root, text='start_comunication', width=20, height=5, command=start_comunication)
    register_faces_btn.pack(pady=(350, 20))

root = Tk()
root.title('Login Form')
root.geometry('550x900')
root.configure(background='#0096DC')

img = Image.open('wallpapers/img1.jpg')
resized_img = img.resize((210, 210))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 1))

text_label = Label(root, text='PBL', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 10))

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 22))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(10, 8))
password_label.config(font=('verdana', 22))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command=handle_login)
login_btn.pack(pady=(40, 50))
login_btn.config(font=('verdana', 10))

root.mainloop()