def even_numbers(my_list) ->list:
    filtered_list = []
    for element in numbers_list:
        element = int(element)
        if element % 2 == 0:
            filtered_list.append(element)
    return filtered_list


numbers_list = input().split()
print(even_numbers(numbers_list))
