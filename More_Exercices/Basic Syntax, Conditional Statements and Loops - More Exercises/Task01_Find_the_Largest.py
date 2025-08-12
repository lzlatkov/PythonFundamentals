number = int(input())
number = str(number)

sorted_digits = sorted(number, reverse=True)
largest_number_str = ''.join(sorted_digits)
largest_number = int(largest_number_str)
print(largest_number)