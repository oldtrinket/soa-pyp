def main_menu():
    while True:
        print("\n------- GELOS Enterprises -------")
        print("1. Login")
        print("2. Register")
        print("3. Change Password")
        print("4. Reset Password")
        print("5. View Accounts (Admin Only)")
        print("6. Exit")
        choice = input("\nChoose an option: ").lower()

        if choice == '1' or choice == 'login':
            # Call login function
            pass
        elif choice == '2' or choice == 'register':
            # Call register function
            pass
        elif choice == '3' or choice == 'change password':
            # Call change password function
            pass
        elif choice == '4' or choice == 'reset password':
            # Call reset password function
            pass
        elif choice == '5' or choice == 'view accounts':
            # Call view accounts function
            pass
        elif choice == '6' or choice == 'exit':
            # Call exit function
            break
        else:
            print("Invalid option.   ")
