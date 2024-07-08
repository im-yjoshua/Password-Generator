import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length > 4:
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    else:
        print("The length of the password should be greater than 4.")
        return None

length = int(input("Enter the length of the password: "))
print(f"Generated password: {generate_password(length)}")
