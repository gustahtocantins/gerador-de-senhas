import secrets, string, os
from tkinter import *
win = Tk()
win.maxsize(width=200, height=130)
win.minsize(width=200, height=130)
win.title("Gerar Senha")
win["bg"] = "black"
def gerar():
   a = string.ascii_letters + string.digits
   pas = "".join(secrets.choice(a) for i in range(9))
   texto["text"] = f"{pas}"

texto = Label(win, text="", font=("arial", "25"))
texto["bg"] = "red"
texto.pack()
texto.place(bordermode=OUTSIDE, x=5, y=20)

botao = Button(win, text="Gerar", command=gerar, bg="red")
botao["fg"] = "white"
botao["font"] = ("arial","20","bold")
botao.pack()
botao.place(bordermode=OUTSIDE, x=60, y=80, width=90, height=40)

win.mainloop()
