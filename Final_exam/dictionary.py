user_input = input().split(" | ")
word_dictionary = {}


for element in user_input:
    word, definition = element.split(": ")
    if word not in word_dictionary:
        word_dictionary[word] = []
    word_dictionary[word].append(definition)

test_words = input().split(" | ")
command = input()
if command == "Test":
    for test_word in test_words:
        if test_word in word_dictionary:
            definitions_list = word_dictionary.get(test_word)
            print(f"{test_word}:")
            for word_definition in definitions_list:
                print(f" -{word_definition}")

elif command == "Hand Over":
    for word in word_dictionary.keys():
        print(f"{word}", end=" ")