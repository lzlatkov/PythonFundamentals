def sum_numbers(first: int, second: int) -> int:
    result = first + second
    return result


def subtract(first: int, second: int, third: int) -> int:
    subtract_result = (first + second) - third
    return subtract_result


def add_and_subtract(first: int, second: int, third: int) -> int:
    result2 = first + second
    final_result = result2 - third
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
