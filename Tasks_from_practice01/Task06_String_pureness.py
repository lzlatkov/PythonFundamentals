number = int(input())

for strings in range(number):
    user_input = input()

    if ',' in user_input or '.' in user_input or '_' in user_input:
        print(f'{user_input} is not pure!')
    else:
        print(f'{user_input} is pure.')
