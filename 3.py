import json
from collections import defaultdict


max_single_purchase_amount = 0
users_max_single_amount = []

user_total_spent = defaultdict(float)
user_total_amount = defaultdict(int)
product_total_amount = defaultdict(int)

total_purchase_values = []
total_purchase_amounts = []


with open("D:/Users/mistik/Desktop/data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        user, product, amount, price = line.split(",")

        amount = int(amount)
        price = float(price)

        purchase_value = amount * price

        #a
        if amount > max_single_purchase_amount:
            max_single_purchase_amount = amount
            users_max_single_amount = [user]
        elif amount == max_single_purchase_amount:
            users_max_single_amount.append(user)

        #b
        user_total_spent[user] += purchase_value

        #d
        user_total_amount[user] += amount

        #e
        product_total_amount[product] += amount

        total_purchase_values.append(purchase_value)
        total_purchase_amounts.append(amount)

#b
max_total_spent = max(user_total_spent.values())
users_max_total_spent = [
    user for user, value in user_total_spent.items()
    if value == max_total_spent
]

#c
average_purchase_value = sum(total_purchase_values) / len(total_purchase_values)

#d
average_purchase_amount = sum(total_purchase_amounts) / len(total_purchase_amounts)

#e
max_product_amount = max(product_total_amount.values())
most_sold_products = [
    product for product, amt in product_total_amount.items()
    if amt == max_product_amount
]

stats = {
    "max_single_purchase_amount": {
        "amount": max_single_purchase_amount,
        "users": users_max_single_amount
    },
    "max_total_spent": {
        "value": max_total_spent,
        "users": users_max_total_spent
    },
    "average_purchase_value": average_purchase_value,
    "average_purchase_amount": average_purchase_amount,
    "most_sold_products": {
        "amount": max_product_amount,
        "products": most_sold_products
    }
}

with open("stats.json", "w", encoding="utf-8") as json_file:
    json.dump(stats, json_file, indent=4, ensure_ascii=False)
