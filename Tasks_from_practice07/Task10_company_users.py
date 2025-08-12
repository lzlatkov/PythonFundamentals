employee_dictionary = {}

while True:
    company = input()
    if company == "End":
        break
    company_name, employee_id = company.split(" -> ")
    if company_name not in employee_dictionary:
        employee_dictionary[company_name] = []
    if employee_id not in employee_dictionary[company_name]:
        employee_dictionary[company_name].append(employee_id)

for employer, id_ in employee_dictionary.items():
    print(employer)
    for employee in id_:
        print(f"-- {employee}")
