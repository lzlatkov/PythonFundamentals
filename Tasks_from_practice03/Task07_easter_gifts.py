gifts_string = input().split()
index_in_valid = True
modified_list = []

while True:
    command = input().split()
    if command[0] == "No" and command[1] == "Money":
        break
    elif command[0] == "OutOfStock":
        if command[1] not in gifts_string:
            continue
        for index in gifts_string:
            if index == command[1]:
                modified_list.append("None")
                continue
            modified_list.append(index)
        gifts_string.clear()
        gifts_string = modified_list.copy()
    elif command[0] == "Required":
        if 0 <= int(command[2]) <= (len(gifts_string) - 1):
            gifts_string[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts_string[len(gifts_string) -1] = command[1]

for element in gifts_string:
    if element == "None":
        gifts_string.remove("None")

for element in gifts_string:
    print(element, end=" ")

