import tkinter as tk
from tkinter import ttk
from pages.main_page import show_page
import main.theme as theme
from main import session
from main.database import get_user_information

def show_profile_page(root, mode_button_text):
    from login.login_page import show_login_screen

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    tk.Label(root, text="User Profile", font=("Segoe UI", 18, "bold"),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(pady=20)

    email = session.get_logged_in_user()
    user_data_list = get_user_information(email)

    if not user_data_list:
        tk.Label(root, text="User data not found.", font=("Segoe UI", 12), fg="red", bg=theme.current_theme["bg"]).pack(pady=20)
        return

    user = user_data_list[0]

    details = {
        "Name": f"{user.get('First Name', '')} {user.get('Last Name', '')}",
        "Email": user.get('User Email', ''),
        "Phone": user.get('Phone', 'N/A')
    }

    for key, value in details.items():
        tk.Label(root, text=f"{key}: {value}", font=("Segoe UI", 12),
                 fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", padx=40, pady=5)
    
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    # Buton de schimbare mod lumină/întuneric
    ttk.Button(
    bottom_frame,
    text="☀️ Light Mode" if theme.current_theme == theme.dark_theme else "🌕 Dark Mode",
    command=lambda: theme.toggle_theme(
        root,
        lambda r: show_profile_page(r, mode_button_text),
        mode_button_text
    ),
    style="Dark.TButton"
    ).pack(side=tk.RIGHT, padx=5)

    ttk.Button(bottom_frame, text="⬅️ Back",
           command=lambda: show_page(root, mode_button_text),
           style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    
    ttk.Button(bottom_frame, text="❌ Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)


