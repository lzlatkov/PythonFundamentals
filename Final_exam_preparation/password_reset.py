some_string = input()
split_list = []
new_raw_password = ""
cut_password = ""
substitute_sting = ""
command = ''

while command != "Done":
    command = input()
    split_list = command.split()
    if command == "TakeOdd":
        for index in range(len(some_string)):
            if index % 2 != 0:
                new_raw_password += some_string[index]
        some_string = new_raw_password
        print(some_string)
    elif split_list[0] == "Cut":
        substring = some_string[int(split_list[1]):int(split_list[1]) + int(split_list[2])]
        cut_password = some_string.replace(substring, "", 1)
        some_string = cut_password
        print(some_string)
    elif split_list[0] == "Substitute":
        if split_list[1] in some_string:
            substitute_sting = some_string.replace(split_list[1], split_list[2])
            some_string = substitute_sting
            print(some_string)
        else:
            print("Nothing to replace!")

print(f'Your password is: {some_string}')