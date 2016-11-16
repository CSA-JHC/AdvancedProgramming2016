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

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#check to see if description has been filled and if something was selected
#otherwise don't do anything
def check(*args):
    try:
        index=int(l.curselection()[0])
        if len(t.get(1.0,END).strip('\n'))!=0:
            pb_update(*args)
    except:
       root.mainloop()

#if both countries and description have been filled out
#fill progress barto 100%
def pb_update(*args):
    pbar['value']=100

#when clear is pressed, clear screen
def clear(*args):
    pbar['value']=0
    l.selection_clear(0, END)
    t.delete('1.0', END)

#shows what the program is about
def showbox():
    messagebox.showinfo(title='Travel Log - Version 0.1', message='This program helps you sort out which countries you want to visit. Simply choose a country, then write what you think about it in the description box. Press SUBMIT to write it to a file and CLEAR to clear the screen.')

#countries that can be selected
countries=('Afghanistan','Bahamas','Cambodia','Dominican Repbulic','Egypt','Finlad','Germany','Haiti','India','Japan','Kenya','Libya','Madagascar','Namibia','Oman','Pakistan','Qatar','Romania','Saudi Arabia','Taiwan','Uganda','Venezuela','Yemen','Zimbabwe')

#main window
root=Tk()
#for submenus
menuframe=Menu(root)
root.config(menu=menuframe)

#menus - file and help, exit and about respectively
filemenu=Menu(menuframe)
menuframe.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)  #quit when selected
helpmenu=Menu(menuframe)
menuframe.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=showbox)  #show messagebox when selected

#variables
listcountry=StringVar(value=countries)  #connected to the list of countries

#listbox
l=Listbox(root, listvariable=listcountry, height=5)
l.grid(column=0, row=1, sticky=(N,W,E,S))
l.configure(selectmode='browse', exportselection=False)

#scrollbar
s=ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=0, row=1, sticky=(N,S,E))
l['yscrollcommand']=s.set

#text box for description
t=Text(root, width=18, height=10)
t.grid(column=0, row=3)
t.config(wrap=WORD)

#progressbar
pbar=ttk.Progressbar(root, orient=VERTICAL, length=100, mode='determinate')
pbar.grid(column=2, row=3)

#buttons
submit=ttk.Button(root, text='Submit', command=check)  #go to check
submit.grid(column=1, row=0)
clear=ttk.Button(root, text='Clear', command=clear)  #go to clear
clear.grid(column=1, row=1)

#labels
descriptionlbl=ttk.Label(root, text='Description').grid(column=0, row=2)
countrieslbl=ttk.Label(root, text='Countries').grid(column=0, row=0)

#so it will expand
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(3, weight=1)

#do it again
root.mainloop()