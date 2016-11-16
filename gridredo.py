from tkinter import *
from tkinter import ttk

root=Tk()
root.title('Login')

menuframe=Menu(root)
root.config(menu=menuframe)

mainframe=ttk.Frame(root, width=100)
mainframe.grid(row=2, column=3)

filemenu=Menu(menuframe)
menuframe.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)

def clear():
    namentry.delete(0, 'end')
    passentry.delete(0, 'end')

namelbl=ttk.Label(root, text='Userame: ').grid(row=1, column=1, sticky=(N,S,E,W), padx=10, pady=10)
passlbl=ttk.Label(root, text='Password: ').grid(row=2, column=1, sticky=(N,S,E,W), padx=10, pady=10)

username=StringVar()
password=StringVar()

namentry=ttk.Entry(root, textvariable=username, width=10)
namentry.grid(row=1, column=2, padx=10, pady=10, sticky=(E, W))
passentry=ttk.Entry(root, textvariable=password, width=10)
passentry.grid(row=2, column=2, padx=10, pady=10, sticky=(E, W))
passentry.config(show='*')

loginbtn=ttk.Button(root, text='Login', command=clear)
loginbtn.grid(row=3, column=2, columnspan=2, sticky=(E,W), padx=10, pady=10)

root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.mainloop()
