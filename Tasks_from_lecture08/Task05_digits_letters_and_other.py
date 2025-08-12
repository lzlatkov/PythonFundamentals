user_input = input()
digits = ""
letters = ""
characters = ""

for symbol in user_input:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        characters += symbol

print(f"{digits}\n{letters}\n{characters}")
