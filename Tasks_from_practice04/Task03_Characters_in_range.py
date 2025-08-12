def character_in_range(first_char, second_char) -> str:
    char_list = []
    for char in range(ord(first_character) + 1, ord(second_character)):
        char_list.append(chr(char))
    return char_list


first_character = input()
second_character = input()

result = (character_in_range(first_character, second_character))
print(" ".join(result))