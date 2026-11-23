import tkinter as tk
from tkinter import ttk


class GuiPart2App:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Science 2 - GUI Part 2")
        self.root.geometry("900x650")

        # The outer frame organizes the application.
        outer = ttk.Frame(root, padding=15)
        outer.grid(row=0, column=0, sticky="nsew")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        outer.columnconfigure(0, weight=1)
        outer.rowconfigure(2, weight=1)

        ttk.Label(
            outer,
            text="GUI Part 2: ttk + Grid + Frames",
            font=("Arial", 20),
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 10),
        )

        # Top controls.
        controls = ttk.LabelFrame(
            outer,
            text="Kontrollet",
            padding=10,
        )
        controls.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        controls.columnconfigure(1, weight=1)

        ttk.Label(controls, text="Gjuha:").grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5,
        )

        self.language = tk.StringVar(value="Python")

        ttk.Combobox(
            controls,
            textvariable=self.language,
            values=["Python", "Java", "C++"],
            state="readonly",
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5,
        )

        ttk.Button(
            controls,
            text="Shfaq zgjedhjen",
            command=self.show_language,
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
        )

        self.status = ttk.Label(
            controls,
            text="Gati.",
        )
        self.status.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="w",
            padx=5,
            pady=5,
        )

        # Notebook with two pages.
        self.notebook = ttk.Notebook(outer)
        self.notebook.grid(
            row=2,
            column=0,
            sticky="nsew",
        )

        table_page = ttk.Frame(self.notebook, padding=10)
        text_page = ttk.Frame(self.notebook, padding=10)

        self.notebook.add(table_page, text="Tabela")
        self.notebook.add(text_page, text="Text")

        # Treeview page.
        table_page.columnconfigure(0, weight=1)
        table_page.rowconfigure(0, weight=1)

        tree = ttk.Treeview(
            table_page,
            columns=("name", "model", "year"),
            show="headings",
        )

        tree.heading("name", text="Marka")
        tree.heading("model", text="Modeli")
        tree.heading("year", text="Viti")

        tree.column("name", width=180)
        tree.column("model", width=180)
        tree.column("year", width=100)

        for row in [
            ("VW", "Golf", 2020),
            ("BMW", "320i", 2021),
            ("Audi", "A4", 2022),
        ]:
            tree.insert("", "end", values=row)

        tree.grid(row=0, column=0, sticky="nsew")

        tree_scroll = ttk.Scrollbar(
            table_page,
            orient="vertical",
            command=tree.yview,
        )
        tree_scroll.grid(row=0, column=1, sticky="ns")

        tree.configure(yscrollcommand=tree_scroll.set)

        # Text page with a combined frame.
        text_page.columnconfigure(0, weight=1)
        text_page.rowconfigure(0, weight=1)

        text_container = ttk.Frame(
            text_page,
            padding=1,
            relief="solid",
        )
        text_container.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        text_container.columnconfigure(0, weight=1)
        text_container.rowconfigure(0, weight=1)

        text = tk.Text(text_container, wrap=tk.WORD)
        text.grid(row=0, column=0, sticky="nsew")

        text_scroll = ttk.Scrollbar(
            text_container,
            orient="vertical",
            command=text.yview,
        )
        text_scroll.grid(row=0, column=1, sticky="ns")

        text.configure(yscrollcommand=text_scroll.set)

        text.insert(
            "1.0",
            "Kjo faqe kombinon Text, Scrollbar dhe Frame.\n"
            "Ato trajtohen si një komponent i përbashkët.\n",
        )

        # Progressbar at the bottom.
        progress_frame = ttk.Frame(outer)
        progress_frame.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(10, 0),
        )

        progress_frame.columnconfigure(0, weight=1)

        self.progress = ttk.Progressbar(
            progress_frame,
            mode="determinate",
            maximum=100,
        )
        self.progress.grid(
            row=0,
            column=0,
            sticky="ew",
        )

        ttk.Button(
            progress_frame,
            text="Progresi",
            command=self.start_progress,
        ).grid(
            row=0,
            column=1,
            padx=(10, 0),
        )

        ttk.Sizegrip(root).grid(
            row=1,
            column=1,
            sticky="se",
        )

    def show_language(self):
        self.status.config(
            text=f"Gjuha e zgjedhur: {self.language.get()}"
        )

    def start_progress(self):
        self.progress["value"] = 0
        self.step_progress()

    def step_progress(self):
        value = self.progress["value"]

        if value < 100:
            self.progress["value"] = value + 4
            self.root.after(100, self.step_progress)


if __name__ == "__main__":
    root = tk.Tk()
    app = GuiPart2App(root)
    root.mainloop()
