def is_palindrome(some_number_as_string):
    return some_number_as_string == some_number_as_string[::-1]


numbers_as_string = input().split(", ")
for number in numbers_as_string:
    print(is_palindrome(number))