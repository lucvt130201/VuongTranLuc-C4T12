m = int(input("nhập m = "))
n = int(input("nhập n ="))
if n<= m:
    print("nhập lại")
else:
    for i in range(n, m+1, -1):
        print(i)
