def fetch_all_users():
    users = []
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_data = line.strip().split(":")
            users.append(user_data)
    return users
