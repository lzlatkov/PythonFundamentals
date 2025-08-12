count = int(input())
synonym_dict = {}

for element in range(count):
    word = input()
    synonym = input()
    if word not in synonym_dict:
        synonym_dict[word] = []
    synonym_dict[word].append(synonym)

for word in synonym_dict:
    print(f"{word} - {', '.join(synonym_dict[word])}")