import random
import tkinter as tk
import requests
import json
import requests
from tkinter import Frame, Toplevel
import requests
from urllib.request import urlopen
from PIL import Image, ImageTk
import io






usernamestored = 'rh'
userpasswordstored = 'pokedex'


response = requests.get("https://pokeapi.co/")
print(response.status_code)

url = "https://pokeapi.co/api/v2/pokemon/"


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
    top.rowconfigure(2, minsize=400, weight=1)
    top.columnconfigure(1, minsize=400, weight=1)
    txt_edit = tk.Entry(top)
    fr_buttons = tk.Frame(top)
    btn_search = tk.Button(fr_buttons, text="Search", command=lambda: search(txt_edit.get(), top))

    btn_search.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
    fr_buttons.grid(row=2, column=2, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")
    
        
def search(name, top):
    url = "https://pokeapi.co/api/v2/pokemon/" + name
    print(url)
    response = requests.get(url)
    data = response.json()
    print(data['name'])
    print(data['sprites']['front_default'])

    image_url = data['sprites']['front_default']
    data1 = urlopen(image_url)
    #image = tk.PhotoImage(data=data1.read())

    #label1 = tk.Label(top, image=image)
    #label1.grid(row=1, column=0)
    image_data = data1.read()
    image = Image.open(io.BytesIO(image_data))

    # Convert the image for Tkinter use
    tk_image = ImageTk.PhotoImage(image)

    # Create and display the label with the image
    label1 = tk.Label(top, image=tk_image)
    label1.grid(row=1, column=0)

    # Keep a reference to the image object to prevent it from being garbage collected
    label1.image = tk_image
    Poke_Name = (data['name'])

    tk.Label(top,
             textvariable = Poke_Name)








window = tk.Tk()

window.title('Pokedex login')
tk.Label(window, text='user name').grid(row=0)
tk.Label(window, text='password').grid(row=1)
window.geometry("250x50")
background="grey"
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

closebutton = tk.Button(window, text="close",command=window.destroy)
closebutton.grid(row=1, column=2)
logbutton = tk.Button(window, text="login",command=login)
logbutton.grid(row=0, column=2)









window.mainloop()

