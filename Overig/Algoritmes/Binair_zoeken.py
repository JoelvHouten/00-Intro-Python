# Binair Zoeken (bineair - tweedelig of in tweeen gedeeld omdat het altijd de middelste index vind)

def binaire_zoek(lijst, doel):
    laag, hoog = 0, len(lijst) - 1
    while laag <= hoog:
        midden = (laag + hoog) // 2
        if lijst[midden] == doel:
            return midden
        elif lijst[midden] < doel:
            laag = midden + 1
        else:
            hoog = midden - 1
    return None

lijst = [10, 20, 25, 30, 35, 40, 50]
doel = 30
resultaat = binaire_zoek(lijst, doel)
print(resultaat)
