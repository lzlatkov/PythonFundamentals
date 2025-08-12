def sorted_numbers(my_list) ->list:
    return list(my_list)


numbers = input().split()
numbers_as_int = []
for number in numbers:
    numbers_as_int.append(int(number))

result = (sorted_numbers(sorted(numbers_as_int)))
print(result)