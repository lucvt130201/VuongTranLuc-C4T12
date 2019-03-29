from datetime import date
year = int(input("Your year: "))
month = int(input("Your month: "))
if month > 0 and  month  < 13:
    days = (date(year, month + 1, 1) - date(year, month, 1)).days
    print(days)
else:
    print("Your month should betwen 1 - 12")
    