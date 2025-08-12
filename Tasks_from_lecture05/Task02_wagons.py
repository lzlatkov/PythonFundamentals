wagons = [0] * int(input())

train = []

while True:
    user_input = input().split()
    if user_input[0] == "End":
        print(wagons)
        break

    elif user_input[0] == "add":
        people = int(user_input[1])
        wagons[-1] += people

    elif user_input[0] == "insert":
        index = int(user_input[1])
        people = int(user_input[2])
        wagons[index] += people

    elif user_input[0] == "leave":
        index = int(user_input[1])
        people = int(user_input[2])
        wagons[index] -= people



