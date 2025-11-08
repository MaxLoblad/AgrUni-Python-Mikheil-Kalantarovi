import random

randomNumbers = []
for i in range(5):
    r = random.randint(1, 4)   #1 <= r <= 10
    randomNumbers.append(r)
print(' List of random numbers: ', randomNumbers)
multipliedList = []
for i in range(5):
    for j in range(randomNumbers[i]):
        multipliedList.append(randomNumbers[i])
print(' List of multiplied numbers: ', multipliedList, '\n', 'Length: ', len(multipliedList))