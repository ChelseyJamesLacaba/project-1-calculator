# Calculator's code with the LOGIC & UI

from tkinter import *
from tkinter import messagebox

calc = Tk()                         # Making the basic window
calc.geometry("312x394+300+100")    # The window's side width: 312, height: 394 & The window's positioning 300 pixels from the right, 100 pixels down
calc.resizable(0, 0)                # This prevents the window from resizing
calc.title("Calculator")            # Name of the window

#needed for declaring Calculator() as an argument
input_text = ""

#--------------------------------------- FUNCTIONS ---------------------------------------
class Calculator:
    def __init__(self, input_text):
        self.input_text = input_text

    def about(self):
        messagebox.showinfo('About'," \n CALCULATOR \n Created by NOT A PRO CODERS")

    def click_button(self, item):                                         # the 'click_button' function updates the input field constantly when you enter a number
        global expression
        input_text.set(input_text.get()+(str(item)))

    def clear_button(self):                                               # the 'clear_button' function removes the final item from the input list
        global expression
        expression = " "
        input_text.set(input_text.get()[0:-1])

    def clear_all(self):                                                  # the 'clear_all' function removes all the item in the input field
        input_text.set(" ")

    def equal_button(self):

        result = " "
        try:
            result = eval(input_text.get())                               # 'eval' function dynamically evalutes the string expression
            input_text.set(result)
            return result
        except:
            result = "ERROR"
            input_text.set(result)
            return result

c = Calculator(input_text)

#--------------------------------------- MENUBAR ---------------------------------------
# the 'menubar' serves as an identification of the coders
# this function can be seen at the 'help' button in the UI

menu_bar = Menu(calc,bg="black",fg="white")

help_menu = Menu(menu_bar, tearoff=0,bg="black",fg="white")
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=c.about)

calc.config(bg="grey",menu=menu_bar)  

#--------------------------------------- FRAME ---------------------------------------

expression = ""
input_text = StringVar()                     # 'StringVar()' is used to get the instance of input field

#Input Frame
input_frame = Frame(calc, width=312, height=50, bd=0, highlightbackground="#121212", highlightcolor="crimson", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18), textvariable=input_text, width=50,fg="white", bg="#121212", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=19)

#Button Frame
button_frame = Frame(calc, width=312, height=272.5, bg="grey")
button_frame.pack()

#--------------------------------------- BUTTONS ---------------------------------------
# First_row
clearall = Button(button_frame, text = "AC", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: c.clear_all()).grid(row = 1, column = 0, padx = 1, pady = 1)
l_bracket= Button(button_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: c.click_button("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
r_bracket = Button(button_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: c.click_button(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(button_frame, text = "DEL", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: c.clear_button()).grid(row = 1, column = 3, padx = 1, pady = 1)

# Second_row
# With the Additional Functions
# For 'pie' and 'sqrt', integer must be inputted first before the function itself
power = Button(button_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: c.click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie = Button(button_frame, text = "??", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: c.click_button( "*(3.1415)")).grid(row = 2, column = 1, padx = 1, pady = 1)
sqrt = Button(button_frame, text = "???", fg = "black", width = 10, height = 3, bd = 0, bg = "gray70", cursor = "hand2", command = lambda: c.click_button("**0.5")).grid(row = 2, column = 2, padx = 1, pady = 1)
divide_= Button(button_frame, text = "??", fg = "black", width = 10, height = 3, bd = 0, bg = "orange2", cursor = "hand2", command = lambda: c.click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

#Third_row
seven = Button(button_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "orange2", cursor = "hand2", command = lambda: c.click_button("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

#Fourth_row
four = Button(button_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "orange2", cursor = "hand2", command = lambda: c.click_button("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

#Fifth_row
one = Button(button_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "orange2", cursor = "hand2", command = lambda: c.click_button("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

#Sixth_row
point = Button(button_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: c.click_button(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
zero = Button(button_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", cursor = "hand2", command = lambda: c.click_button(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "white", width = 21, height = 3, bd = 0, bg = "gray25", cursor = "hand2", command = lambda: c.equal_button()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)
 
calc.mainloop()                       #mainloop() is an infinite loop used to run the application
