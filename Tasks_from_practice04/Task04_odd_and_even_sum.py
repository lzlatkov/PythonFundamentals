def odd_and_even_sum(number) -> int:
    odd_sum = 0
    even_sum = 0
    for element in str(number):
        element = int(element)
        if element % 2 == 0:
            even_sum += element
        else:
            odd_sum += element
    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


num = int(input())
print(odd_and_even_sum(num))
