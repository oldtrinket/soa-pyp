file_path = "userfile.txt"

user_response = input("Do you want to print the content of the text file? (yes/no) ").lower()

if user_response == 'yes':
    with open(file_path, 'r') as file:
        data = file.readlines()
        for line in data:
            name, surname, password = line.strip().split()  # Assuming the data in the file is space-separated
            print(f"Net User: {name}.{surname} Password: {password}")
else:
    print("Okay, content will not be printed
    .")
