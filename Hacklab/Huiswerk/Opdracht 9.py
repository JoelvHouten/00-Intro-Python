# Opdracht 9

def xo(tekst):
    tekst = tekst.lower()
    return tekst.count('x') == tekst.count('o')

print(xo("ooxx")) # True
print(xo("xooxx")) # False
print(xo("ooxXm")) # True
print(xo("zpzpzpp")) # True
print(xo("zzoo")) # False