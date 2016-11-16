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

#imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from decimal import *

#important stuff: set frame, etc.
root=Tk()
root.title("Database")
menuframe=Menu(root)
root.config(menu=menuframe)

#shows instructions through messagebox
def showbox():
    messagebox.showinfo(title='Database - Version 0.1', message="This program will allow you to store your information in a file or retrieve your inforamation from a file. Please be sure to fill in all information and to fill it in correctly. Otherwise it will not submit the information. If you happen to fill in the date incorrectly, for example, February 30, the information will not submit. Please use this program wisely and don't screw around!")

#menus -- file with exit and help with about
filemenu=Menu(menuframe)
menuframe.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)
helpmenu=Menu(menuframe)
menuframe.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=showbox)

#clears screen when submit is entered
def clear(*args):
    useridentry.delete(0,END)
    firstentry.delete(0,END)
    lastentry.delete(0,END)
    streetentry.delete(0,END)
    street2entry.delete(0,END)
    states.set('')
    cityentry.delete(0,END)
    zipentry.delete(0,END)
    d.delete('1.0',END)
    pricentry.delete(0,END)
    month.set('')
    day.set('')
    year.set('')
    finalprice.set('')
    taxnum.set('')
    ship.selection_clear(0,END)

#sets the tax and total when something in listbox is clicked
def setlbl(*args):
    try:
        shiprice=ship.curselection()
        if 0 in shiprice:
            shipmoney=5
        elif 1 in shiprice:
            shipmoney=10
        elif 2 in shiprice:
            shipmoney=15
        elif 3 in shiprice:
            shipmoney=20
        elif 4 in shiprice:
            shipmoney=25
        taxvalue = float(pricentry.get()) * 0.0825
        tax=(round(taxvalue, 2))
        totalamt = (tax + float(pricentry.get()) + shipmoney)
        taxnum.set(tax)
        finalprice.set(round(totalamt,2))
    except:
        messagebox.showinfo(title='ERROR', message="You didn't enter an appropriate price.")
        root.mainloop()

#checks to make sure everything is filled in
def check(*args):
    if len(useridentry.get())<9 or len(useridentry.get())>9:
        messagebox.showinfo(title='ERROR', message="You entered a false PO Number.")
        root.mainloop()
    if d.get('1.0', END).strip('\n')=='' or firstentry.get()=='' or lastentry.get()=='' or streetentry.get()=='' or street2entry.get()=='' or states.get()=='' or cityentry.get()=='' or price.get()=='':
        messagebox.showinfo(title='ERROR', message="You didn't enter all the information.")
        root.mainloop()
    if (month.get()=='February' and day.get()=='30') or ((month.get()=='February' or month.get()=='April' or month.get()=='June' or month.get()=='September' or month.get()=='November') and day.get()=='31'):
        messagebox.showinfo(title='ERROR', message="You entered a false date.")
        root.mainloop()
    if month.get()=='' or day.get()=='' or year.get()=='':
        messagebox.showinfo(title='ERROR', message="You didn't enter all the information.")
        root.mainloop()
    write(*args)

#finds shipping and writes everything to a file, then goes to clear
def write(*args):
        file = open('database.csv', 'a')
        file.write(useridentry.get() + ',')
        file.write(firstentry.get() + ',')
        file.write(lastentry.get() + ',')
        file.write(streetentry.get() + ',')
        file.write(street2entry.get() + ',')
        file.write(states.get() + ',')
        file.write(cityentry.get() + ',')
        file.write(zipentry.get() + ',')
        file.write(d.get('1.0', END).strip('\n') + ',')
        file.write(price.get() + ',')
        shiprice = ship.curselection()
        if 0 in shiprice:
            money = 5
        elif 1 in shiprice:
            money = 10
        elif 2 in shiprice:
            money = 15
        elif 3 in shiprice:
            money = 20
        elif 4 in shiprice:
            money = 25
        file.write(str(money) + ',')
        file.write(month.get() + ',')
        file.write(day.get() + ',')
        file.write(year.get() + '\n')
        file.close()
        clear(*args)

#finds all info and sets to designated area, finds tax and total based on info and sets it
def find(*args):
     file=open('database.csv','r')
     for line in file:
         if useridentry.get() in line:
             line=line.split(',')
     firstentry.insert(0,line[1])
     lastentry.insert(0,line[2])
     streetentry.insert(0,line[3])
     street2entry.insert(0,line[4])
     states.set(line[5])
     cityentry.insert(0,line[6])
     zipentry.insert(0,line[7])
     d.insert(INSERT,line[8])
     pricentry.insert(0,line[9])
     month.set(line[11])
     day.set(line[12])
     year.set(line[13])
     if line[10]=='5':
         ship.selection_set(0)
         money=5
     if line[10]=='10':
         ship.selection_set(1)
         money=10
     if line[10]=='15':
         ship.selection_set(2)
         money=15
     if line[10]=='20':
         ship.selection_set(3)
         money=20
     if line[10]=='25':
         ship.selection_set(4)
         money=25
         
     taxvalue = float(pricentry.get()) * 0.0825
     tax=(round(taxvalue, 2))
     totalamt = (tax + float(pricentry.get()) + money)
     taxnum.set(tax)
     finalprice.set(round(totalamt,2))

#for listbox
days=('1 day - $5', '2 day - $10', '3 day - $15', '4 day - $20', '5 day - $25')

#variables
POentry=StringVar()
FirstName=StringVar()
LastName=StringVar()
street=StringVar()
street2=StringVar()
state=StringVar()
city=StringVar()
zipcode=IntVar()
price=StringVar()
shipping=StringVar(value=days)
months=StringVar()
days=StringVar()
years=StringVar()
taxnum=StringVar()
finalprice=StringVar()

#PO NUMBER -- entry for PO number
#its automatically inserted in, but you can change it if you're retrieving info
useridlbl=ttk.Label(root, text='PO Number: ').grid(column=1, row=1)
useridentry=ttk.Entry(root, textvariable=POentry)
useridentry.grid(column=2, row=1, padx=5, pady=5)
useridentry.insert(0, (str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))))

#FIRST NAME -- entry for first name
firstlbl=ttk.Label(root, text='First Name: ').grid(column=1, row=2)
firstentry=ttk.Entry(root, textvariable=FirstName)
firstentry.grid(column=2, row=2, padx=5, pady=5)

#LAST NAME -- entry for last name
lastlbl=ttk.Label(root, text='Last Name: ').grid(column=1, row=3)
lastentry=ttk.Entry(root, textvariable=LastName)
lastentry.grid(column=2, row=3, padx=5, pady=5)

#STREETS -- entry for street(s)
streetlbl=ttk.Label(root, text='Street: ').grid(column=1, row=4)
streetentry=ttk.Entry(root, textvariable=street)
streetentry.grid(column=2, row=4, padx=5, pady=5)
street2lbl=ttk.Label(root, text='Street (2): ').grid(column=1, row=5)
street2entry=ttk.Entry(root, textvariable=street2)
street2entry.grid(column=2, row=5, padx=5, pady=5)

#STATE -- combobox for state
statelbl=ttk.Label(root, text='State:').grid(column=1, row=6)
states=ttk.Combobox(root, textvariable=state, state='readonly', width=15)
states.grid(column=2, row=6, padx=5, pady=5)
states['values']=('Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennesse','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming')

#CITY -- entry for city
citylbl=ttk.Label(root, text='City: ').grid(column=1, row=7)
cityentry=ttk.Entry(root, textvariable=city)
cityentry.grid(column=2, row=7, padx=5, pady=5)

#ZIPCODE -- entry for zipcode
ziplbl=ttk.Label(root, text='Zipcode: ').grid(column=1, row=8)
zipentry=ttk.Entry(root, textvariable=zipcode)
zipentry.grid(column=2, row=8)

#DESCRIPTION -- entry for description of what they bought
d=Text(root, width=20, height=10)
d.grid(column=2, row=15, padx=5, pady=5, rowspan=3)
d.config(wrap=WORD)
dlbl=ttk.Label(root, text='Description: ').grid(column=1, row=15)

#PRICE -- entry for price
pricelbl=ttk.Label(root, text='Price: ').grid(column=4, row=1)
pricentry=ttk.Entry(root, textvariable=price)
pricentry.grid(column=5, row=1, padx=5, pady=5)

#TAX -- shows total amount of tax
taxlbl=ttk.Label(root, text='Tax: ').grid(column=4, row=2)
taxamtlbl=ttk.Label(root, textvariable=taxnum).grid(column=5, row=2)

#SHIPPING -- lbl for shipping
shiplbl=ttk.Label(root, text='Shipping: ').grid(column=4, row=3)
ship=Listbox(root, listvariable=shipping, height=5)
ship.grid(column=5, row=3, sticky=(N,W,E,S), padx=5, pady=5, rowspan=3)
ship.configure(selectmode='browse', exportselection=False)

#TOTAL -- shows the total amount of money spent
totallbl=ttk.Label(root, text='Total: ').grid(column=4, row=6)
totalamt=ttk.Label(root, textvariable=finalprice).grid(column=5, row=6)

#PRICE DATE -- put in when they made the purchase
pricedatelbl=ttk.Label(root, text='Purchase Date: ').grid(column=4, row=7)
month=ttk.Combobox(root, textvariable=months, state='readonly', width=10)
month.grid(column=5, row=7, padx=5, pady=5)
day=ttk.Combobox(root, textvariable=days, state='readonly', width=10)
day.grid(column=6, row=7, padx=5, pady=5)
year=ttk.Combobox(root, textvariable=years, state='readonly', width=10)
year.grid(column=7, row=7, padx=5, pady=5)
#values for month, day, and year
month['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
day['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
year['values']=('2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040')

#BUTTONS (RETRIEVE AND SUBMIT) - submit button goes to check and retrieve button goes to find
submitbtn=ttk.Button(root, text='Submit', command=check).grid(column=5, row=9)
retrievebtn=ttk.Button(root, text='Retrieve', command=find).grid(column=5, row=10)

#COLUMNCONFIGURE -- allows widgets to expand with window
root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.columnconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.columnconfigure(5,weight=1)
root.rowconfigure(6,weight=1)
root.columnconfigure(6,weight=1)
root.rowconfigure(7,weight=1)
root.columnconfigure(7,weight=1)
root.rowconfigure(8,weight=1)
root.rowconfigure(9,weight=1)
root.rowconfigure(10,weight=1)

#bind listbox to function to set tax and total
root.bind('<<ListboxSelect>>', setlbl)
zipentry.delete(0,END)

#do it again
root.mainloop()
