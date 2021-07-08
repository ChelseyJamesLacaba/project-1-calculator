# Calculator Logic

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
        input_text.set(input_text.get()[0:-1]                      
        
    def clear_all(self):                                                  # the 'clear_all' function removes all the item in the input field
        input_text.set(" ")

    def equal_button(self):

        result = " "
        try:
            result = eval(input_text.get())                              # 'eval' function dynamically evalutes the string expression
            input_text.set(result)
            return result
        except:
            result = "ERROR"
            input_text.set(result)
            return result

c = Calculator(input_text)
