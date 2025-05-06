import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import main.theme as theme

def show_blank_page(root, mode_button_text):
    from login.login_page import show_login_screen
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    # Top navigation buttons
    top_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    top_frame.pack(side=tk.TOP, fill="x", padx=10, pady=10)

    style = ttk.Style()
    style.configure("Top.TButton", font=("Segoe UI", 12), padding=6)

    ttk.Button(top_frame, text="Profile", style="Top.TButton", command=lambda: print("Profile clicked")).pack(side=tk.LEFT, padx=5)
    ttk.Button(top_frame, text="Reservations", style="Top.TButton", command=lambda: print("Reservations clicked")).pack(side=tk.LEFT, padx=5)
    ttk.Button(top_frame, text="Log Out", style="Top.TButton", command=lambda: show_login_screen(root, mode_button_text)).pack(side=tk.LEFT, padx=5)

    # Scrollable container
    canvas = tk.Canvas(root, bg=theme.current_theme["bg"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    hotel_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    hotel_frame.pack(expand=True, fill="both", padx=10, pady=20)
    hotel_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=hotel_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)


    hotel_data = [
        {"name": "Bella Vista Resort", "location": "Sicily, Italy", "rating": 4.5, "price": 150, "image": "", "stars": 4,
         "reviews":[
            "Amazing views and friendly staff!",
            "Loved the food and pool area.",
            "Great for families, we’ll be back!"
         ], "facilities" : ["Wi-Fi", "Pool", "Private Beach", "Breakfast included"]},
        {"name": "Ocean Breeze Hotel", "location": "Madeira, Portugal", "rating": 4.2, "price": 180, "image": "", "stars": 4,
         "reviews":[
            "Clean rooms and near the beach.",
            "Reception was helpful with activities.",
            "Wi-Fi was a bit slow, but still a nice stay."
         ], "facilities" : ["Wi-Fi", "Pool", "Beach Access", "Air Conditioning"]},
        {"name": "Aegean Paradise Hotel", "location": "Evia, Greece", "rating": 4.7, "price": 120, "image": "", "stars": 4,
         "reviews":[
            "Quiet location and beautiful sunsets!",
            "Affordable and comfortable rooms.",
            "Excellent value for the money."
         ], "facilities" : ["Wi-Fi", "Pool", "Private Beach", "Spa", "Air Conditioning"]}
    ]

    for i, hotel in enumerate(hotel_data):
        hotel_frame_row = tk.Frame(hotel_frame, bg=theme.current_theme["bg"])
        hotel_frame_row.grid(row=i, column=0, padx=10, pady=15, sticky="w")

        # Placeholder image
        img_label = tk.Label(hotel_frame_row, text="[Image]", width=20, height=10, bg=theme.current_theme["bg"], fg=theme.current_theme["fg"])
        img_label.grid(row=0, column=0, rowspan=2, padx=10)

        # Name and location container
        name_loc_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        name_loc_frame.grid(row=0, column=1, sticky="w")

        # Hotel name (blue)
        name_label = tk.Label(name_loc_frame, text=hotel["name"], font=("Segoe UI", 14, "bold"), fg="blue", bg=theme.current_theme["bg"])
        name_label.pack(anchor="w")

        # Location (smaller, just under the name)
        location_label = tk.Label(name_loc_frame, text=hotel["location"], font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
        location_label.pack(anchor="w", pady=(0, 2))

        # Rating and stars
        rating_star_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        rating_star_frame.grid(row=0, column=2, sticky="w", padx=20)

        stars = "★" * hotel["stars"]
        star_label = tk.Label(rating_star_frame, text=stars, font=("Segoe UI", 12), fg="gold", bg=theme.current_theme["bg"])
        star_label.pack(anchor="w")

        rating_label = tk.Label(rating_star_frame, text=f"Rating: {hotel['rating']}/5", font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
        rating_label.pack(anchor="w")

        # Price per night (aligned to far right)
        price_label = tk.Label(hotel_frame_row, text=f"€{hotel['price']}/night", font=("Segoe UI", 12, "bold"), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
        price_label.grid(row=0, column=3, sticky="e", padx=40)

        # Reviews section
        reviews_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        reviews_frame.grid(row=1, column=1, columnspan=3, sticky="w", pady=(10, 0))
        review_title = tk.Label(reviews_frame, text="User Reviews:", font=("Segoe UI", 10, "italic"), fg="gray", bg=theme.current_theme["bg"])
        review_title.pack(anchor="w")
        for review in hotel["reviews"]:
            review_label = tk.Label(reviews_frame, text=f"• {review}", font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
            review_label.pack(anchor="w")

        # Facilities section
        facilities_frame = tk.Frame(hotel_frame_row, bg=theme.current_theme["bg"])
        facilities_frame.grid(row=2, column=1, columnspan=3, sticky="w", pady=(5, 0))

        fac_title = tk.Label(facilities_frame, text="Facilities:", font=("Segoe UI", 10, "italic"), fg="gray", bg=theme.current_theme["bg"])
        fac_title.pack(anchor="w")

        for fac in hotel["facilities"]:
            fac_label = tk.Label(facilities_frame, text=f"• {fac}", font=("Segoe UI", 10), fg=theme.current_theme["fg"], bg=theme.current_theme["bg"])
            fac_label.pack(anchor="w")

    # Bottom right buttons frame
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("Light Mode" if theme.current_theme == theme.dark_theme else "Dark Mode")
    dark_btn = ttk.Button(
        bottom_frame,
        textvariable=mode_button_text,
        command=lambda: theme.toggle_theme(root, lambda r: show_blank_page(r, mode_button_text), mode_button_text)
    )
    dark_btn.pack(side=tk.RIGHT, padx=5)

    style.configure("Dark.TButton", font=("Segoe UI", 14), padding=4)
    dark_btn.configure(style="Dark.TButton")

    exit_btn = ttk.Button(
        bottom_frame,
        text="Exit",
        command=root.destroy,
        style="Dark.TButton"
    )
    exit_btn.pack(side=tk.RIGHT, padx=5)
