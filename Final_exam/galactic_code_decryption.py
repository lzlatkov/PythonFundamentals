coded_message = input()

while True:
    user_input = input()
    if user_input == "Finalize":
        break
    command = user_input.split()
    if command[0] == "Encrypt":
        reversed_string = coded_message[::-1]
        coded_message = reversed_string
        print(coded_message)
    elif command[0] == "Decrypt":
        swapped_message = coded_message.swapcase()
        coded_message = swapped_message
        print(coded_message)
    elif command[0] == "Substitute":
        old_char = command[1]
        new_char = command[2]
        if old_char not in coded_message:
            print("Character not found.")
        else:
            replaced_string = coded_message.replace(old_char, new_char)
            coded_message = replaced_string
            print(coded_message)
    elif command[0] == "Scramble":
        index = int(command[1])
        char = command[2]
        if index > len(coded_message):
            print("Index out of bounds.")
        else:
            # ? scrambled_string = coded_message.replace(coded_message[index], char)
            # ? coded_message = scrambled_string
            coded_message = coded_message[:index] + char + coded_message[index + 1:]
            print(coded_message)
    elif command[0] == "Remove":
        substring = command[1]
        removed_string = coded_message.replace(substring, "")
        coded_message = removed_string
        print(coded_message)
    else:
        print("Invalid command detected!")