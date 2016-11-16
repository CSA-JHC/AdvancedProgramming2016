from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def calculate(*args):
    try:
        value = float(far.get())
        num=(((value-32)/9)*5)
        if value>=230:
            cel.set("IS IT EVEN POSSIBLE FOR IT TO BE THIS HOT?!")
        elif value<30:
            cel.set("Get a jacket or something, you might freeze.")
        else:
            cel.set(num)
    except ValueError:
        pass

root = Tk()
root.title("Celsius to Fahrenheit")

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

far = StringVar()
cel = StringVar()

far_entry = ttk.Entry(mainframe, width=10, textvariable=far)
far_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=cel).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="How Hot", command=calculate).grid(column=2, row=4, sticky=N)

ttk.Label(mainframe, text="Celcius").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="degrees Fahrenheit").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=50)

far_entry.focus()
root.bind('<space>', calculate)

root.mainloop()
