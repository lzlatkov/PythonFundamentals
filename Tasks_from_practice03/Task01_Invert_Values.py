string = input().split()

opposite_list = []
for number in string:
    opposite_number = -int(number)
    opposite_list.append(opposite_number)


print(opposite_list)