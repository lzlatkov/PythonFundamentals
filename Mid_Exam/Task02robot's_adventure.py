items_in_each_city = input().split("|")
items_as_integers = [int(number) for number in items_in_each_city]
collected_items = 0

while True:
    command = input().split(" ")
    if command[0] == "Adventure":
        break
    if command[0] == "Double":
        if int(command[1]) > len(items_as_integers) - 1:
            continue
        items_as_integers[int(command[1])] *= 2
    if command[0] == "Switch":
        items_as_integers.reverse()
    if command[0] == "Step":
        step_direction = command[1].split("$")
        start_index = int(step_direction[1])
        steps = int(step_direction[2])
        if start_index > len(items_as_integers) - 1:
            continue
        if step_direction[0] == "Backward":
            landing_index = (start_index - steps) % len(items_as_integers)
            collected_items += items_as_integers[landing_index]
            items_as_integers[landing_index] = 0
        elif step_direction[0] == "Forward":
            landing_index = (start_index + steps) % len(items_as_integers)
            collected_items += items_as_integers[landing_index]
            items_as_integers[landing_index] = 0

print(" - ".join(map(str, items_as_integers)))
print(f"Robo finished the adventure with {collected_items} items!")

