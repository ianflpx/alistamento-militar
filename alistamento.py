import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import datetime

def consultar():
    date = calend.get_date()
    today = datetime.date.today()
    idade = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    if date.year <= 2005 and not var.get():
        messagebox.showinfo("Resultado", f"Voce ESTA apto para servir, pois voce tem {idade} anos!")
    else:
        messagebox.showinfo("Resultado",f"Voce NAO esta apto para servir, pois voce tem {idade} anos!")

app = Tk()
app.title("Alistamento militar")
app.geometry("300x300")
app.minsize(300, 300)
app.maxsize(300, 300)

titulo_alistamento = Label(app, font="Arial 15", text="ALISTAMENTO")
titulo_alistamento.place(x=80, y=25)

nome = Label(app, text="Nome completo")
nome.place(x=30, y=85)
box_nome = Entry(app, width=20)
box_nome.place(x=140, y=85)

ano = Label(app, text="Data de nascimento")
ano.place(x=20, y=115)
calend = DateEntry(app, width=17, background='darkblue',foreground='white', borderwidth=2)
calend.place(x=140, y=115)

var = tk.BooleanVar()
checkbox = tk.Checkbutton(app, text="Portador de deficiência física", variable=var)
checkbox.place(x=75, y=145)

button = ttk.Button(app, width=25, text="Consultar", command=consultar)
button.place(x=75, y=190)

app.mainloop()