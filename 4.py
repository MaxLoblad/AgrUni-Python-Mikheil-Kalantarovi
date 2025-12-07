from functools import reduce

sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."

#1
words = sentence.replace(".", "").split()
print(words)
print('')

#2
lowerCase = list(map(lambda w: w.lower(), words))
print(lowerCase)
print('')

#3
wordCount= reduce(
    lambda acc, w: {**acc, w: acc.get(w, 0) + 1},
    lowerCase,
    {}
)
print(wordCount)
print('')

#4
mostCommon = max(wordCount.items(), key=lambda x: x[1])
print("Most frequent word:", mostCommon)
print('')

#5
longWords = list(filter(lambda w: len(w) > 3, lowerCase))
print(longWords)
print('')

