# 🏨 Hotel Booking System

A desktop GUI application built with **Tkinter** that allows users to register, log in, browse hotels by country, view details and reviews, and switch between **light and dark themes**. 

The app uses **SQLite** for persistent storage and **Pillow (PIL)** for image handling.

---

## 📁 Project Structure

```
Booking-System/
├── login/              # Login and registration GUI logic
│   ├── login_page.py
│   ├── register_page.py
│   └── auth_utils.py
├── main/               # App entry point, theming, and database logic
│   ├── app.py
│   ├── theme.py
│   └── database.py
├── pages/              # Country-specific hotel views
│   ├── main_page.py
│   ├── greece.py
│   ├── italy.py
│   └── portugal.py
├── photos/             # Images organized by country
│   ├── Greece/
│   ├── Italy/
│   └── Portugal/
├── hotel_database.db   # SQLite database file
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. **Clone the repository** or download the code.

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the app**:

   ```bash
   python3 -m main.app
   ```

---

## ✨ Features

* 🧑‍💼 **Login & Register System** with password validation
* 💡 **Dark / Light Theme Toggle**
* 🌍 **Browse Hotels** by Country (Greece, Italy, Portugal)
* 🖼️ Hotel photos, reviews, ratings, facilities
* ✅ Clean UI with consistent design using `ttk`
* 🗃️ **SQLite** backend to store users and reservations
* 🔐 Password strength indicator and visibility toggle

---

## 🛠️ Requirements

The only external library required is:

```
pillow
```

> ✅ `tkinter` and `sqlite3` are included with standard Python installations — no need to install them separately.

---

## 📌 Future Improvements

* Add room booking UI and availability filtering
* Improve validation and error feedback
* Admin interface for managing hotels/rooms

---

## 🧑‍💻 Authors

This project was developed as part of a university coursework assignment. 
Contributors:
* Armașu Octavian
* Brutaru Bogdan
* Crețu Mihnea Tudor
* Tunsoiu Dan

---

## 📸 Screenshots

*TO ADD*

---

