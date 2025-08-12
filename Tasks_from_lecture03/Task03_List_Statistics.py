number_count = int(input())
positive_numbers_list = []
negative_numbers_list = []

for num in range(number_count):
    number = int(input())
    if number >= 0:
        positive_numbers_list.append(number)
    else:
        negative_numbers_list.append(number)

print(positive_numbers_list)
print(negative_numbers_list)
print(f'Count of positives: {len(positive_numbers_list)}')
print(f'Sum of negatives: {sum(negative_numbers_list)}')