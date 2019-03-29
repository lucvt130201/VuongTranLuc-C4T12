import random

count_point = 0

while True:

    a = random.randint(0, 100)
    b = random.randint(0, 100)

    op = random.choice(["+", "-"])

    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b


    err = random.choice([-1, 0, 1])
    display_err = err + c
    print(a, op, b ,"=", display_err)
    answer = input("True or False: ")
    if err == 0:
        if answer == "True":
            print("correct")
            count_point += 1
            print(count_point)
        else:
            break

    else:
        if answer =="False":
            print("correct")
            count_point += 1
            print(count_point)
        else:
            break




