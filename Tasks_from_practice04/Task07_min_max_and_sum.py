def min_max_and_sum(my_list)-> list:
    filtered_list = []
    for num in my_list:
        num = int(num)
        filtered_list.append(num)
        min_number = min(filtered_list)
        max_number = max(filtered_list)
        sum_numbers = sum(filtered_list)
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}"


user_numbers = input().split()
print(min_max_and_sum(user_numbers))