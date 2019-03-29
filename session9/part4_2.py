ask = input("enter your list of numbers, seperated by ' ': ")

numbers = []

for i in ask.split(' '):
    numbers.append(int(i))

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("All even numbers are: ")
print(*even_numbers, sep = ", ")


