first_char = int(input())
last_char = int(input())

for number in range(first_char, last_char + 1):
    print(chr(number), end=' ')
