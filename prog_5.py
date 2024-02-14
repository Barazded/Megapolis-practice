import csv
import string
file = open("space.txt", "r")
ships = list(csv.DictReader(file, delimiter="*", quotechar='"'))
#LOСА-302
def gen_hash(name: str):
    alph = "ЯЧСМИТЬБЮЁЭЖДЛОРПАВЫФЙЦУКЕНГШЩЗХЪ" + string.ascii_uppercase + string.digits
    d = dict()
    for i in range(len(alph)):
        d[alph[i]] = (i+1)
    hash = 0
    m = 10**9 +9
    p = len(alph)
    step = 1
    for e in name:
        hash += (d[e]*step) % m
        step = step*p
    return int(hash)
def getShips(planet: str):
    mas = []
    for ship in ships:
        if ship["planet"] == planet:
            mas.append(ship)
    return mas
currPlanet = input("Введите планету: ")
findShips = getShips(currPlanet)
count = 1
for ship in findShips:
    if count > 10: exit()
    name = ship["ShipName"]
    hash = gen_hash(name.replace("-",""))
    print(f"{currPlanet}: ({hash}, {name})")
    count+=1