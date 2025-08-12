lost_battles = int(input())
broken_helmets = 0
broken_swords = 0
broken_shields = 0
broken_armors = 0
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0

broken_helmets = lost_battles // 2
broken_swords = lost_battles // 3
broken_shields = lost_battles // (2 * 3)
broken_armors = broken_shields // 2

total_expenses = broken_helmets * helmet_price \
    + broken_swords * sword_price \
    + broken_shields * shield_price \
    + broken_armors * armor_price

print(f'Gladiator expenses: {total_expenses:.2f} aureus')