stock = input().split()
stock_dict = {}

for element in range(0, len(stock), 2):
    product = stock[element]
    quantity = stock[element + 1]
    stock_dict[product] = int(quantity)

searched_product = input().split()

for element in searched_product:
    if element in stock_dict:
        print(f'We have {stock_dict[element]} of {element} left')
    else:
        print(f"Sorry, we don't have {element}")