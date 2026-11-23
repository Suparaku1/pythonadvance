import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Grid Resize and Sticky")
root.geometry("700x450")

frame = ttk.Frame(root, padding=15)
frame.grid(row=0, column=0, sticky="nsew")

# Give rows and columns positive weights so they can grow.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

for column in range(3):
    frame.columnconfigure(column, weight=1)

frame.rowconfigure(2, weight=1)

ttk.Label(frame, text="Emri").grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5,
)

ttk.Entry(frame).grid(
    row=0,
    column=1,
    columnspan=2,
    sticky="ew",
    padx=5,
    pady=5,
)

ttk.Label(frame, text="Adresa").grid(
    row=1,
    column=0,
    sticky="nw",
    padx=5,
    pady=5,
)

address = tk.Text(frame, height=8)
address.grid(
    row=1,
    column=1,
    columnspan=2,
    rowspan=2,
    sticky="nsew",
    padx=5,
    pady=5,
)

ttk.Button(frame, text="OK").grid(
    row=3,
    column=1,
    sticky="e",
    padx=5,
    pady=10,
)

ttk.Button(frame, text="Cancel").grid(
    row=3,
    column=2,
    sticky="w",
    padx=5,
    pady=10,
)

root.mainloop()
