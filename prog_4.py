import csv
import random
file = open("space.txt", "r")
ships = list(csv.DictReader(file, delimiter="*", quotechar='"'))
def gen_password(nameShip: str ,planet: str):
    password = ""
    codeShip = nameShip.split("-")[0]
    mid = len(codeShip)//2
    password = (planet[-1]+planet[-2]+planet[-3])[::-1] #название планеты
    password = password + codeShip[mid] + codeShip[mid-1] #код корабля
    password = password + (planet[0]+planet[1]+planet[2])[::-1]
    return password.upper()
filenew = open("space_uniq_password.csv", "w")
filenew.write("ShipName*planet*coord_place*direction*password\n")
for ship in ships:
    name = ship["ShipName"]
    planet = ship["planet"]
    coords = ship["coord_place"]
    vec = ship["direction"]
    password = gen_password(name, planet)
    filenew.write(f"{name}*{planet}*{coords}*{vec}*{password}\n")