import tkinter as tk

def button_click(symbol):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + symbol)

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for displaying numbers and results
entry_display = tk.Entry(root, width=25, font=('Arial', 12))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="C", width=5, height=2, command=clear_display).grid(row=5, column=0, padx=5, pady=5)

# Equal button
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=5, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
