# Importing the tkinter library
from tkinter import *
from sys import argv

positions = {
    "Perseverance": 77.43,
    "InSight": 135.970,
    "Curiosity": 137.42
}
landingsol = {
    "Perseverance": 52304,
    "InSight": 51511,
    "Curiosity": 49268
}

def print_missions():
    for entry in positions:
        print("\t%s" % entry)


if len(argv) != 2:
    print("Please enter the name of a mission!\nOptions:")
    print_missions()
    exit(0)

# Create an instance of tkinter frame
win = Tk()

# Define the size of the window or frame, non resizable
win.geometry("700x400")
win.resizable(0,0)
# Set position
win.geometry("+%d+%d" % (win.winfo_screenwidth()-700, win.winfo_screenheight()-400))

# Make borderless
#win.overrideredirect(True)
win.lift()
win.attributes("-topmost", True)

# Select rover
selected = False
path, rover = argv
print(rover)
win.title("%s mission clock" % rover)

# To Make it transparent use alpha property to define the opacity of the frame
win.attributes('-alpha', 0.3)
win.mainloop()
