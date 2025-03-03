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
            break
        else:
            print ("Incorrect login, try again.")
            break
           
            
        


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

button = tk.Button(window, text="login",command=login)
button.grid(row=0, column=2)


top = Toplevel()
top.geometry("600x600")
top.title("Pokedex")
l2 = Label(top, text = "Welcome rh")
l2.pack()



# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     command=window.destroy,
#     bg="blue",
#     fg="orange",
# )
# button.pack()


window.mainloop()

