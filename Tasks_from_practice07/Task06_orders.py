products = {}

while True:
    user_input = input()
    if user_input == "buy":
        break
    name, price, quantity = user_input.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        if products[name]["price"] != price:
            products[name]["price"] = price

for product_name, details in products.items():
    total_price = details["price"] * details["quantity"]
    print(f"{product_name} -> {total_price:.2f}")