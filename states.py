from tkinter import *
from tkinter import ttk

def answer(event):
    try:
        respond.set('Hi '+Name.get()+' from '+State.get()+'!')
    except:
        pass
        
root=Tk()
root.title('State')

mainframe=ttk.Frame(root, padding='100 100 100 100')
mainframe.grid(row=1, column=1, sticky=(N,W,E,S))
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

Name=StringVar()
State=StringVar()
respond=StringVar()

ttk.Label(mainframe, text='Name: ').grid(row=1, column=1)
name=ttk.Entry(mainframe, textvariable=Name)
name.grid(row=1, column=2)

ttk.Label(mainframe, text='State: ').grid(row=2, column=1)
combo=ttk.Combobox(mainframe, textvariable=State, width=17)
combo.grid(row=2, column=2)
combo['values']=('Texas', 'Maine', 'Oklahoma', 'Colorado', 'Arizona')
combo.bind('<<ComboboxSelected>>', answer)

ttk.Label(mainframe, textvariable=respond).grid(row=3, column=2)
