number = int(input())

for letter1 in range(0, number):
    for letter2 in range(0, number):
        for letter3 in range(0, number):
            print(f'{chr(97 + letter1)}{chr(97 + letter2)}{chr(97 + letter3)}')