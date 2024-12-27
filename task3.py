def checkpassword(password):
        # Criteria
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password)
    length_valid = len(password) >= 8

   
    checkstrength= sum([has_upper, has_lower, has_digit, has_special, length_valid])

    if checkstrength == 5:
        return "Strong Password: Meets all criteria."
    elif checkstrength >= 3:
        return "Moderate Password: Add more character variety or increase length."
    else:
        return "Weak Password: Use a mix of uppercase, lowercase, numbers, special characters, and at least 8 characters."


password = input("Enter a password: ")
feedback = checkpassword(password)
print(feedback)



















