from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter import messagebox
import random

root=Tk()
root.geometry("750x500")
root.title("Игра - Выбери правильную карточку")

def game(): #Играть
    btn_start.pack_forget()
    btn_bg.pack_forget()
    btn_rules.pack_forget()
    btn_exit.pack_forget()


def rules(): #Вход в список правил
    global label
    global textA
    btn_start.pack_forget()
    btn_bg.pack_forget()
    btn_exit.pack_forget()

    btn_rules.configure(text="Назад",height=3, width=20,font="Arial 15",bg='#E0E0E0',command=nazad1)
    btn_rules.place(x=250,y=350)

    textA=Text(root,height=8, width=50)
    textA.configure(font=("Arial", 18 ))
    label = Label(root, text = "Правила")
    label.configure(bg='#E0E0E0',font =("Arial", 35))
    Rule = """Есть 3 карты. 2 из этих карт красные. Если вытянешь одну из этих карт - ты проиграл.
    Но из трех карт есть одна выигрышная зеленая карточка. Вытяни эту карточку чтобы победить."""

    label.pack()
    textA.pack()
    textA.insert(END, Rule)

def nazad1(): #Выход в меню из списка правил
    global label
    global textA
    label.pack_forget()
    textA.pack_forget()

    btn_start.configure(text="Играть",height=3, width=20,font="Arial 15")
    btn_start.place(x=250, y=50)

    btn_bg.configure(text="Выбери фон",height=3, width=20,font="Arial 15")
    btn_bg.place(x=250,y=150)

    btn_rules.configure(text="Правила",height=3, width=20,font="Arial 15",command=rules)
    btn_rules.place(x=250,y=250)

    btn_exit.configure(text="Выход",height=3, width=20,font="Arial 15")
    btn_exit.place(x=250,y=350)

   

def exit(): #Выход
    root.destroy()

btn_start=Button(root,text="Играть",height=3, width=20,font="Arial 15",bg='#E0E0E0',command=game)
btn_start.place(x=250, y=50)

btn_bg=Button(root,text="Выбери фон",height=3,width=20,font="Arial 15",bg='#E0E0E0')
btn_bg.place(x=250,y=150)

btn_rules=Button(root,text="Правила",height=3, width=20,font="Arial 15",bg='#E0E0E0',command=rules)
btn_rules.place(x=250,y=250)

btn_exit=Button(root,text="Выход",height=3, width=20,font="Arial 15",bg='#E0E0E0',command=exit)
btn_exit.place(x=250,y=350)

btn_rules.pack()
btn_bg.pack()
btn_start.pack()
btn_exit.pack()

root.mainloop()

