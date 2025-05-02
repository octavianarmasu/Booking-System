import tkinter as tk
from tkinter import ttk, messagebox
import re
from main.database import add_user

# Theme settings
light_theme = {
    "bg": "white", "fg": "black", "accent": "#28a745",
    "entry_bg": "white", "entry_fg": "black"
}

dark_theme = {
    "bg": "#1c1c1c", "fg": "#f5f5f5", "accent": "#00ff88",
    "entry_bg": "#2e2e2e", "entry_fg": "white"
}

current_theme = light_theme.copy()

def toggle_theme(root, refresh_screen):
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme
    refresh_screen(root)

def show_register_screen(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    from login.login_page import show_login_screen

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TLabel", background=current_theme["bg"], foreground=current_theme["fg"], font=("Segoe UI", 13))
    style.configure("TEntry", font=("Segoe UI", 13))
    style.configure("TButton", font=("Segoe UI", 14), padding=12)
    style.configure("Dark.TButton", font=("Segoe UI", 10), padding=4)

    root.configure(bg=current_theme["bg"])
    frame = tk.Frame(root, bg=current_theme["bg"])
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Create Account", font=("Segoe UI", 28, "bold"),
                     fg=current_theme["accent"], bg=current_theme["bg"])
    title.pack(pady=(60, 40))

    form_frame = tk.Frame(frame, bg=current_theme["bg"])
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

    # Password strength meter in the same column as password
    strength_label = ttk.Label(form_frame, text="Password Strength: ", background=current_theme["bg"], foreground=current_theme["fg"])
    strength_label.grid(row=len(labels), column=0, sticky="w", padx=15, pady=10)

    strength_meter = ttk.Progressbar(form_frame, length=200, mode='determinate', maximum=100)
    strength_meter.grid(row=len(labels), column=1, pady=10)

    def check_password_strength(password):
        """Check the strength of the password."""
        strength = 0
        if len(password) >= 8:
            strength += 25
        if re.search(r"[A-Z]", password):  # At least one uppercase letter
            strength += 25
        if re.search(r"[a-z]", password):  # At least one lowercase letter
            strength += 25
        if re.search(r"[0-9]", password):  # At least one number
            strength += 15
        if re.search(r"[\W_]", password):  # At least one special character
            strength += 10
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

    # Bind password field to update strength meter
    password_vars["Password"][1].trace_add("write", on_password_change)

    # Show Password checkbox
    show_pw = tk.BooleanVar(value=False)

    def toggle_password_visibility():
        for entry, _ in password_vars.values():
            entry.config(show="" if show_pw.get() else "*")

    check_btn = tk.Checkbutton(
        form_frame, text="Show Password", variable=show_pw, command=toggle_password_visibility,
        bg=current_theme["bg"], fg=current_theme["fg"],
        activebackground=current_theme["bg"], activeforeground=current_theme["fg"],
        font=("Segoe UI", 10),
        bd=0,
        highlightthickness=0,
        selectcolor=current_theme["bg"]
    )
    check_btn.grid(row=len(labels) + 1, column=1, sticky="w", padx=4)

    def handle_register():
        values = {label: entry.get() for label, entry in entries.items()}

        # Check if all fields are filled
        for label, value in values.items():
            if not value:  # If any field is empty
                messagebox.showerror("Error", f"{label} cannot be empty.")
                return

        # Check if passwords match
        if values["Password"] != values["Confirm Password"]:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Check if password is strong enough
        if strength_meter['value'] < 50:
            messagebox.showerror("Error", "Password is too weak")
            return

        # If all conditions are met
        email = values["Email"]
        first_name = values["First Name"]
        last_name = values["Last Name"]
        phone = values["Phone"]
        password = values["Password"]
        if add_user(email, first_name, last_name, phone, password) == 0:
            messagebox.showinfo("Success", "Account created successfully!")
            show_login_screen(root, mode_button_text)
        else:
            messagebox.showerror("Error", "Email already exists or invalid data.")
            return

    button_frame = tk.Frame(frame, bg=current_theme["bg"])
    button_frame.pack(pady=40)

    ttk.Button(button_frame, text="Register", command=handle_register).pack(pady=10, ipadx=15)
    ttk.Button(button_frame, text="Back", command=lambda: show_login_screen(root, mode_button_text)).pack(pady=5, ipadx=15)

    # Bottom right buttons frame
    bottom_frame = tk.Frame(root, bg=current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("Light Mode" if current_theme == dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: toggle_theme(root, lambda r: show_register_screen(r, mode_button_text))
    )
    dark_btn.pack(side=tk.RIGHT, padx=5)
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
