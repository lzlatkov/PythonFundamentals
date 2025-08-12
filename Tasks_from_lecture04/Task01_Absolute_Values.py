numbers = input().split()
final_list = []

for number in numbers:
    number_abs = abs(float(number))
    final_list.append(number_abs)

print(final_list)

#####################################################


numbers_list = []
numbers = list(map(float, input().split()))
for num in numbers:
    numbers_list.append(abs(num))

print(numbers_list)