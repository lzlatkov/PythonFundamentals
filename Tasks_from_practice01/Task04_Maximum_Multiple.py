divisor = int(input())
current_largest_number = 0
largest_number = 0
boundary = int(input())

for num in range(1, boundary + 1):
    if num % divisor == 0 and boundary >= num > 0:
        current_largest_number = num
        if num > current_largest_number:
            current_largest_number = num
print(num)
#####################################################
divisor = int(input())
boundary = int(input())

for num in range(boundary, divisor - 1, -1): 
    if num % divisor == 0 and boundary >= num > 0:
        print(num)
        break