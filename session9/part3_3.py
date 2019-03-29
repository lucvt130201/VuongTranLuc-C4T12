# not using sum()
ask = input("enter a list of numbers, seperated by ' ': ")

numbers = ask.split(" ")

total = 0
for i in numbers:
    
    total += int(i)

print("the sum of your list of numbers is: ", total)

# using sum
total2 = []

for i in numbers:
    total2.append(int(i))

print("the sum without using sum() function is: ", sum(total2))


