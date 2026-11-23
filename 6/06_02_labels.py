import tkinter as tk

root = tk.Tk()
root.geometry("600x350")
root.title("GUI - Labels")

# Label i thjeshtë.
label1 = tk.Label(
    root,
    text="Përshëndetje nga Tkinter!",
    font=("Arial", 20),
    fg="blue",
    bg="white",
)

# pack() e vendos widget-in në dritare.
label1.pack(pady=20)

# Label tjetër për demonstrimin e anchor.
label2 = tk.Label(
    root,
    text="Ky është një Label i dytë.",
    anchor="w",
    width=40,
    bg="lightgray",
)

label2.pack(pady=10)

root.mainloop()
