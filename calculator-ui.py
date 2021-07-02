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
clearall = Button(button_frame, text = "AC", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: clear_all()).grid(row = 1, column = 0, padx = 1, pady = 1)
l_parenth = Button(button_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
r_parenth = Button(button_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(button_frame, text = "DEL", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: clear_button()).grid(row = 1, column = 3, padx = 1, pady = 1)

#Second_row
#With the Additional Functions
#For 'pie_func' and 'sqrt_func', input a given int first before the said two functions
power_func = Button(button_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie_func = Button(button_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button( "*(3.1415)")).grid(row = 2, column = 1, padx = 1, pady = 1)
sqrt_func = Button(button_frame, text = "√",fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: click_button("**(1/2)")).grid(row = 2, column = 2, padx = 1, pady = 1)
divide_func = Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "orange2", cursor = "hand2", command = lambda: click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)




























multiply = Button(button_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

#Fourth_row
four = Button(button_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

#Fifth_row
one = Button(button_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

#Sixth_row
point = Button(button_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
zero = Button(button_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: click_button(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "crimson", width = 21, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: equal_button()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)
 
cal.mainloop()                       #mainloop() is an infinite loop used to run the application