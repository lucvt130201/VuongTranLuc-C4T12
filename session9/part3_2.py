# not use sum()
numbers = [5, 1, 8, 92, -1, 30]
total = 0

for i in numbers:
    total += i

print("The sum of all the numbers in the list is: ", total)

# use sum:
total2 = sum(numbers)
print("the sum of all the numbers in the list using sum() method is:", total2)