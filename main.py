from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self):
        #_height and _width sets the wanted size of the main window
        self._height = 200
        self._width = 330
        self.main_window = Tk()
        self.build_app()
        
    
    def build_main_window(self):
        self.main_window.title("Calculator L27")
        self.main_window.geometry(str(self._width)+"x"+str(self._height))
        self.main_window.mainloop()
        

    def build_entry_field(self):
        self.entry_field = ttk.Entry(self.main_window ,background="white")
        self.entry_field.grid(row=0, column=0, columnspan=4, padx=5, pady=20, sticky=W)
        self.entry_field.bind('<Return>', self.equals())

    def add_to_entry_field(self,value):
        return self.entry_field.insert(END, value)
       
    def build_delete_button(self):
        self.delete_button = ttk.Button(self.main_window, text="C", command=lambda: self.delete_entry())
        self.delete_button.grid(row=0, column=3)

    def delete_entry(self):
        self.entry_field.delete(0, END)
        self.counter = 0
        return self.counter

    def build_buttons(self):
        #Button to close the Application
        self.quit_button = ttk.Button(self.main_window, text="Quit", command = self.main_window.destroy)
        self.quit_button.grid(padx = 4, pady = 2, row = 0, column = 4)
        self.button_list = []
        #Create the several buttons from 1 to 9 and add the created Objects to the button_list
        for i in range(0,10):
            #self.entry_field.delete(0)
            self.number = i
            if i == 1 or i == 2 or i == 3:
                self.number_button = ttk.Button(self.main_window, text = self.number)
                self.number_button.grid(padx = 4, pady=2, row = 3, column = (i))
                self.button_list.append(self.number_button)
            
            elif i == 4 or i == 5 or i == 6:
                self.number_button = ttk.Button(self.main_window, text = self.number)
                self.number_button.grid(padx = 4, pady=2, row = 2, column = (i-3))
                self.button_list.append(self.number_button)
            
            elif i == 7 or i == 8 or i == 9:
                self.number_button = ttk.Button(self.main_window, text = self.number)
                self.number_button.grid(padx = 4, pady=2, row = 1, column = (i-6))
                self.button_list.append(self.number_button)
            
            else:
                #Create the 0, point and equals button and append them to the button_list
                self.number_button = ttk.Button(self.main_window, text = self.number)
                self.point_button = ttk.Button(self.main_window, text = ".")
                self.equals_button = ttk.Button(self.main_window, text = "=")

                self.number_button.grid(padx = 4, pady=2, row = 4, column = 1)
                self.point_button.grid(padx = 4, pady=2, row = 4, column = 2)
                self.equals_button.grid(padx = 4, pady=2, row = 4, column = 3)
                
                self.button_list.append(self.number_button)
                self.button_list.append(self.point_button)
                self.button_list.append(self.equals_button)
                 
    def build_operator_buttons(self):
        #creates the different arithmetic operators
        self.plus_button = ttk.Button(self.main_window, text="+")
        self.minus_button = ttk.Button(self.main_window, text="-")
        self.multiply_button = ttk.Button(self.main_window, text="x")
        self.divide_button = ttk.Button(self.main_window, text="/")

        self.plus_button.grid(padx = 4, pady = 2, row = 1, column = 4)
        self.minus_button.grid(padx = 4, pady = 2, row = 2, column = 4)
        self.multiply_button.grid(padx = 4, pady = 2, row = 3, column = 4)
        self.divide_button.grid(padx = 4, pady = 2, row = 4, column = 4)

        self.button_list.append(self.plus_button)
        self.button_list.append(self.minus_button)
        self.button_list.append(self.multiply_button)
        self.button_list.append(self.divide_button)

        print(len(self.button_list))
    
    def button_config(self):
        self.counter = 0
        self.button_list[0].config(command=lambda: self.add_to_entry_field(0))
        self.button_list[1].config(command=lambda: self.add_to_entry_field("."))
        self.button_list[2].config(command=lambda: self.equals())
        self.button_list[3].config(command=lambda: self.add_to_entry_field(1))
        self.button_list[4].config(command=lambda: self.add_to_entry_field(2))
        self.button_list[5].config(command=lambda: self.add_to_entry_field(3))
        self.button_list[6].config(command=lambda: self.add_to_entry_field(4))
        self.button_list[7].config(command=lambda: self.add_to_entry_field(5))
        self.button_list[8].config(command=lambda: self.add_to_entry_field(6))
        self.button_list[9].config(command=lambda: self.add_to_entry_field(7))
        self.button_list[10].config(command=lambda: self.add_to_entry_field(8))
        self.button_list[11].config(command=lambda: self.add_to_entry_field(9))
        self.button_list[12].config(command=lambda: self.add_to_entry_field("+"))
        self.button_list[13].config(command=lambda: self.add_to_entry_field("-"))
        self.button_list[14].config(command=lambda: self.add_to_entry_field("x"))
        self.button_list[15].config(command=lambda: self.add_to_entry_field("/"))
    
    
    def equals(self):
        self.equation = self.entry_field.get()
        print(self.equation)
        for element in self.equation:
            if element == "+":
                equation_list = self.equation.split("+")
                self.sum = float(equation_list[0]) + float(equation_list[1])
                self.entry_field.delete(0, END)
                self.counter = 0
                self.entry_field.insert(self.counter, self.sum)
            
            elif element == "-":
                equation_list = self.equation.split("-")
                self.differ = float(equation_list[0]) - float(equation_list[1])
                self.entry_field.delete(0, END)
                self.counter = 0
                self.entry_field.insert(self.counter, self.differ)
            
            elif element == "x":
                equation_list = self.equation.split("x")
                self.product = float(equation_list[0]) * float(equation_list[1])
                self.entry_field.delete(0, END)
                self.counter = 0
                self.entry_field.insert(self.counter, self.product)
            
            elif element == "/":
                equation_list = self.equation.split("/")
                self.quotient = float(equation_list[0]) / float(equation_list[1])
                self.entry_field.delete(0, END)
                self.counter = 0
                self.entry_field.insert(self.counter, self.quotient)

    
    def build_app(self):
        self.build_entry_field()
        self.build_delete_button()
        self.build_buttons()
        self.build_operator_buttons()
        self.button_config()
        self.build_main_window()


if __name__ == "__main__":
    app = Calculator()