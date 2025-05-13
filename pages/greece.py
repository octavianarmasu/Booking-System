def show_country_page(root, mode_button_text):
    import tkinter as tk
    from tkinter import ttk
    from main import theme
    from pages.main_page import show_page

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    tk.Label(root, text="Welcome to Greece!", font=("Segoe UI", 20),
             bg=theme.current_theme["bg"], fg=theme.current_theme["fg"]).pack(pady=40)

    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("Light Mode" if theme.current_theme == theme.dark_theme else "Dark Mode")

    ttk.Button(bottom_frame, textvariable=mode_button_text,
               command=lambda: theme.toggle_theme(root, lambda r: show_country_page(r, mode_button_text), mode_button_text),
               style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="Back", command=lambda: show_page(root, mode_button_text), style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    
