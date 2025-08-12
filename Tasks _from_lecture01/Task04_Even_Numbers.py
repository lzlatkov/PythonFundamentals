number = int(input())

for i in range(1, number + 1):
    user_number_input = int(input())
    if user_number_input % 2 != 0:
        print(f"{user_number_input} is odd!")
        break
else:
    print("All numbers are even.")


############################################################33
n = int(input())

for i in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        break
    else:
        print(f"All numbers are even.")
        break