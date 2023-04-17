# Импортируем нужные модули
import os
from tkinter import *

# Базовые функции
def shutdown():
    return os.system("shutdown /s /t 1")
def restart():
    return os.system("shutdown /r /t 1")
def logout():
    return os.system("shutdown -l")
def shutdown_after_time():
    offtime = int(timer.get())
    time = offtime * 60
    return os.system(f"shutdown /s -t {time}")


# tkinter
master = Tk()
 
# настройки
master.configure(bg='light grey')
master.title("Выключение ПК")
master.geometry("250x120")
master.resizable(False, False)

#делаем марафет
text = Label(master, text="Выкл. через")  
text.grid(column=0, row=0) 

timer = Entry(master,width=10)  
timer.grid(column=1, row=0)  

# создаем кнопки
# кнопки будут выполнять функции
Button(master, text="минут", command=shutdown_after_time).grid(column=2,row=0)
Button(master, text="Выключить сейчас", command=shutdown).grid(row=1)
Button(master, text="Перезагрузить", command=restart).grid(row=2)
Button(master, text="Выйти за профиля", command=logout).grid(row=3)


mainloop()

