num1, num2 = int(input()), int(input())

for i in range(num1):
    for j in range(num2):
        print('*' if i in [0, num1-1] or j in [0, num2-1] else ' ', end='')
    print()