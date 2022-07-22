#Mini Time project -  Sparsh Arya 22-07-2022

from tkinter import * # Standard GUI Library
from tkinter.ttk import * # Override GUI Objects in Tkinter, in this case label

from time import strftime

root = Tk() # Create a new Window or Tkinter instance
root.title("Clock") # Title for the new Window

def time(): # Creating a call function
    string = strftime('%H:%M:%S %p') # string contains time in the format mentioned in brackets 
    label.config(text=string) # Data element of label changes with change in string value
    label.after(1000, time) # Call the time function after every 1 sec or 1000 mili sec

label = Label(root, font = ("times", 90), background="black", foreground="yellow") # Label styling
label.pack(anchor="center") # Label Align center

time() # Call time function

mainloop() #Event loop