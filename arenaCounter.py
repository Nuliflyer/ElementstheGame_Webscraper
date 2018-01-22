import re
import urllib

def getElement(num):
    elements = {1: "Entropy", 2: "Death", 3: "Gravity", 4: "Earth", 5: "Life", 6: "Fire", 7: "Water", 8: "Light", 9: "Air", 10: "Time", 11: "Darkness", 12: "Aether"}
    return elements.get(num)

def makeUrl(rank, league):
    return "http://www.elementsthegame.com/arena.php?rank=" + str(rank) + "&league=" + str(league)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def countElements(league):
    elements = [0,0,0,0,0,0,0,0,0,0,0,0]
    for j in range(20):
        url = makeUrl(25*j + 1, league)
        f = urllib.urlopen(url)
        data = f.read()
        wordlocs = [m.start() for m in re.finditer('eleico.', data)]
        for i in wordlocs:
            if(is_number(data[i+8])):
                elements[int(data[i+7:i+9]) - 1] += 1
            else:
                elements[int(data[i+7]) - 1] += 1
    return elements

def printElements(elements, ranking):
    for i in range(12):
        print(elements[i], getElement(i+1))


printElements(countElements(1), "Bronze")
printElements(countElements(2), "Silver")
printElements(countElements(3), "Gold")
printElements(countElements(4), "Platinum")
