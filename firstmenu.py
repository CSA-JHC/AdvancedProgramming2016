from tkinter import *

def doNothing(): #default function
    print("I won't...")

root=Tk()

#main menu
menu=Menu(root)
root.config(menu=menu)

#submenu
subMenu=Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator() #separates exit from new project and new
subMenu.add_command(label="Exit", command=root.quit)

#edit menu
editMenu=Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

#creating the toolbar
toolbar=Frame(root, bg="blue")
#buttons in toolbar
insertButton=Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton=Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

#show the toolbar
toolbar.pack(side=TOP)

root.mainloop() #do it again