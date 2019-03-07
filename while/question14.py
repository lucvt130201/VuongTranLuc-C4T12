import datetime

currentDT = datetime.datetime.now()
print(str(currentDT))
print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
print (currentDT.strftime("%Y/%m/%d"))
print (currentDT.strftime("%H:%M:%S"))
print (currentDT.strftime("%I:%M:%S %p"))
print (currentDT.strftime("%a, %b %d, %Y"))
print(currentDT.strftime("%A,%Y-%m-%d %H:%M:%S "))

