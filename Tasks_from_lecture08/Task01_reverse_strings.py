some_text = input()

while some_text != "end":
    reversed_text = some_text[::-1]
    print(f"{some_text} = {reversed_text}")
    some_text = input()