# main/session.py
current_user_email = None

def set_logged_in_user(email):
    global current_user_email
    current_user_email = email

def get_logged_in_user():
    return current_user_email

def logout():
    global current_user_email
    current_user_email = None