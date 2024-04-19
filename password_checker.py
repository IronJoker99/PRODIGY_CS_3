import re

def check_password_strength(password):
    """
    Checks the strength of a password based on various criteria.
    
    Parameters:
        password (str): The password to be checked.
    
    Returns:
        str: Feedback on the password strength.
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_error = re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password) is None
    
    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_error]
    error_count = sum(errors)
    
    if error_count == 0:
        return "Strong password"
    elif error_count == 1:
        return "Moderate password"
    else:
        return "Weak password"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
