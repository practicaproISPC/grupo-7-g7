import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

pantalla=Tk()
pantalla.geometry("300x300")
pantalla.title("Bienvenido")
pantalla.iconbitmap("imagenes/tuvionline.ico")

image=PhotoImage(file="imagenes/tuvilogo.gif")
image=image.subsample(2,2)
label=Label(image=image)
label.pack()

Label(text="Acceso al Sistema", bg="navy", fg="white", width="300")

pantalla.mainloop()
