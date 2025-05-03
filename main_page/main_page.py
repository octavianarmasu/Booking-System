import tkinter as tk
from tkinter import ttk
from login.register_page import toggle_theme  
light_theme = {
    "bg": "white", "fg": "black", "accent": "#28a745",
    "entry_bg": "white", "entry_fg": "black"
}

dark_theme = {
    "bg": "#1c1c1c", "fg": "#f5f5f5", "accent": "#00ff88",
    "entry_bg": "#2e2e2e", "entry_fg": "white"
}

current_theme = light_theme.copy()

def show_blank_page(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=current_theme["bg"])

    # Bottom right buttons frame
    bottom_frame = tk.Frame(root, bg=current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("Light Mode" if current_theme == dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: toggle_theme(root, lambda r: show_blank_page(r, mode_button_text))
    )
    dark_btn.pack(side=tk.RIGHT, padx=5)
    style = ttk.Style()
    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)
    dark_btn.configure(style="Dark.TButton")

    # Add exit button
    exit_btn = ttk.Button(
        bottom_frame,
        text="Exit",
        command=root.destroy,
        style="Dark.TButton"
    )
    exit_btn.pack(side=tk.RIGHT, padx=5)