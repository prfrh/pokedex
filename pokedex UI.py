from tkinter import *
import tkinter as tk



usernamestored = 'rh'
userpasswordstored = 'pokedex'

def login():
    while True:
        user = input("Enter a username. ")
        password = input("Enter a password. ")
        if user == usernamestored and password == userpasswordstored:
            print ("Welcome RH...")
            break
        else:
            print ("Incorrect login, try again.")
            
        




window = tk.Tk()
window.title('Pokedex login')

menulabel = Tk()
Label(window, text='user name').grid(row=0)
Label(window, text='password').grid(row=1)
menulabel.geometry("10x50")
background="grey"
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)



top = Toplevel()
top.geometry("200x100")
top.title("Pokedex")
l2 = Label(top, text = "Welcome rh")
l2.pack()

# label = tk.Label(
#     text="Hello, Tkinter",
#     foreground="black",  # Set the text color to white
#     background="grey",  # Set the background color to black
#     width=75, 
#     height=50,
# )
# label.pack()

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

