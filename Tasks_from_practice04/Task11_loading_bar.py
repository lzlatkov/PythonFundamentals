def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loading_number = number // 10
    return f"{number}% [{'%'* loading_number}{'.' * (10 - loading_number)}]\nStill loading..."


user_number = int(input())
print(loading_bar(user_number))