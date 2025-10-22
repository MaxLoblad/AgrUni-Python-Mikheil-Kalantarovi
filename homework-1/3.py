
n = int(input("Enter natural number not greater than 100: "))
i = 1
fibonacci = [0, 1]
while i < n-1:
    fibonacci.append(fibonacci[i-1] + fibonacci[i])
    i = i + 1
print(fibonacci)