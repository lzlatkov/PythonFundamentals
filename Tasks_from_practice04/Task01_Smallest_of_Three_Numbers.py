# https://pastebin.com/srteuV78


first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_number(some_list: list) -> int:
    return min(some_list)


my_list = [first_number, second_number, third_number]
print(smallest_number(my_list))