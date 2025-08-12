numbers = list(map(int, input().split(", ")))

POSITIVE_NUMBERS = [str(num) for num in numbers if num >= 0]
NEGATIVE_NUMBERS = [str(num) for num in numbers if num < 0]
EVEN_NUMBERS = [str(num) for num in numbers if num % 2 == 0]
ODD_NUMBERS = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(POSITIVE_NUMBERS)}")
print(f"Negative: {', '.join(NEGATIVE_NUMBERS)}")
print(f"Even: {', '.join(EVEN_NUMBERS)}")
print(f"Odd: {', '.join(ODD_NUMBERS)}")