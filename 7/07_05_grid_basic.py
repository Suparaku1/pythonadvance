import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Basic Grid")
root.geometry("650x350")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Emri:").grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5,
)

name_entry = ttk.Entry(frame)
name_entry.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=5,
    pady=5,
)

ttk.Label(frame, text="Mbiemri:").grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=5,
)

surname_entry = ttk.Entry(frame)
surname_entry.grid(
    row=1,
    column=1,
    sticky="ew",
    padx=5,
    pady=5,
)

# One widget spanning two columns.
ttk.Button(
    frame,
    text="Dërgo",
).grid(
    row=2,
    column=0,
    columnspan=2,
    pady=15,
)

# The second column receives extra horizontal space.
frame.columnconfigure(1, weight=1)

# The frame itself expands with the window.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
