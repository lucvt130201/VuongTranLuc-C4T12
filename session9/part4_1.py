numbers = [5, 1, 8, 92, 7, 30]

even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("all even numbers are: ")
print(*even_numbers, sep = ", ")
