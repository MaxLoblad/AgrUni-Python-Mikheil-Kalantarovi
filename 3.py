def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("მაგალითი 1:")
print(f"LCM of 1000 and 400 is {lcm(1000, 400)}")

print("მაგალითი 2:")
print(f"LCM of 10000 and 17 is {lcm(500, 50)}")


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
        result = lcm(a, b)
        break

print(f"LCM of {a} and {b} is {result}")
