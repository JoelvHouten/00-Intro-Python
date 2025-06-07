# Opdracht 15

def reverser(tekst):
    omgekeerde_tekst = reversed(tekst)
    resultaat = ""

    for teken in omgekeerde_tekst:
        resultaat += teken.swapcase()

    print(resultaat)

reverser("Hello World") # "DLROw OLLEh"
reverser("ReVeRsE") # "eSrEvEr"
reverser("Radar") # "RADAr"