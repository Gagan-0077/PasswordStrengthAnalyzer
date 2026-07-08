import re
import random
import string
def check_password_strength(password):
    score = 0
    missing = []
    if len(password) >= 8:
        score += 1
    else:
        missing.append("Password should contain at least 8 characters.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        missing.append("Add at least one uppercase letter (A-Z).")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        missing.append("Add at least one lowercase letter (a-z).")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        missing.append("Add at least one number (0-9).")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        missing.append("Add at least one special character (!@#$%^&* etc.).")
    print("\n========== PASSWORD ANALYSIS ==========")
    if score <= 2:
        print("Strength : WEAK")
    elif score <= 4:
        print("Strength : MEDIUM")
    else:
        print("Strength : STRONG")
    print(f"Security Score : {score}/5")
    if missing:
        print("\nSuggestions:")
        for item in missing:
            print("•", item)
    else:
        print("\nExcellent! Your password meets all security requirements.")
def generate_password(length):
    if length < 8:
        print("Password length must be at least 8.")
        return
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
    remaining = ''.join(random.choice(
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    ) for _ in range(length - 4))
    password = list(uppercase + lowercase + digit + special + remaining)
    random.shuffle(password)
    print("\nGenerated Strong Password:")
    print(''.join(password))
def main():
    while True:
        print("\n======================================")
        print(" PASSWORD STRENGTH ANALYZER ")
        print("======================================")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            password = input("\nEnter your password: ")
            check_password_strength(password)
        elif choice == "2":
            try:
                length = int(input("Enter password length (minimum 8): "))
                generate_password(length)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            print("\nThank you for using Password Strength Analyzer!")
            break
        else:
            print("\nInvalid choice! Please try again.")
if __name__ == "__main__":
    main()
