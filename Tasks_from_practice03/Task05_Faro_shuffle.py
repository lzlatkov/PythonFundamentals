deck = input().split()
faro_shuffles = int(input())

for shuffle in range(faro_shuffles):
    middle_of_the_deck = len(deck) // 2
    left_part = deck[:middle_of_the_deck]
    right_part = deck[middle_of_the_deck:]
    deck_after_shuffle = []
    for card_index in range(len(left_part)):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    deck = deck_after_shuffle

print(deck)
