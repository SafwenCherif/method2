import string

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_punctuation = False

    if len(password) >= 8:
        print("Length: OK")
    else:
        print("Length: Too short (must be at least 8 characters)")

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in string.punctuation:
            has_punctuation = True

    if has_upper and has_lower:
        print("Uppercase and lowercase: OK")
    else:
        print("Uppercase and lowercase: Missing (must contain both upper and lower case letters)")

    if has_digit:
        print("Numerical digit: OK")
    else:
        print("Numerical digit: Missing (must contain at least one digit)")

    if has_punctuation:
        print("Punctuation: OK")
    else:
        print("Punctuation: Missing (must contain at least one punctuation)")

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_punctuation:
        print("Password is strong!")
        return True
    else:
        print("Password is weak. Please try again.")
        return False


password = input("Enter a password: ")
print("Strength Check:")
ok=check_password_strength(password)
while not ok:
    password = input("ReEnter a password: ")
    print("Strength Check:")
    ok=check_password_strength(password)
