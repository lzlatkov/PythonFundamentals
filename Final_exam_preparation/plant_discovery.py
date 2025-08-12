plants_count = int(input())
plants = {}

for plant in range(plants_count):
    plant_name, rarity = input().split("<->")
    plants[plant_name] = {"rarity": int(rarity), "rating": []}

while True:
    user_input = input()
    if user_input == "Exhibition":
        break
    command = user_input.split(": ")

    if command[0] == "Rate":
        plant_details = command[1].split(" - ")
        if plant_details[0] in plants:
            plants[plant_details[0]]['rating'].append(int(plant_details[1]))
        else:
            print("error")

    elif command[0] == "Update":
        plant_details = command[1].split(" - ")
        if plant_details[0] in plants:
            plants[plant_details[0]]["rarity"] = int(plant_details[1])
        else:
            print("error")

    elif command[0] == "Reset":
        plant = command[1]
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")

print(f"Plants for the exhibition:")

for plant, plant_info in plants.items():
    average_rating = sum(plant_info["rating"]) / len(plant_info["rating"]) if plant_info["rating"] else 0
    print(f"- {plant}; Rarity: {plant_info['rarity']}; Rating: {average_rating:.2f}")
