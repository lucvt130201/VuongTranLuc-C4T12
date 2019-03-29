districts = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = [150300, 247100, 333300, 266800, 420900,318000]

most = max(population)
least = min(population)

count_max = 0
count_min = 0

# find max
for i in population:
    count_max += 1
    if most == i:
        break

district_max = districts[count_max - 1]

# find min
for i in population:
    count_min += 1
    if least == i:
        break

district_min = districts[count_min - 1]

print(district_max, "has most population: ", most)
print(district_min, "has least population: ", least)
