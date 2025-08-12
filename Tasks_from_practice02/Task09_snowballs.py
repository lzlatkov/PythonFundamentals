snowballs = int(input())
snowball_value = 0
for snowball in range(snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_value = int(weight / time_needed) ** quality
    if current_value > snowball_value:
        max_weight = weight
        max_time = time_needed
        max_quality = quality
        snowball_value = current_value
print(f"{max_weight} : {max_time} = {snowball_value} ({max_quality})")