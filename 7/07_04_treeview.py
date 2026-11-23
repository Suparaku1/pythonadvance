import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Treeview")
root.geometry("700x450")

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

columns = ("emri", "modeli", "viti")

tree = ttk.Treeview(
    frame,
    columns=columns,
    show="headings",
)

tree.heading("emri", text="Emri")
tree.heading("modeli", text="Modeli")
tree.heading("viti", text="Viti")

tree.column("emri", width=220)
tree.column("modeli", width=220)
tree.column("viti", width=100)

tree.insert("", "end", values=("VW", "Golf", 2020))
tree.insert("", "end", values=("BMW", "320i", 2021))
tree.insert("", "end", values=("Audi", "A4", 2022))

tree.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(
    frame,
    orient="vertical",
    command=tree.yview,
)
scrollbar.pack(side="right", fill="y")

tree.configure(yscrollcommand=scrollbar.set)

root.mainloop()
