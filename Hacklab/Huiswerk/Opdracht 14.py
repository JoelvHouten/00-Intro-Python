# Opdracht 14

import random

def kopmunt(x):
    kop = random.randint(0, x)
    munt = x - kop

    print(f"Er is {kop} keer kop gegooid")
    print(f"Er is {munt} keer munt gegooid")

kopmunt(int(input("Hoevaak wil je het muntje opgooien?: ")))