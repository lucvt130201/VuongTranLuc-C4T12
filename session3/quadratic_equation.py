

print("ax^2 + bx + c = 0")
a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))

delta = b**2 - 4*a*c


if a == 0:
    print("x =", -c/b)
else:
    x1 = (-b + (delta*0.5)/(2*a))
    x2 = (-b - (delta*0.5)/(2*a))
    if delta < 0:
        print("no solution")
    elif delta == 0:
        print("x1 = x2 =", (-b)/(2*a))
    else:
        print("solution of equation is: ")
        print(x1)
        print(x2)    