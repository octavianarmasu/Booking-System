import tkinter as tk
from tkinter import ttk, messagebox
from pages.main_page import show_page
import main.theme as theme
from main import session
from main.database import get_user_information, update_user_contact_info
import re
from PIL import Image, ImageTk
import urllib.request
import io


def show_profile_page(root, mode_button_text):
    from login.login_page import show_login_screen

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    tk.Label(root, text="User Profile", font=("Segoe UI", 18, "bold"),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(pady=20)
    
    def load_profile_picture(url):
        try:
            with urllib.request.urlopen(url) as u:
                raw_data = u.read()
            img = Image.open(io.BytesIO(raw_data))
            img = img.resize((256, 256))
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print("Failed to load profile picture:", e)
            return None
        
    profile_pic_url = "https://upload.wikimedia.org/wikipedia/ro/thumb/c/cb/FCSB_logo.svg/180px-FCSB_logo.svg.png"
    photo = load_profile_picture(profile_pic_url)

    if photo:
        img_label = tk.Label(root, image=photo, bg=theme.current_theme["bg"])
        img_label.image = photo  # prevent garbage collection
        img_label.pack(pady=(0, 10))


    email = session.get_logged_in_user()
    user_data_list = get_user_information(email)

    if not user_data_list:
        tk.Label(root, text="User data not found.", font=("Segoe UI", 12),
                 fg="red", bg=theme.current_theme["bg"]).pack(pady=20)
        return

    user = user_data_list[0]

    # === DISPLAY STATIC INFO ===
    info_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    info_frame.pack(anchor="w", padx=40)

    full_name = f"{user.get('First Name', '')} {user.get('Last Name', '')}"
    tk.Label(info_frame, text=f"Name: {full_name}", font=("Segoe UI", 12, "bold"),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=(0, 5))

    tk.Label(info_frame, text=f"Email: {user.get('User Email', '')}", font=("Segoe UI", 12),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=2)

    tk.Label(info_frame, text=f"Phone: {user.get('Phone', 'N/A')}", font=("Segoe UI", 12),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=2)

    # === EDIT FRAME (inițial ascuns) ===
    edit_frame = tk.Frame(root, bg=theme.current_theme["bg"])

    email_var = tk.StringVar(value=user.get('User Email', ''))
    phone_var = tk.StringVar(value=user.get('Phone', ''))

    tk.Label(edit_frame, text="New Email:", font=("Segoe UI", 12),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=(10, 0))
    tk.Entry(edit_frame, textvariable=email_var, width=40).pack(anchor="w")

    tk.Label(edit_frame, text="New Phone:", font=("Segoe UI", 12),
             fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=(10, 0))
    tk.Entry(edit_frame, textvariable=phone_var, width=40).pack(anchor="w")

    def is_valid_email(email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

    def is_valid_phone(phone):
        return re.match(r"^07\d{8}$", phone)


    def save_changes():
        new_email = email_var.get().strip()
        new_phone = phone_var.get().strip()
        old_email = user.get('User Email')

        if not is_valid_email(new_email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        if not is_valid_phone(new_phone):
            messagebox.showerror("Invalid Phone", "Please enter a valid phone number.")
            return

        if update_user_contact_info(old_email, new_email, new_phone):
            session.set_logged_in_user(new_email)
            messagebox.showinfo("Success", "Contact information updated.")
            show_profile_page(root, mode_button_text)
        else:
            messagebox.showerror("Error", "Update failed. Please try again.")


    ttk.Button(edit_frame, text="💾 Save Changes", command=save_changes, style="Dark.TButton").pack(pady=15)

    # === Buton "Edit Info" ===
    def show_edit_fields():
        edit_frame.pack(anchor="w", padx=40, pady=(10, 0))

    ttk.Button(root, text="✏️ Edit Info", command=show_edit_fields, style="Dark.TButton").pack(pady=(20, 0))

    # === Bottom buttons ===
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

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

    ttk.Button(bottom_frame, text="⬅️ Back", command=lambda: show_page(root, mode_button_text), style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="❌ Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
