import tkinter as tk
from tkinter import ttk, messagebox

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

def show_login_screen(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    from login.register_page import show_register_screen

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TLabel", background=current_theme["bg"], foreground=current_theme["fg"], font=("Segoe UI", 13))
    style.configure("TEntry", font=("Segoe UI", 13))
    style.configure("TButton", font=("Segoe UI", 14), padding=12)
    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)

    root.configure(bg=current_theme["bg"])
    frame = tk.Frame(root, bg=current_theme["bg"])
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Welcome to Our Hotel", font=("Segoe UI", 28, "bold"),
                     fg=current_theme["accent"], bg=current_theme["bg"])
    title.pack(pady=(80, 10))

    subtitle = tk.Label(frame, text="Please login or create an account",
                        font=("Segoe UI", 16), bg=current_theme["bg"], fg=current_theme["fg"])
    subtitle.pack(pady=(0, 40))

    login_btn = ttk.Button(frame, text="Login", command=lambda: login_form(root, mode_button_text))
    register_btn = ttk.Button(frame, text="Create Account", command=lambda: show_register_screen(root, mode_button_text))

    login_btn.pack(pady=15, ipadx=20)
    register_btn.pack(pady=5, ipadx=20)

    mode_button_text.set("Light Mode" if current_theme == dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        root,
        textvariable=mode_button_text,
        command=lambda: toggle_theme(root, lambda r: show_login_screen(r, mode_button_text))
    )
    dark_btn.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    dark_btn.configure(style="Dark.TButton")

def login_form(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    from login.login_page import show_login_screen

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TLabel", background=current_theme["bg"], foreground=current_theme["fg"], font=("Segoe UI", 13))
    style.configure("TButton", font=("Segoe UI", 14), padding=12)

    # Entry styling based on theme
    entry_style_name = "Dark.TEntry" if current_theme == dark_theme else "Light.TEntry"
    style.configure(entry_style_name,
        foreground=current_theme["entry_fg"],
        fieldbackground=current_theme["entry_bg"],
        background=current_theme["entry_bg"],
        font=("Segoe UI", 13)
    )

    root.configure(bg=current_theme["bg"])
    frame = tk.Frame(root, bg=current_theme["bg"])
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Login", font=("Segoe UI", 26, "bold"),
                     fg=current_theme["accent"], bg=current_theme["bg"])
    title.pack(pady=(60, 30))

    form_frame = tk.Frame(frame, bg=current_theme["bg"])
    form_frame.pack(pady=20)

    ttk.Label(form_frame, text="Email:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    email_entry = ttk.Entry(form_frame, width=40, style=entry_style_name)
    email_entry.grid(row=0, column=1, pady=10)

    ttk.Label(form_frame, text="Password:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    # Password Entry + Show Password Toggle
    password_var = tk.StringVar()
    show_password = tk.BooleanVar(value=False)

    password_entry = ttk.Entry(form_frame, textvariable=password_var, show="*", width=40, style=entry_style_name)
    password_entry.grid(row=1, column=1, pady=10)

    def toggle_password():
        password_entry.config(show="" if show_password.get() else "*")

    check_btn = tk.Checkbutton(
        form_frame,
        text="Show Password",
        variable=show_password,
        command=toggle_password,
        bg=current_theme["bg"],
        fg=current_theme["fg"],
        activebackground=current_theme["bg"],
        activeforeground=current_theme["fg"],
        font=("Segoe UI", 10),
        bd=0,
        highlightthickness=0,
        selectcolor=current_theme["bg"]
    )

    check_btn.grid(row=2, column=1, sticky="w", padx=4)

    def handle_login():
        email = email_entry.get()
        password = password_var.get()
        print(f"Login attempted with email: {email}, password: {password}")

    button_frame = tk.Frame(frame, bg=current_theme["bg"])
    button_frame.pack(pady=40)

    ttk.Button(button_frame, text="Submit", command=handle_login).pack(pady=10, ipadx=15)
    ttk.Button(button_frame, text="Back", command=lambda: show_login_screen(root, mode_button_text)).pack(pady=5, ipadx=15)

    mode_button_text.set("Light Mode" if current_theme == dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        root,
        textvariable=mode_button_text,
        command=lambda: toggle_theme(root, lambda r: login_form(r, mode_button_text))
    )
    dark_btn.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)
    dark_btn.configure(style="Dark.TButton")
