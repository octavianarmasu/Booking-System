import tkinter as tk
from login.login_page import show_login_screen

def main():
    root = tk.Tk()
    root.title("Hotel Booking System")
    root.geometry("1000x800")
    root.resizable(True, True)
    root.configure(bg='white')

    mode_button_text = tk.StringVar(value="Dark Mode")
    show_login_screen(root, mode_button_text)
    root.mainloop()


if __name__ == "__main__":
    main()
