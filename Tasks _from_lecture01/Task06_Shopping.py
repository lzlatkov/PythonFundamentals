budget = int(input())
product_sum = 0

while True:
    product_price = input()
    if product_price == "End":
        print(f"You bought everything needed.")
        break
    product_price = int(product_price)
    product_sum += product_price
    if product_sum > budget:
        print(f"You went in overdraft!")
        break
