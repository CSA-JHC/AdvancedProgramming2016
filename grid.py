from tkinter import *
from tkinter import ttk

root=Tk()
root.title=('Login')

mainframe=ttk.Frame(root, padding="25 25 25 25")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Username').grid(column=0, row=0, sticky=(N, W))
ttk.Label(mainframe, text='Password').grid(column=0, row=1, sticky=(N, W))
ttk.Label(mainframe).grid(column=3, row=0, sticky=(N, W))
ttk.Button(mainframe, text='Login', command=clear).grid(row=2, column=2, columnspan=2, sticky=(N, W, E, S))

username=StringVar()
password=StringVar()

un=ttk.Entry(mainframe, textvariable=username)
un.grid(column=1, row=0, sticky=(W, E))
pw=ttk.Entry(mainframe, textvariable=password)
pw.grid(column=1, row=1, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

root.mainloop()