def fetch_user(username):
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_data = line.strip().split(":")
            if user_data[0] == username:
                return user_data
    return None
