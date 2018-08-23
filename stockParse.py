from tkinter import *
from tkinter import ttk
import requests
import time
from bs4 import BeautifulSoup

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


watchList = {}
def onClick():

    pairing = radio.get()

    if (pairing == 1):

    else if (pairing == 2):

    else if (pairing == 3):

    else if (pairing == 4):

    else if (pairing == 5):

    else if (pairing == 6):

    else if (pairing == 7):

    else if (pairing == 8):

    else if (pairing == 9):

    else if (pairing == 10):
    
root = Tk()
root.title("blah")

mainframe = ttk.Frame(root, padding="3 3 12 12")
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
EC = Radiobutton(mainframe, text = "EUR/CAD", value = 7, variable = radio).pack()
UC = Radiobutton(mainframe, text = "USD/CAD", value = 8, variable = radio).pack()
AU = Radiobutton(mainframe, text = "AUD/USD", value = 9, variable = radio).pack()
GJ = Radiobutton(mainframe, text = "GBP/JPY  ", value = 10, variable = radio).pack()

watchPrice = Entry(root)
watchPrice.grid(row=11, column=0)

addButton = Button(text = "Set", command = onClick).grid(row=12, column=0)


root.mainloop()




