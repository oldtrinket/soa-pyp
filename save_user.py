def save_user(username, password, security_question, security_answer):
    with open("accounts.txt", "a") as file:
        file.write(f"{username}:{password}:{security_question}
