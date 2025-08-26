import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True, use_upper=True):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_upper:
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

   
    length = int(input("Enter password length: "))
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"

    password = generate_password(length, use_digits, use_symbols, use_upper)
    print("\nGenerated Password:", password)

    with open("PassGen.txt", "a") as file:
        file.write(password + "\n")

    print("Password saved to PassGen.txt")

if __name__ == "__main__":
    main()
