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

for i in salaries:
    print(i)

new_1 = {
    "name" : "Don",
    "role" : "waiter",
    "hours" : 12,
    "salary/hour($)" :  0.9
}

new_2 = {
    "name" : "H.Duc",
    "role" : "waiter",
    "hours" : 14,
    "salary/hour($)" :  0.7
}

salaries.append(new_1)
salaries.append(new_2)

print("UPDATE")
for i in salaries:
    print(i)