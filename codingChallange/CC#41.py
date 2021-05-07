heroHealt = 200
numberOfVillians = 5
healthOfVillians = [54, 23, 65, 87, 12]

healthOfVillians.sort()
counter = 0
for i in healthOfVillians:
    if(heroHealt > i):
        heroHealt -= i
        counter += 1
    else:
        break
print(counter)