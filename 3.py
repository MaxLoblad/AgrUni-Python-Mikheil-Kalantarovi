from functools import reduce

products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]

#1
available_products = list(filter(lambda p: p[2] > 0, products))
print("Available products:")
for p in available_products:
    print(p)

#2
total_prices = list(map(lambda p: (p[0], round(p[1] * p[2],4)), available_products))
print("\nTotal price per product:")
for t in total_prices:
    print(t)

#3
grand_total = reduce(lambda acc, p: acc + p[1], total_prices, 0)
print("\nGrand total price of all available products:", grand_total)
