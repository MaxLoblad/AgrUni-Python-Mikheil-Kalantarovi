
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

a = 3
print(is_prime(a))
a = 5
print(is_prime(a))
a = 0
print(is_prime(a))
a = 27
print(is_prime(a))
a = 91
print(is_prime(a))
a = 101
print(is_prime(a))
