
str1 = input('Enter word n1: ')
str2 = input('Enter word n2: ')

str1 = sorted(str1.lower())
str2 = sorted(str2.lower())

if str1 == str2:
    print('YES')
else:
    print('NO')