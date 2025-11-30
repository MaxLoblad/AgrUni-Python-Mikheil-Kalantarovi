
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



print("მაგალითი 1:")
print(f"GCD of 1000 and 400 is {gcd(1000, 400)}")

print("მაგალითი 2:")
print(f"GCD of 10000 and 17 is {gcd(10000, 17)}")


while True:
    z = 1
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        if a < 1 or b < 1:
            print("Error: numbers must be >= 1.")
            z = 0
        if a > 10000 or b > 10000:
            print("Error: numbers must be <= 10000.")
            z = 0
    except ValueError:
        print("Error: numbers must be integers.")
        z = 0

    if z == 1:
        result = gcd(int(a), int(b))
        break

print(f"GCD of {a} and {b} is {result}")