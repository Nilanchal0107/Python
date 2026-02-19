user_word = input("Enter a word: ")
user_word = user_word.upper()

n = len(user_word)

for i in range(n):
    if user_word[i] in ('A','I','E','O','U'):
      continue
    else:
        print(user_word[i], end = "")
print("")