import tkinter as tk
from math import sqrt

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("500x600")
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 30), borderwidth=5, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('Back', 4, 4)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            button = tk.Button(self, text=text, width=10, height=3, command=action, bg=self.get_button_color(text))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.memory = 0

    def get_button_color(self, text):
        if text in '0123456789':
            return "lightblue"
        elif text in '+-*/^':
            return "orange"
        elif text in ('C', 'Back'):
            return "red"
        elif text == '=':
            return "green"
        elif text == 'sqrt':
            return "lightgreen"
        else:
            return "lightgrey"

    def on_button_click(self, char):
        if char == 'C':
            self.clear_display()
        elif char == 'Back':
            self.display.delete(len(self.display.get()) - 1, tk.END)
        elif char == 'sqrt':
            self.calculate_sqrt()
        elif char == '=':
            self.calculate()
        elif char == '^':
            self.display.insert(tk.END, '**')
        else:
            self.display.insert(tk.END, char)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate_sqrt(self):
        try:
            current_value = float(self.display.get())
            result = sqrt(current_value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except (SyntaxError, ZeroDivisionError):
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
