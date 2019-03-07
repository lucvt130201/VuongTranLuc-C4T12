count = 0
a = int(input('Your number: '))
while a > 0:
    a = a // 10
    count += 1

print("number of digit is: ", count)