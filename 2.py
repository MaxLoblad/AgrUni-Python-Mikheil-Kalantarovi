employees = [
    {"name": "Alice", "tasks": [5, 7, 9], "department": "IT"},
    {"name": "Bob", "tasks": [2, 3, 4], "department": "Sales"},
    {"name": "Charlie", "tasks": [8, 7, 6], "department": "IT"},
    {"name": "Diana", "tasks": [9, 8, 10], "department": "Marketing"},
    {"name": "George", "tasks": [2, 7, 6], "department": "IT"}
]

averaged = list(map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "average_tasks": sum(emp["tasks"]) // len(emp["tasks"])
    },
    employees
))

avgIT = list(filter(
    lambda x: x["department"] == "IT" and x["average_tasks"] > 6,
    averaged
))


#1
for item in averaged:
    print(item)
print('\n')

#2
sorted_employees = sorted(averaged, key=lambda x: x["average_tasks"], reverse=True)
for item in sorted_employees:
    print(item)
print('\n')

#3
top_employee = max(averaged, key=lambda x: x["average_tasks"])
print(top_employee,'\n')

#4
print(avgIT,'\n')
