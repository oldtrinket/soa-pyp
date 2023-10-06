import re
import random
import string
from datetime import datetime
import time

# Initialize constants and global variables
SYSTEM_ADMIN_USERNAME = "admin"
SYSTEM_ADMIN_PASSWORD = "admin@123"
start_time = datetime.now()

# Validation and Generation Functions
def validate_password(password):
    if (
        re.search("[A-Z]", password) and          
        re.search("[a-z]", password) and          
        re.search("[0-9]", password) and         
        re.search("[!@#$%^]", password) and       
        len(password) >= 6                        
    ):
        return True
    return False

def generate_password(length=8):
    charset = string.ascii_letters + string.digits + "!@#$%^"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^"),
    ] + [random.choice(charset) for i in range(length-4)]
    random.shuffle(password)
    return ''.join(password)

def is_admin_authenticated(username, password):
    return username == SYSTEM_ADMIN_USERNAME and password == SYSTEM_ADMIN_PASSWORD

def fetch_user(username):
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_data = line.strip().split(":")
            if user_data[0] == username:
                return user_data
    return None

def save_user(username, password, security_question, security_answer):
    with open("accounts.txt", "a") as file:
        file.write(f"{username}:{password}:{security_question}:{security_answer}\n")

def update_password(username, new_password):
    lines = []
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
    with open("accounts.txt", "w") as file:
        for line in lines:
            user_data = line.strip().split(":")
            if user_data[0] == username:
                file.write(f"{username}:{new_password}:{user_data[2]}:{user_data[3]}\n")
            else:
                file.write(line)

def fetch_all_users():
    users = []
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_data = line.strip().split(":")
            users.append(user_data)
    return users

def display_duration():
    end_time = datetime.now()
    duration = end_time - start_time
    minutes, seconds = divmod(duration.seconds, 60)
    print(f"\nYou've used the system for {minutes} minutes and {seconds} seconds.")
    time.sleep(2)

# Main Menu
def main_menu():
    while True:
        print("\n------- GELOS Enterprises -------")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("1. Login")
        print("2. Register")
        print("3. Change Password")
        print("4. Reset Password")
        print("5. View Accounts (Admin Only)")
        print("6. Exit")
        choice = input("\nChoose an option: ").lower()

        # ... (Handle each choice, e.g., if choice == '1' or choice == 'login': login_function())

        # Exit
        if choice == '6' or choice == 'exit':
            display_duration()
            break

# ... (Other functions such as login, register, etc.)

# Start the program
if __name__ == "__main__":
    # Check if accounts.txt exists, if not create it
    try:
        with open('accounts.txt', 'r') as file:
            pass
    except FileNotFoundError:
        with open('accounts.txt', 'w') as file:
            pass

    main_menu()
