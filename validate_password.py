import re

def validate_password(password):
    if (
        re.search("[A-Z]", password) and          # At least one uppercase letter
        re.search("[a-z]", password) and          # At least one lowercase letter
        re.search("[0-9]", password) and          # At least one digit
        re.search("[!@#$%^]", password) and       # At least one special character
        len(password) >= 6                        # Password length check
    ):
        return True
    return False

# Test
password = "Passw0rd!"
print(validate_password(password))  # This should return True
