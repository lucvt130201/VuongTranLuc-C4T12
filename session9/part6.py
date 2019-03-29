districts = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = [150300, 247100, 333300, 266800, 420900,318000]
area = [11743, 9.224, 45.35, 12.04, 9.96, 10.09]

density = []
for p,a in zip(population, area):
    d = p/a
    density.append(d)

for i, p in zip(districts, density):
    print(i, ":", " ", round(p,2))

MDTB = sum(density)/len(districts)
print("MBTB is: ", round(MDTB, 2))