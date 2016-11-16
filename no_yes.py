from tkinter import *
from tkinter import ttk

def button_status(*args):
    try:
        #if yes is active and no isn't set button to normal
        if y.get()==1:
            n.set(0)
            button.config(state='normal')
        elif n.get()==1:
            y.set(0)
            answer.set('')
            button.config(state='disabled')
        #anything else, disable button
        else:
            button.config(state='disabled')
            answer.set('')
    except:
        #if it doesn't work, stay disabled
        button.config(state='disabled')
        answer.set('')

def hi(*args):
    try:
        #if hi button is clicked say hi
        answer.set("HI!")
    except:
        #if it doesn't work, say nothing
        answer.set('')

#parent/root    
root=Tk()
root.title("no_yes")

#mainframe
mainframe=ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#string and it variables
y=IntVar()
n=IntVar()
answer=StringVar()

#checkbuttons, go to button_status to disable button
yes=ttk.Checkbutton(mainframe, text="Yes", variable=y, command=button_status).grid(column=1, row=1, sticky=(W, E))
no=ttk.Checkbutton(mainframe, text="No", variable=n, command=button_status).grid(column=1, row=2, sticky=(W, E))
#button, go to hi to say hi
button=ttk.Button(mainframe, text="Hi", command=hi, state=DISABLED) #disable button
button.grid(column=1, row=4, sticky=N)
#label
ttk.Label(mainframe, textvariable=answer).grid(column=2, row=4, sticky=(W,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=10)
root.bind('<Return>', hi)
root.mainloop()
