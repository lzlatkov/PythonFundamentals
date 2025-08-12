number = input().split()
rounded_numbers_list = []

for num in number:
    converted_number = float(num)
    rounded_numbers_list.append(round(converted_number))
print(rounded_numbers_list)
