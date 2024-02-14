import csv
file = open("space.txt", "r")
ships = list(csv.DictReader(file, delimiter="*", quotechar='"'))
def findShipByName(name: str):
    '''
    метод линейного поиска кораблей по названию
    name - имя корабля
    '''
    for ship in ships:
        nameCurrShip = ship["ShipName"]
        if name == nameCurrShip:
            return ship
    return None
reqest = ""
while True:
    reqest = input()
    if reqest == "stop": exit()
    find = findShipByName(reqest)
    if not find is None:
        name = find["ShipName"]
        planet = find["planet"]
        vec = find["direction"]
        print(f"Корабль {name} был отправлен с планеты: {planet}"
              + f" и его направление движения было: {vec}")
    else:
        print("error.. er.. ror..")