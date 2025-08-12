total_energy = float(input())
artefact_counter = 0
mountain_counter = 0
result = ""

while True:
    terrain = input()
    if terrain == "Journey ends here!":
        if artefact_counter < 3:
            result = f"The character could not find all the pieces and needs {3 - artefact_counter} more to complete the legendary artifact."
        break
    if terrain == "mountain":
        total_energy -= 10
        mountain_counter += 1
        if mountain_counter % 3 == 0:
            artefact_counter += 1
        if artefact_counter == 3:
            result = f"The character reached the legendary artifact with {total_energy:.2f} energy left."
            break
    elif terrain == "desert":
        total_energy -= 15
    elif terrain == "forest":
        total_energy += 7
    if total_energy <= 0:
        result = "The character is too exhausted to carry on with the journey."
        break

print(result)