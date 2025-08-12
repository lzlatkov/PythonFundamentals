number = int(input())
numbers_list = []
filtered_list = []

for num in range(number):
    user_input = int(input())
    numbers_list.append(user_input)

type = input()
if type == 'even':
    for num in numbers_list:
        if num % 2 == 0:
            filtered_list.append(num)
elif type == 'odd':
    for num in numbers_list:
        if num % 2 != 0:
            numbers_list.append(num)
elif type == 'positive':
    for num in numbers_list:
        if num >= 0:
            numbers_list.append(num)
elif type == 'negative':
    for num in numbers_list:
        if num < 0:
            numbers_list.append(num)

print(filtered_list)