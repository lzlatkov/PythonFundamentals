number = int(input())
searched_word = input()
word_list = []
searched_word_list = []

for word in range(number):
    some_word = input()
    word_list.append(some_word)
    if searched_word in some_word:
        searched_word_list.append(some_word)

print(word_list)
print(searched_word_list)