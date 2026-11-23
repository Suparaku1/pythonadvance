import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Grid + Text + Scrollbar")
root.geometry("750x500")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

text = tk.Text(frame, wrap=tk.WORD)
text.grid(
    row=0,
    column=0,
    sticky="nsew",
)

vertical = ttk.Scrollbar(
    frame,
    orient="vertical",
    command=text.yview,
)
vertical.grid(
    row=0,
    column=1,
    sticky="ns",
)

text.configure(yscrollcommand=vertical.set)

horizontal = ttk.Scrollbar(
    frame,
    orient="horizontal",
    command=text.xview,
)
horizontal.grid(
    row=1,
    column=0,
    sticky="ew",
)

text.configure(xscrollcommand=horizontal.set)

text.insert(
    "1.0",
    "Ky është një Text widget i vendosur me Grid.\n" * 40
)

root.mainloop()
