import string

print("*" * 130)
print("Welcome to Smart Password Strength Checker!!")
print("," * 130)

while True:
    score = 0  # Reset score for each new password
    Inp_pass = input("Enter your password:\n")

    # Checks
    has_upper = any(char.isupper() for char in Inp_pass)
    has_lower = any(char.islower() for char in Inp_pass)
    has_digit = any(char.isdigit() for char in Inp_pass)
    has_punctuation = any(char in string.punctuation for char in Inp_pass)
    length_ok = len(Inp_pass) >= 8  # Minimum length check

    # Calculate score
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_punctuation:
        score += 1
    if length_ok:
        score += 1  # Max score = 5 now

    # Rate password
    if score == 5:
        print("Password is VERY STRONG 🔐")
    elif score == 4:
        print("Password is STRONG ✅")
    elif score == 3:
        print("Password is MODERATE ⚠️")
    elif score == 2:
        print("Password is WEAK ❌")
    else:
        print("Password is VERY WEAK 🚫")

    # Ask to retry
    while True:
        use_again = input("Do you want to check another password? (yes/no): ").lower()
        if use_again == "no":
            print("<" * 130)
            print("Thanks for using Smart Password Strength Checker! Goodbye 👋💖")
            print("<" * 130)
            exit()
        elif use_again == "yes":
            print("*" * 130)
            break
        else:
            print("Invalid choice! Enter 'yes' or 'no'.")