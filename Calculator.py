import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, padx=20, pady=10,
                               command=lambda t=text: self.handle_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def handle_click(self, value):
        current = self.entry.get()
        if value == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

master = tk.Tk()
app = CalculatorApp(master)
master.mainloop()
