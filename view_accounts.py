def view_accounts():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    if is_admin_authenticated(username, password):
        users = fetch_all_users()
        for user in users:
            print(f"Username: {user[0]}, Security Question: {user[2]}, Security Answer: {user[3]}")
    else:
        print("Invalid admin credentials!")
