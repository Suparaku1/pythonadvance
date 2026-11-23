import tkinter as tk


class GuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Science 2 - GUI Part 1")
        self.root.geometry("750x650")

        # Variablat Tkinter.
        self.name_var = tk.StringVar()
        self.accepted_var = tk.BooleanVar(value=False)
        self.language_var = tk.StringVar(value="Python")

        # Titulli.
        tk.Label(
            root,
            text="Tkinter GUI - Part 1",
            font=("Arial", 22),
        ).pack(pady=15)

        # Entry.
        tk.Label(root, text="Emri:").pack()
        tk.Entry(
            root,
            textvariable=self.name_var,
            width=40,
        ).pack(pady=5)

        # Checkbutton.
        tk.Checkbutton(
            root,
            text="E pranoj",
            variable=self.accepted_var,
        ).pack(pady=5)

        # Radiobuttons.
        tk.Label(root, text="Gjuha:").pack()

        for language in ("Python", "Java", "C++"):
            tk.Radiobutton(
                root,
                text=language,
                value=language,
                variable=self.language_var,
            ).pack()

        # Buton.
        tk.Button(
            root,
            text="Shfaq të dhënat",
            command=self.show_data,
        ).pack(pady=15)

        # Rezultati.
        self.result = tk.Label(
            root,
            text="",
            justify="left",
            anchor="w",
        )
        self.result.pack(fill="x", padx=20)

        # Text multi-line.
        tk.Label(root, text="Shënime:").pack(pady=(15, 0))

        self.text = tk.Text(root, height=8, wrap=tk.WORD)
        self.text.pack(fill="both", expand=True, padx=20, pady=5)

    def show_data(self):
        notes = self.text.get("1.0", tk.END).strip()

        message = (
            f"Emri: {self.name_var.get()}\n"
            f"E pranon: {self.accepted_var.get()}\n"
            f"Gjuha: {self.language_var.get()}\n"
            f"Shënime: {notes}"
        )

        self.result.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = GuiApp(root)
    root.mainloop()
