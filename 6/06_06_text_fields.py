import tkinter as tk

root = tk.Tk()
root.geometry("700x500")
root.title("GUI - Text Fields")


# ---------------- ENTRY: një rresht ----------------

name_var = tk.StringVar()

tk.Label(root, text="Emri:").pack(pady=(10, 0))

name_entry = tk.Entry(root, textvariable=name_var, width=40)
name_entry.pack(pady=5)


def read_entry():
    result_label.config(text=f"Emri: {name_var.get()}")


tk.Button(root, text="Lexo Emrin", command=read_entry).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)


# ---------------- TEXT: disa rreshta ----------------

tk.Label(root, text="Komenti:").pack(pady=(15, 0))

comment_text = tk.Text(root, width=60, height=8, wrap=tk.WORD)
comment_text.pack(pady=5)

# Fusim tekst fillestar.
comment_text.insert("1.0", "Shkruaj komentin këtu...")


def read_text():
    content = comment_text.get("1.0", tk.END)
    output_label.config(text=content.strip())


tk.Button(root, text="Lexo Komentin", command=read_text).pack(pady=5)

output_label = tk.Label(root, text="", justify="left", anchor="w")
output_label.pack(pady=5, fill="x")

root.mainloop()
