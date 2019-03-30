salaries = [
    {"name" : "Huy",
    "role" : "waiter",
    "hours" : 12,
    "salary/hour($)" : 0.8},

    {"name" : "Tung",
    "role" : "cook",
    "hours" : 24,
    "salary/hour($)" : 1.5},

    {"name" : "M.Duc",
    "role" : "manager",
    "hours" : 20,
    "salary/hour($)" : 2}

]

# print(salaries[2])

p1 = {
    "name" : "Huyen",
    "role" : "waitress",
    "hours" : "14",
    "salary/hour($)" : 1

}

# salaries[0] = p1

# for i in salaries:
#     print(i)

# salaries.pop(2)
# print(salaries)
total = 0
for i in salaries:
    monthly = i["hours"] * i["salary/hour($)"] * 30
    print("the salary of ", i["name"], " per month is: $", int(monthly))
    total += int(monthly)

print("the total salaries that the company should pay is: $", total)
