import re       
import random   
import string   
from datetime import datetime
import time

# Initialize constants and global variables

# I know, I'm aware that this is not the standard practice:)
# Again for simplicity of the program, I put everything here in this file. (variables, functions)
SYSTEM_ADMIN_USERNAME = "admin"
SYSTEM_ADMIN_PASSWORD = "admin@123"
start_time = datetime.now()

# Validation and Generation Functions
# I imported re for this function.
def validate_password(password):
    if (
        re.search("[A-Z]", password) and
        re.search("[a-z]", password) and
        re.search("[0-9]", password) and
        re.search("[!@#$%^]", password) and
        len(password) >= 8
    ):
        return True
    return False

# To make sure that during registration, new user will follow Gelos standards
# when creating a username in firstname.lastname format.
def validate_username(username):
    return re.fullmatch(r"[a-zA-Z]+\.[a-zA-Z]+", username) is not None


# I imported random and string for this function.
def generate_password(length=8):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    charset = string.ascii_letters + string.digits + "!@#$%^"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^"),
    ] + [random.choice(charset) for i in range(length-4)]     # I tried list comprehension for the first time haha:)
    random.shuffle(password)
    return ''.join(password)

# This authenticates if the entered credentials match the above hardcoded ADMIN credentials.
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

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter your name.surname: ")
        password = input("Enter your password: ")

        user_data = fetch_user(username)
        if user_data and user_data[1] == password:  # checking password from fetched data
            print(f"Welcome, {username}!")
            return  # successfully logged in, return to main menu
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect credentials. You have {attempts} attempts left.")
            else:
                print("Incorrect credentials. Please contact the system administrator.")
                return  # return to main menu after 3 failed attempts

# Gelos automation task # 1 -- Account Registration
def register():
    # Get the desired username
    while True:
        username = input("Enter a username using name.surname format (minimum 6 characters): ")
        if 6 <= len(username) <= 20:
            if validate_username(username):
                # Check if username already exists
                if not fetch_user(username):
                    break
                else:
                    print("This username already exists. Please choose another one.")
            else:
                print("Username should be in the name.surname format.")
        else:
            print("Username should be at least 6 characters.")

    # Get or generate the password
    while True:
        password_choice = input("Do you want to create your own password or have one generated? (Enter 'own' or 'generated'): ").lower()
        if password_choice == 'own':
            password = input("Enter a new 8+ char password with letter, number & symbol: ")
            if validate_password(password):
                break
            else:
                print("Password does not meet the GELOS standards. Please try again.")
        elif password_choice == 'generated':
            password = generate_password(8)  # Generates an 8-character password
            print(f"Your generated password is: {password}")
            break
        else:
            print("Invalid choice. Please enter 'own' or 'generated'.")

    # Get the security question and answer
    security_question = input("Enter a security question you will remember: ")
    security_answer = input("Enter the answer to your security question: ")

    # Save the new user's details
    save_user(username, password, security_question, security_answer)
    print(f"Registration successful, {username}!")

def change_password():
    # Ask the user for their current username and password
    username = input("Enter your name.surname: ")

    # Fetch the user details
    user_data = fetch_user(username)

    # If the user is found in the accounts.txt
    if user_data:
        current_password = input("Enter your current password: ")

        # Check if the entered password matches the stored password
        if current_password == user_data[1]:  # [1] is the index for the password in the accounts.txt

            # Ask for a new password and confirm it
            while True:
                new_password = input("Enter a new 8+ char password with letter, number & symbol: ")
                confirm_password = input("Confirm your new password: ")

                # Check if the passwords match and meet GELOS standards
                if new_password == confirm_password and validate_password(new_password):
                    # Update the password in accounts.txt
                    update_password(username, new_password)
                    print("Password updated successfully!")
                    break
                else:
                    # Give appropriate error messages
                    if new_password != confirm_password:
                        print("Passwords do not match. Please try again.")
                    elif not validate_password(new_password):
                        print("Password does not meet the GELOS standards. Please try again.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please try again.")

# Gelos automation task # 2 -- Password Reset System
def reset_password():
    # Ask the user for their username
    username = input("Enter your name.surname: ")

    # Fetch the user details
    user_data = fetch_user(username)

    # If the user is found in the accounts.txt
    if user_data:
        print(f"Security Question: {user_data[2]}")  # [2] is the index for the security question in the accounts.txt
        security_answer_input = input("Enter the answer to the security question: ")

        # Check if the provided answer matches the stored answer
        if security_answer_input == user_data[3]:  # [3] is the index for the security answer in the accounts.txt

            # Ask for a new password
            while True:
                new_password = input("Enter a new 8+ char password with letter, number & symbol: ")
                confirm_password = input("Confirm your new password: ")

                # Check if the passwords match and meet GELOS standards
                if new_password == confirm_password and validate_password(new_password):
                    # Update the password in accounts.txt
                    update_password(username, new_password)
                    print("Password reset successfully!")
                    break
                else:
                    # Give appropriate error messages
                    if new_password != confirm_password:
                        print("Passwords do not match. Please try again.")
                    elif not validate_password(new_password):
                        print("Password does not meet the GELOS standards. Please try again.")
        else:
            print("Incorrect answer to the security question. Please try again.")
    else:
        print("Username not found. Please try again.")


# Only ADMIN can use this provided that correct credentials are entered.
# Hardcoded within the program.
def view_accounts():
    # Authenticate admin
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if is_admin_authenticated(username, password):
        users = fetch_all_users()
        print("Debug: ", users)  # Debug print statement
        print("\n---- User Accounts ----")
        for user in users:
            if len(user) >= 4:  # Check if user has at least 4 elements (username,password,security question & answer)
                print(f"Username: {user[0]}, Security Question: {user[2]}, Security Answer: {user[3]}")
            else:
                print("Incomplete user data:", user)
    else:
        print("Invalid admin credentials!")

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

        # Login
        if choice == '1' or choice == 'login':
            login()

        # Register
        if choice == '2' or choice == 'register':
            register()

        # Change Password
        if choice == '3' or choice == 'change password':
            change_password()

        # Reset Password
        if choice == '4' or choice == 'reset password':
            reset_password()

        # View Accounts (Admin Only)
        if choice == '5' or choice == 'view accounts (admin only)':
            view_accounts()

        # Exit
        if choice == '6' or choice == 'exit':
            display_duration()
            break

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

 
       
   
   
       

      
       

     
        
      
       
           
         
       
         
       
      
          
        
       
            
     
      
           
   
   
          
