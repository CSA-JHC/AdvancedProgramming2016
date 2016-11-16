from tkinter import *
from tkinter import ttk

global letternum
letternum=True

def clear(*args):
    if Gender.get()==0 or name.get()=='' or age.get()=='':
        root.mainloop()
    else:
        Gender.set(0)
        name.delete(0, END)
        age.delete(0,END)
        name.insert(0, 'Name')
        age.insert(0, 'Age')
def delete_n(event):
    name.delete(0, END)
    name.config(foreground='black')
def delete_a(event):
    age.delete(0, END)
    age.config(foreground='black')
def check(*args):
    try:
        for i in age.get():
            x=int(age.get())
        for i in name.get():
            if i.isdigit():
                root.mainloop()
        clear(*args)
    except ValueError:
        pass
    
root=Tk()
root.title('Name/Age')

mainframe=ttk.Frame(root, padding='100 100 100 100')
mainframe.grid(column=1, row=1, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Name=StringVar()
Age=StringVar()
Gender=IntVar()
error=StringVar()

button=ttk.Button(mainframe, text="Submit", command=check).grid(column=1, row=4, sticky=(W, E))
label=ttk.Label(mainframe, textvariable=error).grid(column=2, row=4, sticky=(W,E))

name=ttk.Entry(mainframe, textvariable=Name)
name.grid(column=1, row=1, sticky=(W, E))
name.insert(0, 'Name')

age=ttk.Entry(mainframe, textvariable=Age)
age.grid(column=2, row=1, sticky=(W, E))
age.insert(0, 'Age')

female=ttk.Radiobutton(mainframe, text='Female', variable=Gender, value=1)
male=ttk.Radiobutton(mainframe, text='Male', variable=Gender, value=2)
other=ttk.Radiobutton(mainframe, text='Other', variable=Gender, value=3)

female.grid(column=1, row=2, sticky=(W, E))
male.grid(column=2, row=2, sticky=(W, E))
other.grid(column=3, row=2, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=15)

name.bind('<Button-1>', delete_n)
age.bind('<Button-1>', delete_a)
root.bind('<Return>', check)

root.mainloop()
