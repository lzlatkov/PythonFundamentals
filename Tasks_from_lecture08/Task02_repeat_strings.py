string = input().split()
requested_output = ""

for i in string:
    requested_output += i * len(i)
print(requested_output)