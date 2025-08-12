user_input = int(input())
output = ''

for i in range(1, user_input + 1):
    number = int(input())
    if number == 88:
        output = 'Hello'
    elif number == 86:
        output = 'How are you?'
    elif number != 88 and number != 86 and number < 88:
        output = 'GREAT!'
    else:
        output = 'Bye.'

print(output)