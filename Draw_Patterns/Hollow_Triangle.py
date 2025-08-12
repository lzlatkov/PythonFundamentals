num1, num2 = int(input()), int(input())
for i in range(num1):
    for j in range(num2):
        print('*' if i in [j, num1-1] or j == 0 else ' ', end='')
    print()