budget = float(input())
flour_kg_price = float(input())
eggs_pack_price = flour_kg_price * 0.75
milk_price = flour_kg_price * 1.25 / 4
#needed_milk_price = milk_price * 0.25
price_for_one_loaf = flour_kg_price + eggs_pack_price + milk_price
loaves_count = 0
colored_eggs_count = 0
while budget >= price_for_one_loaf:
    budget -= price_for_one_loaf
    loaves_count += 1
    colored_eggs_count += 3
    if loaves_count % 3 == 0:
        colored_eggs_count -= (loaves_count - 2)
print(f'You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')