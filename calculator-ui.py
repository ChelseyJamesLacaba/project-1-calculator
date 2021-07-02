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

#--------------------------------------- FRAME ---------------------------------------

expression = ""
input_text = StringVar() # 'StringVar()' is used to get the instance of input field

# Input Frame
input_frame = Frame(calc, width=312, height=50, bd=0, highlightbackground = "#121212", highlightcolor="crimson", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18), textvariable=input_text, width=50,fg="white", bg="#121212", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=19)

#Button Frame
button_frame = Frame(calc, width=312, height=272.5, bg="grey")
button_frame.pack()

#--------------------------------------- BUTTONS ---------------------------------------

#First_row
clear_all = Button(button_frame, text = "CA", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: clear_all()).grid(row = 1, column = 0, padx = 1, pady = 1)
l_parenth = Button(button_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
r_parenth = Button(button_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(button_frame, text = "CE", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: clear_button()).grid(row = 1, column = 3, padx = 1, pady = 1)

#Second_row
#With the Additional Functions
power = Button(button_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie = Button(button_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button( "*(3.1415)")).grid(row = 2, column = 1, padx = 1, pady = 1)
sqrt = Button(button_frame, text = "√",fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button("**(1/2)")).grid(row = 2, column = 2, padx = 1, pady = 1)
divide = Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "orange2", cursor = "hand2", command = lambda: click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)









