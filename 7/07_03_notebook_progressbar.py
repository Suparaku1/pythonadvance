import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Notebook and Progressbar")
root.geometry("650x420")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=15, pady=15)

page1 = ttk.Frame(notebook, padding=20)
page2 = ttk.Frame(notebook, padding=20)

notebook.add(page1, text="Faqja 1")
notebook.add(page2, text="Faqja 2")

ttk.Label(
    page1,
    text="Notebook lejon disa faqe në të njëjtën dritare.",
).pack(pady=20)

progress = ttk.Progressbar(
    page2,
    orient="horizontal",
    length=400,
    mode="determinate",
    maximum=100,
)
progress.pack(pady=20)


def start_progress():
    progress["value"] = 0
    step()


def step():
    current = progress["value"]

    if current < 100:
        progress["value"] = current + 5
        root.after(100, step)


ttk.Button(
    page2,
    text="Fillo progresin",
    command=start_progress,
).pack()

root.mainloop()
