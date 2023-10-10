import random
import string

def generate_password(length=8):
    if length < 6:
        print("Password length should be at    ")
        return None
    
    charset = string.ascii_letters + string.digits + "!@#$%^"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^"),
    ] + [random.choice(charset) for i in range(length-4)]
    
    random.shuffle(password)
    
    return ''.join(password)

# Test
print(generate_password(10))  # This will print a 10-character password that meets the standards
