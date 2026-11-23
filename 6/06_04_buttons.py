import tkinter as tk

root = tk.Tk()
root.geometry("500x350")
root.title("GUI - Buttons")


def show_message():
    status_label.config(text="Butoni u klikua!")


def change_button_text():
    action_button.config(text="Teksti u ndryshua")


def toggle_button():
    if action_button["state"] == tk.NORMAL:
        action_button.config(state=tk.DISABLED, text="I çaktivizuar")
    else:
        action_button.config(state=tk.NORMAL, text="Aktiv")


status_label = tk.Label(root, text="Kliko një buton.")
status_label.pack(pady=10)

action_button = tk.Button(
    root,
    text="Kliko",
    command=show_message,
)
action_button.pack(pady=10)

change_text_button = tk.Button(
    root,
    text="Ndrysho tekstin",
    command=change_button_text,
)
change_text_button.pack(pady=10)

disable_button = tk.Button(
    root,
    text="Çaktivizo/Aktivizo",
    command=toggle_button,
)
disable_button.pack(pady=10)

# Lambda mund të përdoret si alternativë për funksione të shkurtra.
lambda_button = tk.Button(
    root,
    text="Lambda",
    command=lambda: status_label.config(text="U ekzekutua lambda!"),
)
lambda_button.pack(pady=10)

root.mainloop()
