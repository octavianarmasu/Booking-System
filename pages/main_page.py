import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import importlib
import main.theme as theme
from main.database import get_hotels


def show_page(root, mode_button_text):
    from login.login_page import show_login_screen
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    top_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    top_frame.pack(side=tk.TOP, fill="x", padx=10, pady=10)

    style = ttk.Style()
    style.configure("Top.TButton", font=("Segoe UI", 12), padding=6)

    ttk.Button(top_frame, text="Profile", style="Top.TButton", command=lambda: print("Profile clicked")).pack(side=tk.LEFT, padx=5)
    ttk.Button(top_frame, text="Reservations", style="Top.TButton", command=lambda: print("Reservations clicked")).pack(side=tk.LEFT, padx=5)

    scroll_frame = tk.Frame(root)
    scroll_frame.pack(expand=True, fill="both", padx=10, pady=20)

    canvas = tk.Canvas(scroll_frame, bg=theme.current_theme["bg"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)

    hotel_frame = tk.Frame(canvas, bg=theme.current_theme["bg"])

    hotel_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=hotel_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    # scrollbar — invisible but functional
    # scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        if os.name == 'nt':  # Windows
            canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        elif os.name == 'posix': 
            canvas.yview_scroll(-1 * int(event.delta), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows/macOS
    canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
    canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down
    tabel = get_hotels()

    hotel_data = [
        {"name": "Bella Vista Resort", "location": "Sicily, Italy", "rating": 4.5, "price": 150, "stars": 4,
         "reviews": ["Amazing views and friendly staff!", "Loved the food and pool area.", "Great for families, we’ll be back!"],
         "facilities": ["Wi-Fi", "Pool", "Private Beach", "Breakfast included"]},
        {"name": "Ocean Breeze Hotel", "location": "Madeira, Portugal", "rating": 4.2, "price": 180, "stars": 4,
         "reviews": ["Clean rooms and near the beach.", "Reception was helpful with activities.", "Wi-Fi was a bit slow, but still a nice stay."],
         "facilities": ["Wi-Fi", "Pool", "Beach Access", "Air Conditioning"]},
        {"name": "Aegean Paradise Hotel", "location": "Evia, Greece", "rating": 4.7, "price": 120, "stars": 4,
         "reviews": ["Quiet location and beautiful sunsets!", "Affordable and comfortable rooms.", "Excellent value for the money."],
         "facilities": ["Wi-Fi", "Pool", "Private Beach", "Spa", "Air Conditioning"]}
    ]

    image_refs = []

    def open_country_page(root, country_name):
        try:
            module = importlib.import_module(f"pages.{country_name.lower()}")
            module.show_country_page(root, mode_button_text)
        except Exception as e:
            print(f"Error opening page for {country_name}: {e}")

    for i, hotel in enumerate(hotel_data):
        hotel_frame_row = tk.Frame(hotel_frame, bg=theme.current_theme["bg"])
        hotel_frame_row.grid(row=i, column=0, padx=10, pady=15, sticky="w")

        country = hotel["location"].split(",")[-1].strip()
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        image_path = os.path.join(base_dir, "photos", country, "image1.png")

        try:
            img = Image.open(image_path)
            img = img.resize((160, 100))
            photo = ImageTk.PhotoImage(img)
            image_refs.append(photo)
            img_label = tk.Label(hotel_frame_row, image=photo, bg=theme.current_theme["bg"])
            img_label.image = photo
        except Exception:
            img_label = tk.Label(hotel_frame_row, text="[Image not found]", width=20, height=10, fg="red", bg=theme.current_theme["bg"])

        img_label.grid(row=0, column=0, rowspan=2, padx=10)

        name_loc_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        name_loc_frame.grid(row=0, column=1, sticky="w")

        name_label = tk.Label(name_loc_frame, text=hotel["name"], font=("Segoe UI", 14, "bold"),
                              fg="blue", bg=theme.current_theme["bg"], cursor="hand2")
        name_label.pack(anchor="w")

        name_label.bind("<Button-1>", lambda e, c=country: open_country_page(root, c))

        tk.Label(name_loc_frame, text=hotel["location"], font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=(0, 2))

        rating_star_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        rating_star_frame.grid(row=0, column=2, sticky="w", padx=20)

        stars = "★" * hotel["stars"]
        tk.Label(rating_star_frame, text=stars, font=("Segoe UI", 12), fg="gold", bg=theme.current_theme["bg"]).pack(anchor="w")
        tk.Label(rating_star_frame, text=f"Rating: {hotel['rating']}/5", font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w")

        tk.Label(hotel_frame_row, text=f"€{hotel['price']}/night", font=("Segoe UI", 12, "bold"), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).grid(row=0, column=3, sticky="e", padx=40)

        reviews_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        reviews_frame.grid(row=1, column=1, columnspan=3, sticky="w", pady=(10, 0))
        tk.Label(reviews_frame, text="User Reviews:", font=("Segoe UI", 10, "italic"), fg="gray", bg=theme.current_theme["bg"]).pack(anchor="w")
        for review in hotel["reviews"]:
            tk.Label(reviews_frame, text=f"• {review}", font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w")

        facilities_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        facilities_frame.grid(row=2, column=1, columnspan=3, sticky="w", pady=(5, 0))
        tk.Label(facilities_frame, text="Facilities:", font=("Segoe UI", 10, "italic"), fg="gray", bg=theme.current_theme["bg"]).pack(anchor="w")
        for fac in hotel["facilities"]:
            tk.Label(facilities_frame, text=f"• {fac}", font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w")

    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("☀️ Light Mode" if theme.current_theme == theme.dark_theme else "🌕 Dark Mode")

    ttk.Button(bottom_frame, textvariable=mode_button_text,
           command=lambda: theme.toggle_theme(root, lambda r: show_page(r, mode_button_text), mode_button_text),
           style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="⬅️ Log Out",
           command=lambda: show_login_screen(root, mode_button_text),
           style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="❌ Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)