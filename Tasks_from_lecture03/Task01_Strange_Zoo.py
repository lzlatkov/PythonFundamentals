string_one_tail = input()
string_two_body = input()
string_three_head = input()

my_list = [string_one_tail, string_two_body, string_three_head]

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)