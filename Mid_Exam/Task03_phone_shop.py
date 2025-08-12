phones_list = input().split(", ")

while True:
    command = input().split(" - ")
    if command[0] == "End":
        print(", ".join(phones_list))
        break
    elif command[0] == "Add":
        if command[1] not in phones_list:
            phones_list.append(command[1])
    elif command[0] == "Remove":
        if command[1] in phones_list:
            phones_list.remove(command[1])
    elif command[0] == "Bonus phone":
        filtered_phone_list = command[1].split(":")
        if filtered_phone_list[0] in phones_list:
            old_phone = filtered_phone_list[0]
            new_phone = filtered_phone_list[1]
            phones_list.insert((phones_list.index(old_phone)) + 1, new_phone)
    elif command[0] == "Last":
        if command[1] in phones_list:
            phones_list.remove(command[1])
            phones_list.insert(len(phones_list), command[1])