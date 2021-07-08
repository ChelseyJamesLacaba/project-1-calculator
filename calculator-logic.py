# Calculator Logic

#--------------------------------------- FUNCTIONS ---------------------------------------

class Calculator:
    def __init__(self, input_text):
        self.input_text = input_text

    def about(self):
        messagebox.showinfo('About'," \n CALCULATOR \n Created by NOT A PRO CODERS")

    def click_button(self, item):                                           # the 'click_button' function updates the input field constantly when you enter a number
        global expression
        input_text.set(input_text.get()+(str(item)))

    def clear_button(self):                                               # the 'clear_button' function removes the final item from the input list
        global expression
        expression = " "
        input_text.set(input_text.get()[0:-1]                      
