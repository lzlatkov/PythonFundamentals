def calculation(operator: str, a: int, b: int) -> int:
    result = 0
    if input_operator == "multiply":
        result = num1 * num2
    elif input_operator == "divide":
        result = num1 / num2
    elif input_operator == "add":
        result = num1 + num2
    elif input_operator == "subtract":
        result = num1 - num2
    return result


input_operator = input()
num1 = int(input())
num2 = int(input())
output = int(calculation(input_operator, num1, num2))

print(output)