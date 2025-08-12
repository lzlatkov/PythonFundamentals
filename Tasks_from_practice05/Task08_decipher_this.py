# secret_message = input().split()
# deciphered_message = []
# for word in secret_message:
#     temp_word = " "
#     string1 = " "
#     string2 = " "
#     for char in word:
#         if 48 <= ord(char) <= 57:
#             string1 += char
#         else:
#             string2 += char
#     if string1 != "":
#         word = chr(int(string1)) + string2
#     if len(word) > 2:
#         temp_word = word[0] + word[len(word) - 1]
#         for index in range(2, len(word) - 1):
#             temp_word += word[index]
#         temp_word += word[1]
#         word = temp_word
#     deciphered_message.append(word)
#
# print(" ".join(deciphered_message))


secret_message = input().split()
deciphered_message = []
for word in secret_message:
    i = 0
    while i < len(word) and word[i].isdigit():
        i += 1
    char_code = int(word[:i])
    first_letter = chr(char_code)
    rest_of_word = word[i:]
    if len(rest_of_word) > 1:
        rest_of_word = list(rest_of_word)
        rest_of_word[0], rest_of_word[-1] = rest_of_word[-1], rest_of_word[0]
        rest_of_word = ''.join(rest_of_word)
        deciphered_word = first_letter + rest_of_word
        deciphered_message.append(deciphered_word)
    final_message = ' '.join(deciphered_message)
print(final_message)
