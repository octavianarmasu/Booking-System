import tkinter as tk

from login.login_page import show_login_screen

def main():
    root = tk.Tk()
    root.title("Hotel Booking System")

    # FULLSCREEN + RESIZABLE
    root.attributes('-fullscreen', True)  
    root.resizable(True, True)            

    root.configure(bg='white')

    show_login_screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
