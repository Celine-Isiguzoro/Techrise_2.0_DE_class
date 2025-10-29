def validate_password(password):
    if len(password) < 8:
        return False 

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    return has_upper and has_lower and has_digit


print(validate_password("Hello123"))
print(validate_password("Hello"))