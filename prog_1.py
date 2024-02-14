import csv
file = open("space.txt", "r")
ships = list(csv.DictReader(file, delimiter="*", quotechar='"'))
def algo(n,m,xd,yd,t):
    x,y = 0,0
    if n > 5:
        x = n + xd
    elif n <= 5:
        x = (n + xd)*4 + t
    if m > 3:
        y = m + yd + t
    elif m <= 3:
        y = -(n+yd)*m
    return x,y
filenew = open("space_new.txt", "w")
filenew.write("ShipName*planet*coord_place*direction\n")
for ship in ships:
    name = ship["ShipName"].split("-")
    coords = ship["coord_place"].split(" ")
    x,y = int(coords[0]),int(coords[1])
    vec = ship["direction"].split(" ")
    planet = ship["planet"]
    fullvec = ship["direction"]
    fullname = ship["ShipName"]
    if x == 0 and y == 0:
        x,y = algo(int(name[1][0]), int(name[1][1]), int(vec[0]), int(vec[1]), len(planet))
    if name[0][-1] == "V":
        print(f"{fullname} - ({x}, {y})")
    filenew.write(f"{fullname}*{planet}*{x} {y}*{fullvec}\n")

