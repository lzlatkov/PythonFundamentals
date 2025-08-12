ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
decoration = ""
christmas_spirit = 0
money_spend = 0
quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

for day in range(1, days_left_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        money_spend += quantity_of_decorations * ornament_set_price
        christmas_spirit += 5
    if day % 3 == 0:
        money_spend += quantity_of_decorations * (tree_skirt_price +  tree_garland_price)
        christmas_spirit += 13 #3 + 10
    if day % 5 == 0:
        money_spend += quantity_of_decorations * tree_lights_price
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spend += tree_skirt_price + tree_lights_price + tree_garland_price
if days_left_until_christmas % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {money_spend}")
print(f"Total spirit: {christmas_spirit}")




