import tkinter as tk
from tkinter import ttk, messagebox
from main.database import login_check_info
from main_page.main_page import show_blank_page
import main.theme as theme


def show_login_screen(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    from login.register_page import show_register_screen

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TLabel", background=theme.current_theme["bg"], foreground=theme.current_theme["fg"], font=("Segoe UI", 13))
    style.configure("TEntry", font=("Segoe UI", 13))
    style.configure("TButton", font=("Segoe UI", 14), padding=12)
    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)

    root.configure(bg=theme.current_theme["bg"])
    frame = tk.Frame(root, bg=theme.current_theme["bg"])
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Welcome to Our Hotel", font=("Segoe UI", 28, "bold"),
                     fg=theme.current_theme["accent"], bg=theme.current_theme["bg"])
    title.pack(pady=(80, 10))

    subtitle = tk.Label(frame, text="Please login or create an account",
                        font=("Segoe UI", 16), bg=theme.current_theme["bg"], fg=theme.current_theme["fg"])
    subtitle.pack(pady=(0, 40))

    login_btn = ttk.Button(frame, text="Login", command=lambda: login_form(root, mode_button_text))
    register_btn = ttk.Button(frame, text="Create Account", command=lambda: show_register_screen(root, mode_button_text))

    login_btn.pack(pady=15, ipadx=20)
    register_btn.pack(pady=5, ipadx=20)

    # Bottom right buttons frame
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    
    mode_button_text.set("Light Mode" if theme.current_theme == theme.dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: theme.toggle_theme(root, lambda r: show_login_screen(r, mode_button_text), mode_button_text)

    )
    dark_btn.pack(side=tk.RIGHT, padx=5)
    dark_btn.configure(style="Dark.TButton")
    
    # Add exit button
    exit_btn = ttk.Button(
        bottom_frame,
        text="Exit",
        command=root.destroy,
        style="Dark.TButton"
    )
    exit_btn.pack(side=tk.RIGHT, padx=5)

def login_form(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()
        
    from login.login_page import show_login_screen

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TLabel", background=theme.current_theme["bg"], foreground=theme.current_theme["fg"], font=("Segoe UI", 13))
    style.configure("TButton", font=("Segoe UI", 14), padding=12)

    # Entry styling based on theme
    entry_style_name = "Dark.TEntry" if theme.current_theme == theme.dark_theme else "Light.TEntry"
    style.configure(entry_style_name,
        foreground=theme.current_theme["entry_fg"],
        fieldbackground=theme.current_theme["entry_bg"],
        background=theme.current_theme["entry_bg"],
        font=("Segoe UI", 13)
    )

    root.configure(bg=theme.current_theme["bg"])
    frame = tk.Frame(root, bg=theme.current_theme["bg"])
    frame.pack(expand=True, fill="both")

    title = tk.Label(frame, text="Login", font=("Segoe UI", 26, "bold"),
                     fg=theme.current_theme["accent"], bg=theme.current_theme["bg"])
    title.pack(pady=(60, 30))

    form_frame = tk.Frame(frame, bg=theme.current_theme["bg"])
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
        bg=theme.current_theme["bg"],
        fg=theme.current_theme["fg"],
        activebackground=theme.current_theme["bg"],
        activeforeground=theme.current_theme["fg"],
        font=("Segoe UI", 10),
        bd=0,
        highlightthickness=0,
        selectcolor=theme.current_theme["bg"]
    )

    check_btn.grid(row=2, column=1, sticky="w", padx=4)

    def handle_login():
        email = email_entry.get()
        password = password_var.get()
        print(f"Login attempted with email: {email}, password: {password}")
        if login_check_info(email, password):
            messagebox.showinfo("Login Successful", "Welcome back!")
            show_blank_page(root, mode_button_text)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

    button_frame = tk.Frame(frame, bg=theme.current_theme["bg"])
    button_frame.pack(pady=40)

    ttk.Button(button_frame, text="Submit", command=handle_login).pack(pady=10, ipadx=15)
    ttk.Button(button_frame, text="Back", command=lambda: show_login_screen(root, mode_button_text)).pack(pady=5, ipadx=15)

    # Bottom right buttons frame
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    
    mode_button_text.set("Light Mode" if theme.current_theme == theme.dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: theme.toggle_theme(root, lambda r: show_login_screen(r, mode_button_text), mode_button_text)

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
