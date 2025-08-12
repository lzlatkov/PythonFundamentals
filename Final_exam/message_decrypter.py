import re

number_of_checks = int(input())
pattern = re.compile(r'^([$%])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$')

for command in range(number_of_checks):
    user_input = input()
    matched_commands = pattern.match(user_input)
    tag = ""
    deciphered_sting = ""
    if matched_commands:
        split_command = user_input.split(": ")
        testing = user_input[0]
        for char in split_command[0]:
            if char != testing:
                tag += char
        numbers_split = split_command[1].split("|")
        del numbers_split[3]
        for number in numbers_split:
            filtered_num = ''.join(filter(str.isdigit, number))
            deciphered_sting += chr(int(filtered_num))
        print(f"{tag}: {deciphered_sting}")
    else:
        print("Valid message not found!")