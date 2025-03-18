from tkinter import *
import tkinter as tk
import requests


usernamestored = 'rh'
userpasswordstored = 'pokedex'


def login():
    while True:
        #user = input("Enter a username. ")
        user = e1.get()
        #password = input("Enter a password. ")
        password = e2.get()
        if user == usernamestored and password == userpasswordstored:
            print ("Welcome RH...")
            window.withdraw()
            main_window()
            break
        else:
            print ("Incorrect login, try again.")
            break
           


def main_window():
    top = Toplevel(window)
    top.geometry("600x600")
    top.title("Pokedex")
    txt_edit = tk.Entry(top)
    txt_edit.grid(row=0, column=1, sticky="nsew")
    top.title("Pokedex")
    top.rowconfigure(2, minsize=800, weight=1)
    top.columnconfigure(1, minsize=800, weight=1)
    txt_edit = tk.Entry(top)
    fr_buttons = tk.Frame(top)
    btn_search = tk.Button(fr_buttons, text="Search")
    btn_random = tk.Button(fr_buttons, text="Random")
    btn_search.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_random.grid(row=1, column=0, sticky="ew", padx=5)
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")
    
        


response = requests.get("https://pokeapi.co/")
print(response.status_code)

url = ("https://pokeapi.co/")



window = tk.Tk()

window.title('Pokedex login')
Label(window, text='user name').grid(row=0)
Label(window, text='password').grid(row=1)
window.geometry("250x50")
background="grey"
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

closebutton = tk.Button(window, text="close",command=window.destroy)
closebutton.grid(row=1, column=2)
logbutton = tk.Button(window, text="login",command=login)
logbutton.grid(row=0, column=2)









window.mainloop()

