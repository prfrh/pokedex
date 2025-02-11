import tkinter as tk
window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10, 
    height=10,

)
label.pack()
window.mainloop()