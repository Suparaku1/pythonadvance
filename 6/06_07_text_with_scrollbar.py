import tkinter as tk

root = tk.Tk()
root.geometry("700x450")
root.title("GUI - Text + Scrollbar")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

text = tk.Text(frame, wrap=tk.WORD)
scrollbar = tk.Scrollbar(frame, command=text.yview)

# Text dhe scrollbar komunikojnë në të dyja drejtimet.
text.configure(yscrollcommand=scrollbar.set)

text.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

text.insert(
    "1.0",
    "Ky është një shembull me shumë rreshta.\n" * 30
)

root.mainloop()
