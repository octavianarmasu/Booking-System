import tkinter as tk

def show_register_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    from login.login_page import show_login_screen 

    tk.Label(root, text="Create Account", font=("Arial", 18)).pack(pady=20)

    labels = ["First Name", "Last Name", "Email", "Phone", "Password", "Confirm Password"]
    entries = []

    for label in labels:
        tk.Label(root, text=label).pack()
        entry = tk.Entry(root, width=40, show="*" if "Password" in label else None)
        entry.pack()
        entries.append(entry)

    def handle_register():
        values = [e.get() for e in entries]
        if values[4] != values[5]:
            tk.messagebox.showerror("Error", "Passwords do not match")
            return
        print(f"Account created: {values}")  # ADD DATABASE INSERTION HERE

    tk.Button(root, text="Register", command=handle_register).pack(pady=20)
    tk.Button(root, text="Back", command=lambda: show_login_screen(root)).pack()
