import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - ttk")
root.geometry("700x450")

# ttk is the themed widget set that comes with Tkinter.
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Themed Tk Widgets", font=("Arial", 18)).pack(pady=10)

ttk.Label(frame, text="Emri:").pack(anchor="w")
ttk.Entry(frame, width=40).pack(fill="x", pady=5)

ttk.Checkbutton(frame, text="E pranoj kushtin").pack(anchor="w", pady=5)

ttk.Radiobutton(
    frame,
    text="Python",
    value="Python",
).pack(anchor="w")

ttk.Button(
    frame,
    text="OK",
    command=lambda: print("OK u klikua"),
).pack(pady=15)

# Separator: thin line between groups of widgets.
ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)

# Sizegrip is normally placed in the lower-right corner.
ttk.Sizegrip(frame).pack(anchor="se")

root.mainloop()
