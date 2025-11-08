
year = input('Enter a year: ')

while True:
    try:
        year_value = int(year)
        i = 0
    except ValueError:
        year = input('Enter a valid year: ')
        i = 1
    if  i == 0:
        break

if int(year) % 400 == 0:
    print (year,'is a leap year')
elif int(year) % 4 == 0 and int(year) % 100 != 0 :
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

