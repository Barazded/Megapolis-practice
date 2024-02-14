import csv
file = open("space.txt", "r")
ships = list(csv.DictReader(file, delimiter="*", quotechar='"'))
def my_sort(mas):
    for i in range(len(mas)):
        for j in range(len(mas)-i-1):
            val1 = int(mas[i]["ShipName"].split("-")[1])
            val2 = int(mas[j]["ShipName"].split("-")[1])
            if val2 > val1:
                mas[j],mas[i] = mas[i],mas[j]
    return mas
sortships = my_sort(ships)
count = 1
for element in sortships:
    if count > 10: exit()
    print(element["ShipName"])
    count += 1