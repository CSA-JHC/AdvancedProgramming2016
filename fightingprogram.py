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

#imports from tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#import random to select random attack
import random

#shows user stats of person selected
class Info(object):
    def __init__(self, name, weapon, health, defense):
        self.name=name
        self.weapon=weapon
        self.health=health
        self.defense=defense
    def show(self, name, weapon, health, defense):
        #sets infos to show user
        infos.set('Name: '+name+'\n'+'Weapon: '+weapon+'\n'+'Defense: '+defense+'\n'+'Health: '+str(health))

#makes the two people selected fight
class fight():
    def __init__(self, name_m, name_d, strength_m, strength_d):
        self.name_m=name_m
        self.name_d=name_d
        self.strength_m=strength_m
        self.strength_d=strength_d
    def attack(self, name_m, name_d, strength_m, strength_d):
        #while the strength is still larger than 0 keep going
        while (strength_m or strength_d)>0:
            attack_m=random.randint(1, 20)
            strength_d=strength_d-attack_m
            attack_d=random.randint(1, 20)
            strength_m=strength_m-attack_d
        #if the strength on dads side is smaller than zero he lost
        if strength_d<=0:
            infos.set(name_m+' '+'wins!')
            amountwins_m.set(amountwins_m.get()+1)
            amountloss_d.set(amountloss_d.get()+1)
        #if strength on moms side is smaller than zero she lost
        elif strength_m<=0:
            infos.set(name_d+' '+'wins!')
            amountwins_d.set(amountwins_d.get()+1)
            amountloss_m.set(amountloss_m.get()+1)
        #anything else is considered a tie
        else:
            infos.set('It was a tie...')

#dads side of the fam (info), goes to info class to show user stats
def dadside(*args):
    #gives me what is selected
    char=(char_d.curselection())
    #if this number is in char, then it is this person
    if 0 in char:
        person_d='Uncle'    #name
        weapon_d='Tachi Knife'  #weapon
        defense_d='Block'   #defense
        health_d=87 #health
        info=Info(person_d, weapon_d, health_d, defense_d)  #go to info
        info.show(person_d, weapon_d, health_d, defense_d)  #show this info
    elif 1 in char:
        person_d='Cousin'
        weapon_d='Ninja Star'
        defense_d='Deflect Weapon'
        health_d=99
        info=Info(person_d, weapon_d, health_d, defense_d)
        info.show(person_d, weapon_d, health_d, defense_d)
    elif 2 in char:
        person_d='Grandma'
        weapon_d='Bo Staff'
        defense_d='Block'
        health_d=59
        info=Info(person_d, weapon_d, health_d, defense_d)
        info.show(person_d, weapon_d, health_d, defense_d)
    elif 3 in char:
        person_d='Dad'
        weapon_d='Hook Swords'
        defense_d='Hook Weapon'
        health_d=92
        info=Info(person_d, weapon_d, health_d, defense_d)
        info.show(person_d, weapon_d, health_d, defense_d)

#moms side of the fam (info), goes to info class to show user stats
def momside(*args):
    #gives me whats selected
    char=(char_m.curselection())
    #if this number is in char, then it is this person
    if 0 in char:
        person_m='Auntie'   #name
        weapon_m='Kunai Knife'  #weapon
        defense_m='Deflect Weapon'  #defense
        health_m=93 #health
        info=Info(person_m, weapon_m, health_m, defense_m)  #go to info
        info.show(person_m, weapon_m, health_m, defense_m)  #show this info
    elif 1 in char:
        person_m='Grandpa'
        weapon_m='Chain Whip'
        defense_m='Whip Weapon'
        health_m=54
        info=Info(person_m, weapon_m, health_m, defense_m)
        info.show(person_m, weapon_m, health_m, defense_m)
    elif 2 in char:
        person_m='Great Uncle'
        weapon_m='Nunchucks'
        defense_m='Block'
        health_m=65
        info=Info(person_m, weapon_m, health_m, defense_m)
        info.show(person_m, weapon_m, health_m, defense_m)
    elif 3 in char:
        person_m='Mom'
        weapon_m='Katana'
        defense_m='Block'
        health_m=95
        info=Info(person_m, weapon_m, health_m, defense_m)
        info.show(person_m, weapon_m, health_m, defense_m)

#prepares info for the fight    
def goto(*args):
    #gives me what is selected
    char=char_m.curselection()
    #if this number is in char, then it is this person with this health
    if 0 in char:
        person_m='Auntie'   #name
        health_m=93 #health
    if 1 in char:
        person_m='Grandpa'
        health_m=54
    if 2 in char:
        person_m='Great Uncle'
        health_m=65
    if 3 in char:
        person_m='Mom'
        health_m=95

    #gives me what is selected
    char=char_d.curselection()
    #if this number is in char, then it is this person with this health
    if 0 in char:
        person_d='Uncle'    #name
        health_d=87 #health
    if 1 in char:
        person_d='Cousin'
        health_d=99
    if 2 in char:
        person_d='Grandma'
        health_d=59
    if 3 in char:
        person_d='Dad'
        health_d=92
    try:
        #go to battle with all the info
        battle=fight(person_m, person_d, health_m, health_d)
        battle.attack(person_m, person_d, health_m, health_d)
    except:
        pass
          
root=Tk()
menuframe=Menu(root)
root.config(menu=menuframe)
#title of window
root.title('Fight for the Check')

#show message box
def showbox():
    messagebox.showinfo(title='Fighting Program', message='A fighting program where the two selected characters fight each other for the check in order to pay for the meal.')

#take off line in submenus
root.option_add('*tearOff', FALSE)

#submenu - File
filemenu=Menu(menuframe)
menuframe.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)

#submenu - Help
helpmenu=Menu(menuframe)
menuframe.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=showbox)

#options in list box that you can choose from
dadfam=('Uncle', 'Cousin', 'Grandma', 'Dad')
momfam=('Auntie', 'Grandpa', 'Great Uncle', 'Mom')

#variables - amount of wins and losses and the characters
amountwins_m=IntVar()
amountwins_d=IntVar()
amountloss_m=IntVar()
amountloss_d=IntVar()
infos=StringVar()
characters_m=StringVar(value=momfam)
characters_d=StringVar(value=dadfam)

#set amounts of wins and losses to zero because they haven't done anything yet..
amountwins_m.set('0')
amountwins_d.set('0')
amountloss_m.set('0')
amountloss_d.set('0')


#labels - wins and losses
win_m=ttk.Label(root, text='WINS:').grid(column=1, row=3, sticky=W)
win_d=ttk.Label(root, text='WINS:').grid(column=5, row=3, sticky=W)
losses_m=ttk.Label(root, text='LOSSES:').grid(column=1, row=4, sticky=W)
losses_d=ttk.Label(root, text='LOSSES:').grid(column=5, row=4, sticky=W)
#labels - number of wins and losses
numwins_m=ttk.Label(root, textvariable=amountwins_m)
numwins_d=ttk.Label(root, textvariable=amountwins_d)
numloss_m=ttk.Label(root, textvariable=amountloss_m)
numloss_d=ttk.Label(root, textvariable=amountloss_d)
numwins_m.grid(column=2, row=3)
numwins_d.grid(column=6, row=3)
numloss_m.grid(column=2, row=4)
numloss_d.grid(column=6, row=4)
#labels - stats and error (just in case)
stats=ttk.Label(root, textvariable=infos)
stats.grid(column=3, row=5, rowspan=2, columnspan=3)

#listbox
char_m=Listbox(root, listvariable=characters_m, height=4)
char_d=Listbox(root, listvariable=characters_d, height=4)
char_m.grid(column=1, row=1, rowspan=2, columnspan=2)
char_d.grid(column=5, row=1, rowspan=2, columnspan=2)
#only allows for one option to be selected
char_m.configure(selectmode="browse", exportselection=False)
char_d.configure(selectmode="browse", exportselection=False)

#button
fightbutton=ttk.Button(root, text='Fight', command=goto)
fightbutton.grid(column=3, row=7, columnspan=2)

#move with expansion of screen
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)

#binds to return key and when something in listbox is clicked it shows stats
root.bind('<Return>', goto)
char_m.bind('<<ListboxSelect>>', momside)
char_d.bind('<<ListboxSelect>>', dadside)

#do it again
root.mainloop()
