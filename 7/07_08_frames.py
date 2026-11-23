import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Frames")
root.geometry("750x500")

# Main frame: controls outer padding and overall organization.
main = ttk.Frame(root, padding=15)
main.pack(fill="both", expand=True)

# LabelFrame groups widgets by topic and displays a title.
user_frame = ttk.LabelFrame(
    main,
    text="Të dhënat e përdoruesit",
    padding=10,
)
user_frame.pack(fill="x", pady=(0, 10))

ttk.Label(user_frame, text="Emri:").grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5,
)

ttk.Entry(user_frame).grid(
    row=0,
    column=1,
    sticky="ew",
    padx=5,
    pady=5,
)

user_frame.columnconfigure(1, weight=1)

# A second frame groups Text + Scrollbar as one component.
text_frame = ttk.Frame(
    main,
    padding=1,
    relief="solid",
)
text_frame.pack(fill="both", expand=True)

text_frame.columnconfigure(0, weight=1)
text_frame.rowconfigure(0, weight=1)

text = tk.Text(text_frame, wrap=tk.WORD)
text.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(
    text_frame,
    orient="vertical",
    command=text.yview,
)
scrollbar.grid(row=0, column=1, sticky="ns")

text.configure(yscrollcommand=scrollbar.set)

# Bottom frame demonstrates mixing layout managers:
# pack inside this frame, grid for the larger application structure.
button_frame = ttk.Frame(main)
button_frame.pack(fill="x", pady=(10, 0))

ttk.Button(button_frame, text="OK").pack(side="right", padx=5)
ttk.Button(button_frame, text="Cancel").pack(side="right", padx=5)

root.mainloop()
