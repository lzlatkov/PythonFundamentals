words = input().split()
palindrome = input()

palindrome_list = [word for word in words if word[::-1] == word]
palindrome_counter = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {palindrome_counter} times')