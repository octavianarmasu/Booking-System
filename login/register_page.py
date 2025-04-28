import tkinter as tk
from tkinter import ttk, messagebox

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
    check_btn.grid(row=len(labels), column=1, sticky="w", padx=4)

    def handle_register():
        values = {label: entry.get() for label, entry in entries.items()}
        if values["Password"] != values["Confirm Password"]:
            messagebox.showerror("Error", "Passwords do not match")
            return
        print(f"Account created: {values}")  # ADD DATABASE INSERTION HERE

    button_frame = tk.Frame(frame, bg=current_theme["bg"])
    button_frame.pack(pady=40)

    ttk.Button(button_frame, text="Register", command=handle_register).pack(pady=10, ipadx=15)
    ttk.Button(button_frame, text="Back", command=lambda: show_login_screen(root, mode_button_text)).pack(pady=5, ipadx=15)

    mode_button_text.set("Light Mode" if current_theme == dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        root,
        textvariable=mode_button_text,
        command=lambda: toggle_theme(root, lambda r: show_register_screen(r, mode_button_text))
    )
    dark_btn.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)
    dark_btn.configure(style="Dark.TButton")
