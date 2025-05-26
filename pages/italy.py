import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from main import theme
from main.database import get_hotels
from pages.main_page import show_page
from pages import reservations

def show_country_page(root, mode_button_text):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=theme.current_theme["bg"])

    # Get hotel data (Italy → ID 2)
    hotel_data = next((h for h in get_hotels() if h["ID"] == 2), None)

    if not hotel_data:
        tk.Label(root, text="Hotel not found.", font=("Segoe UI", 16), bg=theme.current_theme["bg"], fg="red").pack(pady=20)
        return

    hotel_name = hotel_data["Nume"]
    facilities = [f.strip() for f in hotel_data["Facilities"].split(",")] if hotel_data["Facilities"] else []

    # Title
    title_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    title_frame.pack(anchor="w", padx=30, pady=(20, 10))

    tk.Label(title_frame, text=hotel_name, font=("Segoe UI", 24, "bold"),
         fg=theme.current_theme["accent"], bg=theme.current_theme["bg"]).pack(side="left")

    stars = "★" * int(hotel_data["Stars"])
    tk.Label(title_frame, text=stars, font=("Segoe UI", 18),
            fg="gold", bg=theme.current_theme["bg"]).pack(side="left", padx=10)


    main_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    main_frame.pack(fill="both", expand=True, padx=30, pady=10)

    # Left: image + facilities
    left_frame = tk.Frame(main_frame, bg=theme.current_theme["bg"])
    left_frame.grid(row=0, column=0, sticky="nw")

    image_display = tk.Label(left_frame, bg=theme.current_theme["bg"])
    image_display.pack()

    fac_frame = tk.Frame(left_frame, bg=theme.current_theme["bg"])
    fac_frame.pack(anchor="w", pady=(10, 0))

    tk.Label(fac_frame, text="Facilities:", font=("Segoe UI", 11, "bold"),
             fg="gray", bg=theme.current_theme["bg"]).pack(anchor="w")

    line = tk.Frame(fac_frame, bg=theme.current_theme["bg"])
    line.pack(anchor="w", pady=(2, 10))

    for fac in facilities:
        tk.Label(line, text=fac, font=("Segoe UI", 11),
                 fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(side="left", padx=10)
    # Price
    price = hotel_data["Price"]
    tk.Label(fac_frame, text=f"Price: €{price}/night", font=("Segoe UI", 12, "bold"),
            fg=theme.current_theme["fg"], bg=theme.current_theme["bg"]).pack(anchor="w", pady=(10, 0))

    ttk.Button(fac_frame, text="📅 Make a Reservation",
           command=lambda: reservations.show_reservation_page(root, mode_button_text, hotel_id=2),
           style="Accent.TButton").pack(anchor="w", pady=(20, 0), ipadx=10, ipady=5)


    # Right: thumbnails
    right_frame = tk.Frame(main_frame, bg=theme.current_theme["bg"])
    right_frame.grid(row=0, column=1, sticky="n", padx=(20, 0))

    thumb_canvas = tk.Canvas(right_frame, bg=theme.current_theme["bg"], highlightthickness=0, width=160)
    thumb_scroll = ttk.Scrollbar(right_frame, orient="vertical", command=thumb_canvas.yview)
    thumb_container = tk.Frame(thumb_canvas, bg=theme.current_theme["bg"])

    thumb_container.bind("<Configure>", lambda e: thumb_canvas.configure(scrollregion=thumb_canvas.bbox("all")))
    thumb_canvas.create_window((0, 0), window=thumb_container, anchor="nw")
    thumb_canvas.configure(yscrollcommand=thumb_scroll.set)

    thumb_canvas.pack(side="left", fill="y", expand=False)
    thumb_scroll.pack(side="right", fill="y")

    image_refs = []
    image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "photos", "italy"))

    def show_image(path):
        img = Image.open(path).resize((700, 450))
        img_tk = ImageTk.PhotoImage(img)
        image_display.config(image=img_tk)
        image_display.image = img_tk

    if os.path.exists(image_dir):
        images = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg"))])
        if images:
            show_image(images[0])

            for img_path in images:
                img = Image.open(img_path).resize((140, 90))
                img_tk = ImageTk.PhotoImage(img)
                image_refs.append(img_tk)
                thumb = tk.Button(thumb_container, image=img_tk, command=lambda p=img_path: show_image(p), bg=theme.current_theme["bg"], bd=0)
                thumb.image = img_tk
                thumb.pack(pady=5)

    # Bottom buttons
    bottom_frame = tk.Frame(root, bg=theme.current_theme["bg"])
    bottom_frame.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    mode_button_text.set("☀️ Light Mode" if theme.current_theme == theme.dark_theme else "🌕 Dark Mode")

    ttk.Button(bottom_frame, textvariable=mode_button_text,
               command=lambda: theme.toggle_theme(root, lambda r: show_country_page(r, mode_button_text), mode_button_text),
               style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="⬅️ Back", command=lambda: show_page(root, mode_button_text), style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
    ttk.Button(bottom_frame, text="❌ Exit", command=root.destroy, style="Dark.TButton").pack(side=tk.RIGHT, padx=5)
