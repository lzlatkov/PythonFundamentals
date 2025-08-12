ticket_price = 150

items_with_prices = input().split("|")
budget = float(input())
bought_items_list = []
new_price_list = []
bought_items_sum = 0
new_price_sum = 0

for element in items_with_prices:
    element_list = element.split("->")
    element_price = float(element_list[1])
    if element_list[0] == "Clothes":
        if element_price <= 50.00 and element_price <= budget:
            budget -= element_price
            bought_items_list.append(element_price)
    elif element_list[0] == "Shoes":
        if element_price <= 35.00 and element_price <= budget:
            budget -= element_price
            bought_items_list.append(element_price)
    elif element_list[0] == "Accessories":
        if element_price <= 20.50 and element_price <= budget:
            budget -= element_price
            bought_items_list.append(element_price)

for num in bought_items_list:
    bought_items_sum += num
    new_price = num + (num * 0.4)
    new_price_list.append(new_price)

for num in new_price_list:
    new_price_sum += num

for element in new_price_list:
    print(f'{element:.2f}', end=" ")

print()
print(f"Profit: {(new_price_sum - bought_items_sum):.2f}")
new_budget = budget + new_price_sum
if new_budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")




# def check_elements(max_price):
#     if int(element_list[1]) <= max_price and int(element_list[1]) <= budget:
#         element_list.append(bought_items_list)