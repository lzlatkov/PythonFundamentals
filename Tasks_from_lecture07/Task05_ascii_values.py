characters = input().split(", ")
char_dict = {}

for element in range(0, len(characters)):
    key = characters[element]
    value = ord(characters[element])
    char_dict[key] = value
    if element in char_dict:
        continue
print(char_dict)