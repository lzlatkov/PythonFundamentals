numbers_as_string = input().split()

numbers_as_int = []
for number in numbers_as_string:
    numbers_as_int.append(int(number))

count_of_numbers_to_remove = int(input())
for _ in range(count_of_numbers_to_remove):
    numbers_as_int.remove(min(numbers_as_int))

print(numbers_as_int, sep=", ")
