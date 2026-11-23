import tkinter as tk

root = tk.Tk()
root.geometry("700x400")
root.title("GUI - Packer")

# side="top" është sjellja tipike.
tk.Label(root, text="TOP").pack(side="top", fill="x")

# Vendosim komponentë në skajin e majtë.
tk.Button(root, text="LEFT 1").pack(side="left", padx=10, pady=10)
tk.Button(root, text="LEFT 2").pack(side="left", padx=10, pady=10)

# Vendosim komponentë në skajin e djathtë.
tk.Button(root, text="RIGHT").pack(side="right", padx=10, pady=10)

# expand=True dhe fill="both" lejojnë widget-in të përdorë hapësirën e lirë.
tk.Label(
    root,
    text="Ky Label përdor hapësirën e lirë.",
    bg="lightgray",
).pack(
    expand=True,
    fill="both",
    padx=20,
    pady=20,
)

root.mainloop()
