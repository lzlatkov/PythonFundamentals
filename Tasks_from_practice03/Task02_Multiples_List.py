factor = int(input())
count = int(input())
count_list = []

for number in range(1, count + 1):
    count_list.append(int(number * factor))

print(count_list)