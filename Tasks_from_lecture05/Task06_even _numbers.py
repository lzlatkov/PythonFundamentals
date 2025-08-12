numbers_as_int = list(map(int, input().split(", ")))
even_nums_found = map(lambda x: x if numbers_as_int[x] % 2 == 0 else 'no', range(len(numbers_as_int)))
even_numbers = list(filter(lambda a: a != 'no', even_nums_found))
print(even_numbers)