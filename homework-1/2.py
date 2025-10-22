
number = int(input("Enter natural number not greater than 1000: "))
i = 0
while i < number:
    i=i+1
    if (number % i) == 0:
        print(i, end=" ")
