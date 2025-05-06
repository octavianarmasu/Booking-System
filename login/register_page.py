import tkinter as tk
from tkinter import ttk, messagebox
import re
from main.database import add_user
import main.theme as theme

def show_register_screen(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    from login.login_page import show_login_screen

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TLabel", background=theme.current_theme["bg"], foreground=theme.current_theme["fg"], font=("Segoe UI", 13))
    style.configure("TEntry", font=("Segoe UI", 13))
    style.configure("TButton", font=("Segoe UI", 14), padding=12)
    style.configure("Dark.TButton", font=("Segoe UI", 10), padding=4)

    root.configure(bg=theme.current_theme["bg"])
    frame = tk.Frame(root, bg=theme.current_theme["bg"])
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Create Account", font=("Segoe UI", 28, "bold"),
                     fg=theme.current_theme["accent"], bg=theme.current_theme["bg"])
    title.pack(pady=(60, 40))

    form_frame = tk.Frame(frame, bg=theme.current_theme["bg"])
    form_frame.pack()

    labels = ["First Name", "Last Name", "Email", "Phone", "Password", "Confirm Password"]
    entries = {}
    password_vars = {}

    for i, label in enumerate(labels):
        ttk.Label(form_frame, text=label + ":").grid(row=i, column=0, sticky="w", padx=15, pady=12)
        is_password = "Password" in label
        var = tk.StringVar()
        entry = ttk.Entry(form_frame, width=40, show="*" if is_password else "", textvariable=var)
        entry.grid(row=i, column=1, pady=12)
        entries[label] = entry
        if is_password:
            password_vars[label] = (entry, var)

    strength_label = ttk.Label(form_frame, text="Password Strength: ",
                               background=theme.current_theme["bg"], foreground=theme.current_theme["fg"])
    strength_label.grid(row=len(labels), column=0, sticky="w", padx=15, pady=10)

    strength_meter = ttk.Progressbar(form_frame, length=200, mode='determinate', maximum=100)
    strength_meter.grid(row=len(labels), column=1, pady=10)

    def check_password_strength(password):
        strength = 0
        if len(password) >= 8: strength += 25
        if re.search(r"[A-Z]", password): strength += 25
        if re.search(r"[a-z]", password): strength += 25
        if re.search(r"[0-9]", password): strength += 15
        if re.search(r"[\W_]", password): strength += 10
        return strength

    def on_password_change(*args):
        password = password_vars["Password"][1].get()
        strength = check_password_strength(password)
        strength_meter['value'] = strength
        if strength < 50:
            strength_label.config(text="Password Strength: Weak", foreground="red")
        elif strength < 75:
            strength_label.config(text="Password Strength: Medium", foreground="orange")
        else:
            strength_label.config(text="Password Strength: Strong", foreground="green")

    password_vars["Password"][1].trace_add("write", on_password_change)

    show_pw = tk.BooleanVar(value=False)

    def validate_phone(event=None):
        phone_error_label = tk.Label(form_frame, text="", fg="red", bg=theme.current_theme["bg"], font=("Segoe UI", 10))
        phone_error_label.grid(row=labels.index("Phone"), column=2, padx=10, sticky="w")
        phone = entries["Phone"].get()
        if not phone.isdigit() or len(phone) != 10:
            phone_error_label.config(text="Phone must be 10 digits")
        else:
            phone_error_label.config(text="")

    def toggle_password_visibility():
        for entry, _ in password_vars.values():
            entry.config(show="" if show_pw.get() else "*")

    check_btn = tk.Checkbutton(
        form_frame, text="Show Password", variable=show_pw, command=toggle_password_visibility,
        bg=theme.current_theme["bg"], fg=theme.current_theme["fg"],
        activebackground=theme.current_theme["bg"], activeforeground=theme.current_theme["fg"],
        font=("Segoe UI", 10), bd=0, highlightthickness=0, selectcolor=theme.current_theme["bg"]
    )
    check_btn.grid(row=len(labels) + 1, column=1, sticky="w", padx=4)

    def handle_register():
        values = {label: entry.get() for label, entry in entries.items()}
        if any(not value for value in values.values()):
            messagebox.showerror("Error", "All fields must be filled.")
            return
        if values["Password"] != values["Confirm Password"]:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        if strength_meter['value'] < 50:
            messagebox.showerror("Error", "Password is too weak.")
            return

        email = values["Email"]
        if "@" not in email or "." not in email.split("@")[-1]:
            messagebox.showerror("Error", "Invalid email address.")
            return
        first = values["First Name"]
        last = values["Last Name"]
        phone = values["Phone"]
        if not phone.isdigit() :
            messagebox.showerror("Error", "Invalid phone number.")
            return
        if len(phone) != 10:
            messagebox.showerror("Error", "Phone number must be exactly 10 digits.")
            return
        pwd = values["Password"]
        if add_user(email, first, last, phone, pwd) == 0:
            messagebox.showinfo("Success", "Account created successfully!")
            show_login_screen(root, mode_button_text)
        else:
            messagebox.showerror("Error", "Email already exists or data is invalid.")

    button_frame = tk.Frame(frame, bg=theme.current_theme["bg"])
    button_frame.pack(pady=40)
    ttk.Button(button_frame, text="Register", command=handle_register).pack(pady=10, ipadx=15)
    ttk.Button(button_frame, text="Back", command=lambda: show_login_screen(root, mode_button_text)).pack(pady=5, ipadx=15)

    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("Light Mode" if theme.current_theme == theme.dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: theme.toggle_theme(root, lambda r: show_register_screen(r, mode_button_text), mode_button_text)
    )
    dark_btn.pack(side=tk.RIGHT, padx=5)
    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)
    dark_btn.configure(style="Dark.TButton")

    exit_btn = ttk.Button(
        bottom_frame,
        text="Exit",
        command=root.destroy,
        style="Dark.TButton"
    )
    exit_btn.pack(side=tk.RIGHT, padx=5)
