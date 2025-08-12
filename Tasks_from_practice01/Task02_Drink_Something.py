age = int(input())
drink = ""
user = ""

if age <= 14:
    user = 'kid'
    drink = 'toddy'
elif 14 < age <= 18:
    user = 'teen'
    drink = 'coke'
elif 18 < age <= 21:
    user = 'young adult'
    drink = 'beer'
else:
    user = 'adult'
    drink = 'whisky'

print(drink)

