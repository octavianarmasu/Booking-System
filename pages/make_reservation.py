import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from main import theme
from pages.main_page import show_page
import pages.italy as italy
import pages.portugal as portugal
import pages.greece as greece
from main.database import get_hotels, check_available_room, add_rezervare
from main.session import current_user_email

def show_reservation_page(root, mode_button_text, hotel_id):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])
    hotel_name = [h['Nume'] for h in get_hotels() if h['ID'] == hotel_id][0]

    title = tk.Label(root, text=f"Rezervare la {hotel_name}", font=("Segoe UI", 24, "bold"),
                     fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
    title.pack(pady=20)

    frame = tk.Frame(root, bg=theme.current_theme["bg"])
    frame.pack()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    today_str = today.strftime("%Y-%m-%d")
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")

    entry_bg = "#fff" if theme.current_theme == theme.light_theme else "#444"
    entry_fg = "#000" if theme.current_theme == theme.light_theme else "#fff"

    tk.Label(frame, text="Data Cazare (YYYY-MM-DD):", bg=theme.current_theme["bg"], fg=theme.current_theme["fg"]).grid(row=0, column=0, sticky="e", pady=5)
    checkin_entry = tk.Entry(frame, bg=entry_bg, fg=entry_fg)
    checkin_entry.insert(0, today_str)
    checkin_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Data Eliberare (YYYY-MM-DD):", bg=theme.current_theme["bg"], fg=theme.current_theme["fg"]).grid(row=1, column=0, sticky="e", pady=5)
    checkout_entry = tk.Entry(frame, bg=entry_bg, fg=entry_fg)
    checkout_entry.insert(0, tomorrow_str)
    checkout_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Tip cameră:", bg=theme.current_theme["bg"], fg=theme.current_theme["fg"]).grid(row=2, column=0, sticky="e", pady=5)
    tip_var = tk.StringVar(value="Single-Room")
    tip_menu = ttk.Combobox(frame, values=["Single-Room", "Double-Room", "Apartament"], textvariable=tip_var, state="readonly")
    tip_menu.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Pozitionare:", bg=theme.current_theme["bg"], fg=theme.current_theme["fg"]).grid(row=3, column=0, sticky="e", pady=5)
    poz_var = tk.StringVar(value="La mare")
    poz_menu = ttk.Combobox(frame, values=["La mare", "Spre oras", "Pe laterale"], textvariable=poz_var, state="readonly")
    poz_menu.grid(row=3, column=1, pady=5)

    def rezervare():
        try:
            checkin = datetime.strptime(checkin_entry.get(), "%Y-%m-%d")
            checkout = datetime.strptime(checkout_entry.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Format greșit", "Introdu date valide in formatul YYYY-MM-DD.")
            return

        if checkin < today.replace(hour=0, minute=0, second=0, microsecond=0) or checkout <= checkin:
            messagebox.showerror("Date invalide", "Datele trebuie să fie din viitor, iar check-out > check-in.")
            return

        tip = tip_var.get()
        poz = poz_var.get()
        checkin_str = checkin.strftime("%Y-%m-%d")
        checkout_str = checkout.strftime("%Y-%m-%d")

        # Search for available room
        camera = check_available_room(hotel_name, tip, poz, checkin_str, checkout_str)
        
        if camera:
            # Add reservation
            result = add_rezervare(camera['ID Camera'], hotel_id, checkin_str, checkout_str, current_user_email)
            if result != -1:
                messagebox.showinfo("Succes", f"Rezervarea a fost făcută la etajul {camera['Etaj']}!")
                show_page(root, mode_button_text)
            else:
                messagebox.showerror("Eroare", "A apărut o eroare la efectuarea rezervării.")
        else:
            messagebox.showwarning("Indisponibil", 
                "Nu există camere disponibile cu criteriile selectate.")

    tk.Button(root, text="Rezervă acum", command=rezervare, font=("Segoe UI", 12), bg="#ddd", padx=15, pady=5).pack(pady=15)

    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("☀️ Light Mode" if theme.current_theme == theme.dark_theme else "🌕 Dark Mode")
    ttk.Button(bottom_frame, textvariable=mode_button_text,
               command=lambda: theme.toggle_theme(root, lambda r: show_reservation_page(r, mode_button_text, hotel_id), mode_button_text),
               style="Dark.TButton").pack(side=tk.RIGHT, padx=5)

    def go_back():
        if hotel_id == 2:
            italy.show_country_page(root, mode_button_text)
        elif hotel_id == 3:
            portugal.show_country_page(root, mode_button_text)
        elif hotel_id == 4:
            greece.show_country_page(root, mode_button_text)
        else:
            show_page(root, mode_button_text)

    ttk.Button(bottom_frame, text="⬅️ Back", command=go_back, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="❌ Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)