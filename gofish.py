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
import random
import time

root=Tk()
root.geometry("550x300")
menuframe=Menu(root)
root.config(menu=menuframe)

def showbox():
    messagebox.showinfo(title='GoFish', message='This version of GoFish is just like the card game! When asked what card to ask for, choose a card from the comobobox and press ASK. If the PC has the card, it will be given to you. If not, then you draw from the fishbowl. Same rules apply for the PC. Whenever you have four of the same card, you earn a point. Whoever has the most points when the fishbowl is empty wins!')

filemenu=Menu(menuframe)
menuframe.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)

helpmenu=Menu(menuframe)
menuframe.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=showbox)

def play_playersturn(*args):
    card=askcards.get()
    if card in pcards:
        saypc.set("Player Two gave you "+card+'\n'+"Now it's Player Two's turn!")
        #saypc.set('')
        x=True
        for i in range(len(pcards)):
            if card in pcards:
                pcards.remove(card)
                playercards.append(card)
                mycards.insert(0,card)
        #time.sleep(3)
        play_pcturn(*args)
    elif card not in pcards:
        saypc.set("Player Two didn't have that card and you drew from the fishbowl"+'\n'+"Now it's Player Two's turn!")
        #saypc.set('')
        x=False
        newcard=random.choice(deck)
        deck.remove(newcard)
        playercards.append(newcard)
        mycards.insert(0,newcard)
        #time.sleep(3)
        play_pcturn(*args)

def play_pcturn(*args):
    for i in pcards:
        num=pcards.count(i)
        if num>1:
            if i in playercards:
                playercards.remove(i)
                pcards.append(i)
                mycards.remove(i)
                saypctwo.set('Player Two took'+i+'from you')
                #saypctwo.set('')
                #time.sleep(3)
                root.mainloop()
    newcard=random.choice(deck)
    deck.remove(newcard)
    pcards.append(newcard)
    saypctwo.set('Player Two went Go Fish and took a card from the fish bowl'+'\n'+"It's your turn!")
    #saypctwo.set('')
    #time.sleep(3)
    check_player(*args)

def check_player(*args):
    playerpoint=0
    if ('2 of spades' and '2 of hearts' and '2 of clubs' and '2 of diamonds') in playercards:
        playercards.remove('2 of spades')
        playercards.remove('2 of hearts')
        playercards.remove('2 of clubs')
        playercards.remove('2 of diamonds')
        playerpoint+=1
    elif ('3 of spades' and '3 of hearts' and '3 of clubs' and '3 of diamonds') in playercards:
        playercards.remove('3 of spades')
        playercards.remove('3 of hearts')
        playercards.remove('3 of clubs')
        playercards.remove('3 of diamonds')
        playerpoint+=1
    elif ('4 of spades' and '4 of hearts' and '4 of clubs' and '4 of diamonds') in playercards:
        playercards.remove('4 of spades')
        playercards.remove('4 of hearts')
        playercards.remove('4 of clubs')
        playercards.remove('4 of diamonds')
        playerpoint+=1
    elif ('5 of spades' and '5 of hearts' and '5 of clubs' and '5 of diamonds') in playercards:
        playercards.remove('5 of spades')
        playercards.remove('5 of hearts')
        playercards.remove('5 of clubs')
        playercards.remove('5 of diamonds')
        playerpoint+=1
    elif ('6 of spades' and '6 of hearts' and '6 of clubs' and '6 of diamonds') in playercards:
        playercards.remove('6 of spades')
        playercards.remove('6 of hearts')
        playercards.remove('6 of clubs')
        playercards.remove('6 of diamonds')
        playerpoint+=1
    elif ('7 of spades' and '7 of hearts' and '7 of clubs' and '7 of diamonds') in playercards:
        playercards.remove('7 of spades')
        playercards.remove('7 of hearts')
        playercards.remove('7 of clubs')
        playercards.remove('7 of diamonds')
        playerpoint+=1
    elif ('8 of spades' and '8 of hearts' and '8 of clubs' and '8 of diamonds') in playercards:
        playercards.remove('8 of spades')
        playercards.remove('8 of hearts')
        playercards.remove('8 of clubs')
        playercards.remove('8 of diamonds')
        playerpoint+=1
    elif ('9 of spades' and '9 of hearts' and '9 of clubs' and '9 of diamonds') in playercards:
        playercards.remove('9 of spades')
        playercards.remove('9 of hearts')
        playercards.remove('9 of clubs')
        playercards.remove('9 of diamonds')
        playerpoint+=1
    elif ('Ace of spades' and 'Ace of hearts' and 'Ace of clubs' and 'Ace of diamonds') in playercards:
        playercards.remove('Ace of spades')
        playercards.remove('Ace of hearts')
        playercards.remove('Ace of clubs')
        playercards.remove('Ace of diamonds')
        playerpoint+=1
    elif ('Jack of spades' and 'Jack of hearts' and 'Jack of clubs' and 'Jack of diamonds') in playercards:
        playercards.remove('Jack of spades')
        playercards.remove('Jack of hearts')
        playercards.remove('Jack of clubs')
        playercards.remove('Jack of diamonds')
        playerpoint+=1
    elif ('King of spades' and 'King of hearts' and 'King of clubs' and 'King of diamonds') in playercards:
        playercards.remove('King of spades')
        playercards.remove('King of hearts')
        playercards.remove('King of clubs')
        playercards.remove('King of diamonds')
        playerpoint+=1
    elif ('Queen of spades' and 'Queen of hearts' and 'Queen of clubs' and 'Queen of diamonds') in playercards:
        playercards.remove('Queen of spades')
        playercards.remove('Queen of hearts')
        playercards.remove('Queen of clubs')
        playercards.remove('Queen of diamonds')
        playerpoint+=1
    check_pc(*args)

def check_pc(*args):
    pcpoint=0
    if ('2 of spades' and '2 of hearts' and '2 of clubs' and '2 of diamonds') in pcards:
        pcards.remove('2 of spades')
        pcards.remove('2 of hearts')
        pcards.remove('2 of clubs')
        pcards.remove('2 of diamonds')
        pcpoint+=1
    elif ('3 of spades' and '3 of hearts' and '3 of clubs' and '3 of diamonds') in pcards:
        pcards.remove('3 of spades')
        pcards.remove('3 of hearts')
        pcards.remove('3 of clubs')
        pcards.remove('3 of diamonds')
        pcpoint+=1
    elif ('4 of spades' and '4 of hearts' and '4 of clubs' and '4 of diamonds') in pcards:
        pcards.remove('4 of spades')
        pcards.remove('4 of hearts')
        pcards.remove('4 of clubs')
        pcards.remove('4 of diamonds')
        pcpoint+=1
    elif ('5 of spades' and '5 of hearts' and '5 of clubs' and '5 of diamonds') in pcards:
        pcards.remove('5 of spades')
        pcards.remove('5 of hearts')
        pcards.remove('5 of clubs')
        pcards.remove('5 of diamonds')
        pcpoint+=1
    elif ('6 of spades' and '6 of hearts' and '6 of clubs' and '6 of diamonds') in pcards:
        pcards.remove('6 of spades')
        pcards.remove('6 of hearts')
        pcards.remove('6 of clubs')
        pcards.remove('6 of diamonds')
        pcpoint+=1
    elif ('7 of spades' and '7 of hearts' and '7 of clubs' and '7 of diamonds') in pcards:
        pcards.remove('7 of spades')
        pcards.remove('7 of hearts')
        pcards.remove('7 of clubs')
        pcards.remove('7 of diamonds')
        pcpoint+=1
    elif ('8 of spades' and '8 of hearts' and '8 of clubs' and '8 of diamonds') in pcards:
        pcards.remove('8 of spades')
        pcards.remove('8 of hearts')
        pcards.remove('8 of clubs')
        pcards.remove('8 of diamonds')
        pcpoint+=1
    elif ('9 of spades' and '9 of hearts' and '9 of clubs' and '9 of diamonds') in pcards:
        pcards.remove('9 of spades')
        pcards.remove('9 of hearts')
        pcards.remove('9 of clubs')
        pcards.remove('9 of diamonds')
        pcpoint+=1
    if ('Ace of spades' and 'Ace of hearts' and 'Ace of clubs' and 'Ace of diamonds') in pcards:
        pcards.remove('Ace of spades')
        pcards.remove('Ace of hearts')
        pcards.remove('Ace of clubs')
        pcards.remove('Ace of diamonds')
        pcpoint+=1
    elif ('Jack of spades' and 'Jack of hearts' and 'Jack of clubs' and 'Jack of diamonds') in pcards:
        pcards.remove('Jack of spades')
        pcards.remove('Jack of hearts')
        pcards.remove('Jack of clubs')
        pcards.remove('Jack of diamonds')
        pcpoint+=1
    elif ('King of spades' and 'King of hearts' and 'King of clubs' and 'King of diamonds') in pcards:
        pcards.remove('King of spades')
        pcards.remove('King of hearts')
        pcards.remove('King of clubs')
        pcards.remove('King of diamonds')
        pcpoint+=1
    elif ('Queen of spades' and 'Queen of hearts' and 'Queen of clubs' and 'Queen of diamonds') in pcards:
        pcards.remove('Queen of spades')
        pcards.remove('Queen of hearts')
        pcards.remove('Queen of clubs')
        pcards.remove('Queen of diamonds')
        pcpoint+=1

deckdisplay=['2 of hearts','3 of hearts','4 of hearts','5 of hearts','6 of hearts','7 of hearts','8 of hearts','9 of hearts','2 of diamonds','3 of diamonds','4 of diamonds','5 of diamonds','6 of diamonds','7 of diamonds','8 of diamonds','9 of diamonds','2 of spades','3 of spades','4 of spades','5 of spades','6 of spades','7 of spades','8 of spades','9 of spades','2 of clubs','3 of clubs','4 of clubs','5 of clubs','6 of clubs','7 of clubs','8 of clubs','9 of clubs','Jack of clubs','Queen of clubs','King of clubs','Ace of clubs','Jack of spades','Queen of spades','King of spades','Ace of spades','Jack of diamonds','Queen of diamonds','King of diamonds','Ace of diamonds','Jack of hearts','Queen of hearts','King of hearts','Ace of hearts']
deck=['2 of hearts','3 of hearts','4 of hearts','5 of hearts','6 of hearts','7 of hearts','8 of hearts','9 of hearts','2 of diamonds','3 of diamonds','4 of diamonds','5 of diamonds','6 of diamonds','7 of diamonds','8 of diamonds','9 of diamonds','2 of spades','3 of spades','4 of spades','5 of spades','6 of spades','7 of spades','8 of spades','9 of spades','2 of clubs','3 of clubs','4 of clubs','5 of clubs','6 of clubs','7 of clubs','8 of clubs','9 of clubs','Jack of clubs','Queen of clubs','King of clubs','Ace of clubs','Jack of spades','Queen of spades','King of spades','Ace of spades','Jack of diamonds','Queen of diamonds','King of diamonds','Ace of diamonds','Jack of hearts','Queen of hearts','King of hearts','Ace of hearts']

playercards = []
pcards = []
for i in range(7):
    card=random.choice(deck)
    deck.remove(card)
    playercards.append(card)
for i in range(7):
    card=random.choice(deck)
    deck.remove(card)
    pcards.append(card)

cards=StringVar()
mydeck=StringVar(value=playercards)
saypc=StringVar()
saypctwo=StringVar()

askcards=ttk.Combobox(root, textvariable=cards, state='readonly')
askcards.grid(row=3, column=2, padx=5, pady=5)
askcards['value']=deckdisplay

mycards=Listbox(root, listvariable=mydeck, height=15)
mycards.grid(row=1, column=1, pady=5, padx=5, rowspan=3)
mycards.configure(selectmode="browse", exportselection=False)

pctalk=ttk.Label(root, textvariable=saypc)
pctalk.grid(row=1, column=2, padx=5, pady=5)

pctalktwo=ttk.Label(root, textvariable=saypctwo)
pctalktwo.grid(row=2, column=2, padx=5, pady=5)

#startbtn=ttk.Button(root, text='START', command=start)
#startbtn.grid(row=5, column=1)
askbtn=ttk.Button(root, text='ASK', command=play_playersturn)
askbtn.grid(row=4, column=2, padx=5, pady=5)

root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

saypctwo.set('What card are you going to ask for?')
print(pcards)

root.mainloop()
