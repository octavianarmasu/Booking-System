import tkinter as tk
from tkinter import ttk
from main import theme
from pages.main_page import show_page
import pages.italy as italy
import pages.portugal as portugal
import pages.greece as greece


def show_reservation_page(root, mode_button_text, hotel_id):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    # Title
    title = tk.Label(
        root,
        text="Completează detalii pentru rezervare",
        font=("Segoe UI", 26, "bold"),
        fg=theme.current_theme["fg"],  # ← aici e modificarea
        bg=theme.current_theme["bg"]
    )

    title.pack(pady=40)

    # Buttons
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    mode_button_text.set("☀️ Light Mode" if theme.current_theme == theme.dark_theme else "🌕 Dark Mode")
    ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: theme.toggle_theme(
            root, lambda r: show_reservation_page(r, mode_button_text, hotel_id), mode_button_text
        ),
        style="Dark.TButton"
    ).pack(side=tk.RIGHT, padx=5)

    # Back button logic
    def go_back():
        if hotel_id == 2:
            italy.show_country_page(root, mode_button_text)
        elif hotel_id == 3:
            portugal.show_country_page(root, mode_button_text)
        elif hotel_id == 4:
            greece.show_country_page(root, mode_button_text)
        else:
            show_page(root, mode_button_text)


    ttk.Button(
        bottom_frame,
        text="⬅️ Back",
        command=go_back,
        style="Dark.TButton"
    ).pack(side=tk.RIGHT, padx=5)

    # Exit
    ttk.Button(
        bottom_frame,
        text="❌ Exit",
        command=root.destroy,
        style="Dark.TButton"
    ).pack(side=tk.RIGHT, padx=5)
