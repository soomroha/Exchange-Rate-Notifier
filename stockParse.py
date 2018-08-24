from subprocess import call

call(["python", "-m", "pip", "install", "requests"])
call(["python", "-m", "pip", "install", "bs4"])

from tkinter import *
from tkinter import ttk, messagebox
import requests
import time
from bs4 import BeautifulSoup

watchList = {}

def get_data():
    page = requests.get("http://webrates.truefx.com/rates/connect.html?f=html")
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.findAll(text=True)

    currData = {}

    for x in range(0, 90, 9):
        pair = text[x]
        price = text[x+2] + text[x+3]
        currData[pair] = float(price)

    return currData

def onClick():

    pairing = int(radio.get())

    try:
        price = float(watchPrice.get())

        if (pairing == 1):
            watchList['EUR/USD'] = price
        elif (pairing == 2):
            watchList['USD/JPY'] = price
        elif (pairing == 3):
            watchList['GBP/USD'] = price
        elif (pairing == 4):
            watchList['EUR/GBP'] = price
        elif (pairing == 5):
            watchList['USD/CHF'] = price
        elif (pairing == 6):
            watchList['EUR/JPY'] = price
        elif (pairing == 7):
            watchList['EUR/CHF'] = price
        elif (pairing == 8):
            watchList['USD/CAD'] = price
        elif (pairing == 9):
            watchList['AUD/USD'] = price
        elif (pairing == 10):
            watchList['GBP/JPY'] = price
    except:
        messagebox.showinfo("Error", "please enter a valid price")

def checkNotifier():

    data = get_data()

    for pair in watchList:
        if data[pair] == watchList[pair]:
            del watchList[pair]
            message = "Your alert for "+pair+" at "+watchList[pair]+" has triggered"
            messagebox.showinfo("Price alert", message)
            break

    x = 15
    if watchList != {}:
        for pair in watchList:
            currText = pair + " @ " + str(watchList[pair])
            title = Label(root, text=currText).grid(row=x, column=0)
            x += 1

        
    root.after(1500, checkNotifier)

    
root = Tk()
root.title("Forex Price Alerts")

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

radio = StringVar()

EU = Radiobutton(mainframe, text = "EUR/USD", value = 1, variable = radio).pack()
UJ = Radiobutton(mainframe, text = "USD/JPY  ", value = 2, variable = radio).pack()
GU = Radiobutton(mainframe, text = "GBP/USD", value = 3, variable = radio).pack()
EG = Radiobutton(mainframe, text = "EUR/GBP", value = 4, variable = radio).pack()
UF = Radiobutton(mainframe, text = "USD/CHF", value = 5, variable = radio).pack()
EJ = Radiobutton(mainframe, text = "EUR/JPY  ", value = 6, variable = radio).pack()
EC = Radiobutton(mainframe, text = "EUR/CHF", value = 7, variable = radio).pack()
UC = Radiobutton(mainframe, text = "USD/CAD", value = 8, variable = radio).pack()
AU = Radiobutton(mainframe, text = "AUD/USD", value = 9, variable = radio).pack()
GJ = Radiobutton(mainframe, text = "GBP/JPY  ", value = 10, variable = radio).pack()

watchPrice = Entry(root)
watchPrice.grid(row=11, column=0)

addButton = Button(text = "Set", command = onClick).grid(row=12, column=0)
space = Label(root, text=" ").grid(row=13, column=0)
title = Label(root, text="Current Alerts").grid(row=14, column=0)

root.protocol("WM_DELETE_WINDOW", sys.exit)
root.after(1500, checkNotifier)
root.mainloop()




