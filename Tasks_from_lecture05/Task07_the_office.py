def check_employee_happiness(employees_happiness_index, happiness_factor: int) -> list:
    current_happiness = [happiness_factor * current_value for current_value in employees_happiness_index]
    average_happiness = sum(current_happiness) / len(current_happiness)
    happy_count = sum(num >= average_happiness for num in current_happiness)
    total_count = len(current_happiness)
    message = 'happy' if happy_count >= total_count / 2 else 'not happy'

    return f"Score: {happy_count}/{total_count}. Employees are {message}!"


employees_happiness_index = list(map(int, input().split()))
factor = int(input())
result = check_employee_happiness(employees_happiness_index, factor)
print(result)