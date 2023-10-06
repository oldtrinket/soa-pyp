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
