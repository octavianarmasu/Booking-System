import tkinter as tk
from tkinter import ttk
import main.theme as theme
from pages.main_page import show_page

def show_profile_page(root, mode_button_text):
    from login.login_page import show_login_screen  # dacă ai nevoie de buton de logout

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    title = tk.Label(root, text="User Profile", font=("Segoe UI", 18, "bold"),
                     fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
    title.pack(pady=20)

    # Exemplu de informații despre cont
    details = {
        "Name": "Gheorghe Hagi",
        "Email": "regelefotbalului@yahoo.com",
        "Phone": "+40 728 653 214"
    }

    for key, value in details.items():
        tk.Label(root, text=f"{key}: {value}", font=("Segoe UI", 12),
                 fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", padx=40, pady=5)

    # Buton înapoi
    ttk.Button(root, text="⬅️ Back to Hotels",
               command=lambda: show_page(root, mode_button_text),
               style="Dark.TButton").pack(pady=20)
