user_string = input().split(", ")
count_of_beggars = int(input())
money_as_integer = []

for money in user_string:
    money_as_integer.append(int(money))
final_list = []
start_index = 0
for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integer), count_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    final_list.append(current_beggar_sum)
    start_index += 1
print(final_list)