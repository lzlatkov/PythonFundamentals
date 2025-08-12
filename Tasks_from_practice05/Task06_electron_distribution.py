number_of_electros = int(input())
shells = []
for shell in range(1, number_of_electros + 1):
    max_electrons = 2 * shell **2
    if number_of_electros >= max_electrons:
        shells.append(max_electrons)
        number_of_electros -= max_electrons
        if number_of_electros == 0:
            break
    else:
        shells.append(number_of_electros)
        break
print(shells)
