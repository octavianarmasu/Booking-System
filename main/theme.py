light_theme = {
    "bg": "white", "fg": "black", "accent": "#28a745",
    "entry_bg": "white", "entry_fg": "black"
}

dark_theme = {
    "bg": "#1c1c1c", "fg": "#f5f5f5", "accent": "#00ff88",
    "entry_bg": "#2e2e2e", "entry_fg": "white"
}

current_theme = light_theme.copy()

def toggle_theme(root, refresh_screen, mode_button_text):
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme
    mode_button_text.set("Light Mode" if current_theme == dark_theme else "Dark Mode")
    refresh_screen(root)
