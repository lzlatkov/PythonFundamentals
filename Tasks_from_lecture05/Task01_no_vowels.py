text = input()

filtered_text = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(filtered_text))