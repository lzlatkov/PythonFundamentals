coffee_price = 1.5
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00


def price_calculation(product: str, qty: int) -> int:
    total_price = 0
    if product == "coffee":
        total_price = coffee_price * quantity
    elif product == "coke":
        total_price = coke_price * quantity
    elif product == "water":
        total_price = water_price * quantity
    elif product == "snacks":
        total_price = snacks_price * quantity
    return total_price

product = input()
quantity = int(input())

print(f'{price_calculation(product,quantity):.2f}')
