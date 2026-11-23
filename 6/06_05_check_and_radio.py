import tkinter as tk

root = tk.Tk()
root.geometry("500x350")
root.title("GUI - Check Buttons and Radio Buttons")


# ---------------- CHECKBUTTON ----------------

accepted = tk.BooleanVar(value=False)


def checkbox_changed():
    if accepted.get():
        check_status.config(text="Zgjedhur")
    else:
        check_status.config(text="Pa zgjedhur")


check_status = tk.Label(root, text="Pa zgjedhur")
check_status.pack(pady=5)

check = tk.Checkbutton(
    root,
    text="E pranoj",
    variable=accepted,
    command=checkbox_changed,
)
check.pack(pady=5)


# ---------------- RADIOBUTTON ----------------

choice = tk.StringVar(value="Asnjë")


def radio_changed():
    radio_status.config(text=f"Zgjedhja: {choice.get()}")


radio_status = tk.Label(root, text="Zgjedhja: Asnjë")
radio_status.pack(pady=10)

tk.Radiobutton(
    root,
    text="Python",
    value="Python",
    variable=choice,
    command=radio_changed,
).pack()

tk.Radiobutton(
    root,
    text="Java",
    value="Java",
    variable=choice,
    command=radio_changed,
).pack()

tk.Radiobutton(
    root,
    text="C++",
    value="C++",
    variable=choice,
    command=radio_changed,
).pack()

root.mainloop()
