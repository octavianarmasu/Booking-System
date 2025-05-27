# pages/reservations.py
import tkinter as tk
from tkinter import ttk
from main import theme
from main.database import get_rezervari_for_user
from pages.main_page import show_page
from main.session import get_logged_in_user

def show_reservations_page(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg=theme.current_theme["bg"])

    email = get_logged_in_user()
    if not email:
        tk.Label(root, text="Eroare: Nu ești autentificat.",
                 fg="red", bg=theme.current_theme["bg"]).pack(pady=20)
        return

    rezervari = get_rezervari_for_user(email)

    title = tk.Label(root, text="Rezervările Mele", font=("Segoe UI", 24, "bold"),
                     fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
    title.pack(pady=20)

    if not rezervari:
        tk.Label(root, text="Nu ai rezervări efectuate.", font=("Segoe UI", 14),
                 fg="gray", bg=theme.current_theme["bg"]).pack(pady=10)
    else:
        for rez in rezervari:
            frame = tk.Frame(root, bg=theme.current_theme["bg"], highlightbackground="gray", highlightthickness=1)
            frame.pack(padx=20, pady=10, fill="x")

            for key, val in rez.items():
                tk.Label(frame, text=f"{key}: {val}", font=("Segoe UI", 12),
                         fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", padx=10, pady=2)

    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("☀️ Light Mode" if theme.current_theme == theme.dark_theme else "🌕 Dark Mode")

    ttk.Button(bottom_frame, textvariable=mode_button_text,
               command=lambda: theme.toggle_theme(root, lambda r: show_reservations_page(r, mode_button_text), mode_button_text),
               style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="⬅️ Înapoi",
               command=lambda: show_page(root, mode_button_text),
               style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="❌ Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
