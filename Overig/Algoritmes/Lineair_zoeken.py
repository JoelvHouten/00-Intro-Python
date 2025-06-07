# Lineair zoeken geeft index in de lijst terug (lineair - in een rechte lijn van begin to eind)

def lineair_zoeken_index(lijst, doel_index):
    for i in range(len(lijst)):
        if lijst[i] == doel_index:
            return i
    return None

# Lineair zoeken geeft waarde in de lijst terug

def lineair_zoeken_item(lijst, doel_item):
    for item in lijst:
        if item == doel_item:
            return item
    return None

lijst = [10, 20, 40, 30, 50]
print(lijst)

doel_index = 30
resultaat_index = lineair_zoeken_index(lijst, doel_index)
print(f"De waarde staat in de lijst op index: {resultaat_index}")

doel_item = 30
resultaat_item = lineair_zoeken_item(lijst, doel_item)
print(f"De waarde {resultaat_item} komt voor in de lijst.")