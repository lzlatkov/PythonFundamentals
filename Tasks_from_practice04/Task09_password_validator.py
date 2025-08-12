def password_lenght(some_string: str) -> bool:
    if len(some_string) < 6 or len(some_string) > 10:
        return False
    return True


def password_digit_letter(some_string: str) -> bool:
    for element in some_string:
        if ord(element) not in range(97, 123) and ord(element) not in range(65, 91) and ord(element) not in range(48, 58):
            return False
    return True


def password_digit(some_string: str) -> bool:
    digit_sum = 0
    for element in some_string:
        if ord(element) in range(48, 58):
            digit_sum += 1
    if digit_sum < 2:
        return False
    return True


user_password = input()
if not password_lenght(user_password):
    print("Password must be between 6 and 10 characters")
if not password_digit_letter(user_password):
    print("Password must consist only of letters and digits")
if not password_digit(user_password):
    print("Password must have at least 2 digits")
if password_lenght(user_password) and password_digit_letter(user_password) and password_digit(user_password):
    print("Password is valid")