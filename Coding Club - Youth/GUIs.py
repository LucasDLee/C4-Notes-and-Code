# Graphical User Interfaces (GUIs) #

# A GUI is a way to interact with visual elements such as icons and audio incdicators on our computers

# Tkinter is a GUI library that supports Python (https://tkdocs.com/pyref/index.html)

import tkinter as tk
gui = tk.Tk()
gui.title("Coding Club")

# Labels
# Ways to display important text info
greeting = tk.Label(text="hi")
greeting.pack() # put your words onto the GUI

label_colours = tk.Label(
  text="This has colours",
  foreground="white",
  background="green"
).pack()

label_size = tk.Label(
  text="My label is big",
  bg="red",
  width=20,
  height=20
).pack()

# Buttons
click_me = tk.Button(
  text="Click me!",
  bg = "yellow",
  width= 25,
  height= 5
).pack()

def say_hi():
  print("Hi")

hi_button = tk.Button(
  text="Hello there",
  bg = "pink",
  width= 25,
  height= 5,
  command=say_hi
).pack()

def quit():
  print("You left the GUI")
  gui.quit()
  # quit(): Stops the GUI from running

quit_button = tk.Button(
  text="QUIT",
  command = quit
).pack()

# Displaying messages
msg = tk.Label(text="Nothing here right now")
msg.pack()

def update_msg():
  msg.config(text="IT CHANGED")

msg_button = tk.Button(text="Change Message", command=update_msg).pack()

# User Inputs
input = tk.Entry(
  bg="green",
  fg="white"
)
input.pack()

def print_input():
  # get(): Grabs the user's input and returns it
  # e.g. entry_name.get()
  print(input.get())

submit = tk.Button(
  text="Show input",
  command=print_input
).pack()

### ACTIVITY ###
# Your goal is to make a small GUI that will take a user's input and then display it on the GUI using a label
# 1) Make a label with the text "Nothing here"
# 2) Make an entry (user input)
# 3) Create a function that can connect to the entry and then display the entry's text as the label's text
# 4) Make a button that connects to the function you made in step #3
label = tk.Label(
  text="Nothing here"
)
label.pack()

entry = tk.Entry()
entry.pack()

def show_input():
  label.config(text=entry.get())

button = tk.Button(
  text="Show Input",
  command=show_input
).pack()

gui.mainloop() # used to start the GUI