import tkinter as tk




usernamestored = 'rh'
userpasswordstored = 'Pokedex123!'

def login():
    while True:
        user = input("Enter a username. ")
        password = input("Enter a password. ")
        if user == usernamestored and password == userpasswordstored:
            print ("Welcome RH...")
        else:
            print ("Incorrect login, try again.")

    






window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="black",  # Set the text color to white
    background="grey",  # Set the background color to black
    width=75, 
    height=50,
)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="orange",
)
button.pack()


window.mainloop()
