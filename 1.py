
word = 'azcbobobegghakl'

word = sorted(word)
j = 0
sym = 'a'
longest = 0
for i in range(len(word)):
    if word[i-1] == word[i]:
        j = j + 1
    else:
        if j >= longest:
            sym = word[i-1]
            longest = j + 1
        j = 0
longestWord = sym * longest
print(word, '\n', longestWord)