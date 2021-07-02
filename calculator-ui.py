# Calculator UI
from tkinter import *
from tkinter import messagebox

calc = Tk()                         # Making the basic window
calc.geometry("312x394+300+100")    # The window's side width: 312, height: 394 & The window's positioning 300 pixels from the right, 100 pixels down
calc.resizable(0, 0)                # This prevents the window from resizing
calc.title("Calculator")            # Name of the window

#--------------------------------------- MENUBAR ---------------------------------------
# the 'menubar' serves as an identification of the coders
# this function can be seen at the 'help' button in the UI

menu_bar = Menu(calc,bg="black",fg="white")

help_menu = Menu(menu_bar, tearoff=0,bg="black",fg="white")
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

calc.config(bg="grey",menu=menu_bar)  
