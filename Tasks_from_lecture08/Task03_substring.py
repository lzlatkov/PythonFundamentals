string = input()
second_string = input()
result = ""

while string in second_string:
    second_string = second_string.replace(string, "")
print(second_string)
