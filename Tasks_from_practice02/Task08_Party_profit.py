group_members = int(input())
days = int(input())
total_coins = 0
coins_spend = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        group_members -= 2
    if day % 15 == 0:
        group_members += 5
    if day % 3 == 0:
        coins_spend += 3 * group_members
    if day % 5 == 0:
        total_coins += 20 * group_members
        if day % 3 == 0:
            coins_spend += 2 * group_members
    total_coins += 50
    coins_spend += 2 * group_members
print(f'{group_members} companions received {int((total_coins - coins_spend) / group_members)} coins each.')