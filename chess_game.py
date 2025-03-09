import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + str(button_text))

# Create main window
root = tk.Tk()
root.title("Basic Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=10, relief=tk.GROOVE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Adjust column and row weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
