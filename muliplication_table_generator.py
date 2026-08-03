import tkinter as tk
from tkinter.ttk import*
gui=tk.Tk()
#gui.geometry('300x300')
title=tk.Label(gui, text='multiplication table generator ',bg='white', font=('Arial', 14, 'bold'))
title.grid(row=0,column=2 ,columnspan=3)
numrange=tk.Label(gui, text=' Select the number and the range',bg='white',font=('Arial',8,'bold'))
def result():
    store=''
    for i in range(radio.get()):
result=tk.Button(gui, text='Result',bg='white',font=('Arial',8,'bold'))
result.grid(row=5,column=3)
numrange.grid(row=1,column=3)
num=tk.IntVar()
comboxstorage=Combobox(gui,textvariable=num)
comboxstorage.grid(row=1,column=4)
comboxstorage['values']=tuple(range(101))
radio=tk.IntVar()
radiostorage1=Radiobutton(gui,text='10',variable=radio,value=10)
radiostorage1.grid(row=2,column=5)
radiostorage2=Radiobutton(gui,text='20',variable=radio,value=20)
radiostorage2.grid(row=4,column=5)
radiostorage3=Radiobutton(gui,text='30',variable=radio,value=30)
radiostorage3.grid(row=6,column=5)


gui.mainloop()