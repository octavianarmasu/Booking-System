import tkinter as tk

def show_login_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    from login.register_page import show_register_screen

    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True, fill="both")
    
    title = tk.Label(frame, text="Welcome to our hotel", font=("Arial", 28, "bold"), fg="blue", bg="white")
    subtitle = tk.Label(frame, text="Please login or create an account", font=("Arial", 16), bg="white", fg="black")

    title.pack(pady=60)
    subtitle.pack(pady=10)

    login_btn = tk.Button(frame, text="Login", width=20, height=2, command=lambda: login_form(root))
    register_btn = tk.Button(frame, text="Create Account", width=20, height=2, command=lambda: show_register_screen(root))

    login_btn.pack(pady=20)
    register_btn.pack()

def login_form(root):
    for widget in root.winfo_children():
        widget.destroy()

    from login.login_page import show_login_screen

    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True, fill="both")

    tk.Label(frame, text="Login", font=("Arial", 22), bg="white").pack(pady=30)

    tk.Label(frame, text="Email", bg="white").pack()
    email_entry = tk.Entry(frame, width=40)
    email_entry.pack()

    tk.Label(frame, text="Password", bg="white").pack()
    password_entry = tk.Entry(frame, show="*", width=40)
    password_entry.pack()

    def handle_login():
        email = email_entry.get()
        password = password_entry.get()
        print(f"Login attempted with email: {email}, password: {password}")
        # ADD DATABASE CHECK HERE

    tk.Button(frame, text="Submit", command=handle_login).pack(pady=20)
    tk.Button(frame, text="Back", command=lambda: show_login_screen(root)).pack()
