string = input()
while string != 'End':
    if string != 'SoftUni':
        for symbol in string:
            print(symbol * 2, end='')
        print()
    string = input()

###########################
string = input()
while string != 'End':
    if string != 'SoftUni':
        new_string = ''
        for symbol in string:
            new_string += symbol * 2
        print(new_string)
    string = input()
