def show_country_page(root):
    import tkinter as tk
    from main.theme import current_theme
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg=current_theme["bg"])
    tk.Label(root, text="Welcome to Greece!", font=("Segoe UI", 20), bg=current_theme["bg"], fg=current_theme["fg"]).pack(pady=40)
