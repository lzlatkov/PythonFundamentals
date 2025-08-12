capacity = 255
user_input = int(input())

for liters in range(0, user_input):
    added_liters = int(input())

    if capacity - added_liters < 0:
        print(f'Insufficient capacity!')
        continue
    capacity -= added_liters
print(f'{255 - capacity}')