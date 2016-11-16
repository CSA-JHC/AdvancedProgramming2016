# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

#import stuff for tkiner
from tkinter import *
from tkinter import ttk
#import messagebox
from tkinter import messagebox
#import csv for file
import csv

def showBox():
    #when about is pressed, show info through a messagebox
    messagebox.showinfo(title="Example Changes", message="Version 0.1")
def writeFile():
    #when OK is selected, open file to write info selected
    file=open('examplechanges.csv', 'a')
    #writes info to csv file
    file.write(str(boxone.get())+','+str(boxtwo.get())+','+str(boxthree.get())+','+name.get()+'\n')
    file.close()    #close file
    #go to clear to clear info
    clear()
def clear():
    #when CANCEL is selected, clear all info without writing to file
    name.delete(0,END)
    boxone.set(0)
    boxtwo.set(0)
    boxthree.set(0)

root=Tk()
root.title('Example Changes')   #title of window
menuframe=Menu(root)
root.config(menu=menuframe)

#take off lines on menu
root.option_add('*tearOff', FALSE)

#exitmenu -- submenu, 'File', that allows for you to exit
exitmenu=Menu(menuframe)
menuframe.add_cascade(label="File", menu=exitmenu)
exitmenu.add_command(label="Exit", command=root.quit)

#help menu -- submenu, 'Help', that has 'About' (when clicked goes to the showBox function)
helpmenu=Menu(menuframe)
menuframe.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=showBox)

#variables
boxone=BooleanVar() #for false and true on checkbuttons
boxtwo=BooleanVar()
boxthree=BooleanVar()
namevar=StringVar() #for entry

#name entry and label -> indicating entry is for name
namelbl=ttk.Label(root, text='Name')
name=ttk.Entry(root, width=25, textvariable=namevar)
namelbl.grid(column=3, row=1)   #where i want label and entry to go
name.grid(column=4, row=1, columnspan=2)

#buttons -- OK and CANCEL
ok=ttk.Button(root, text="OK", command=writeFile)   #goes to function of writeFile
cancel=ttk.Button(root, text="Cancel", command=clear)   #goes to function of clear
cancel.grid(column=5, row=2, sticky=(W,E))  #where i want buttons
ok.grid(column=4, row=2, sticky=(W,E))

#checkbuttons -- becomes TRUE when checked
one=ttk.Checkbutton(root, text='One', variable=boxone, onvalue=True)
two=ttk.Checkbutton(root, text='Two', variable=boxtwo, onvalue=True)
three=ttk.Checkbutton(root, text='Three', variable=boxthree, onvalue=True)
one.grid(column=1, row=2, sticky=(W,E)) #where i want checkboxes
two.grid(column=2, row=2, sticky=(W,E))
three.grid(column=3, row=2, sticky=(W,E))

#allows labels, checkbuttons, etc. to move with window when expanded
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

#do it again/run
root.mainloop()