import tkinter as Tk
from tkinter import  ttk
gui= Tk.Tk()
gui.geometry("300x300")
title=Tk.Label(gui, text='Coding class registration ',bg='white', font=('Arial', 14, 'bold'))
title.place(x=40,y=20)
course=Tk.Label(gui,text='select your course',bg='white')
course.place(x=110,y=50)
options = ('Python', 'Game Development', 'Web Design')
comboxstorage=ttk.Combobox(gui, values=options, state="readonly")
comboxstorage.current(1)
selected_value = comboxstorage.get().strip()
comboxstorage.place(x=90,y=80)
batch=Tk.Label(gui,text='select batch timing:',bg='white')
batch.place(x=90,y=120)
radio=Tk.StringVar()
radiostorage1=ttk.Radiobutton(gui,text='Morning(10 AM)',variable=radio,value='Morning(10 PM)')
radiostorage1.place(x=10,y=150)
radiostorage2=ttk.Radiobutton(gui,text='Evening(5 PM)',variable=radio,value='Evening(5 PM)')
radiostorage2.place(x=180,y=150)
enroll=Tk.Button(gui, text="Enroll now")
enroll.place(x=110, y=190)
gui.mainloop()




