import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Part 2 - Combobox, Spinbox, Slider")
root.geometry("650x420")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Combobox: selection from predefined values.
ttk.Label(frame, text="Zgjidh gjuhën:").grid(row=0, column=0, sticky="w", pady=5)

language = tk.StringVar(value="Python")

combo = ttk.Combobox(
    frame,
    textvariable=language,
    values=["Python", "Java", "C++", "C#"],
    state="readonly",
)
combo.grid(row=0, column=1, sticky="ew", pady=5)


# Spinbox: choose a value from a numeric range.
ttk.Label(frame, text="Mosha:").grid(row=1, column=0, sticky="w", pady=5)

age = tk.IntVar(value=20)

spin = ttk.Spinbox(
    frame,
    from_=1,
    to=100,
    textvariable=age,
)
spin.grid(row=1, column=1, sticky="ew", pady=5)


# Slider: drag a handle along a track.
ttk.Label(frame, text="Volumi:").grid(row=2, column=0, sticky="w", pady=5)

volume = tk.DoubleVar(value=50)

slider = ttk.Scale(
    frame,
    from_=0,
    to=100,
    orient="horizontal",
    variable=volume,
)
slider.grid(row=2, column=1, sticky="ew", pady=5)


result = ttk.Label(frame, text="")
result.grid(row=4, column=0, columnspan=2, sticky="w", pady=20)


def show_values():
    result.config(
        text=(
            f"Gjuha: {language.get()} | "
            f"Mosha: {age.get()} | "
            f"Volumi: {volume.get():.0f}"
        )
    )


ttk.Button(
    frame,
    text="Shfaq vlerat",
    command=show_values,
).grid(row=3, column=0, columnspan=2, pady=10)

frame.columnconfigure(1, weight=1)

root.mainloop()
