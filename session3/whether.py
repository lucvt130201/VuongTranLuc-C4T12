from random import randint
t = randint(0,100)
print("temperature is:", t)
if t < 30:
    print("Raniny")
elif t < 60:
    print("cloudy")
else:
    print("sunny")   