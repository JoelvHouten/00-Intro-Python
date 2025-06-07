# Opdracht 18

def char_index(zin, letter):
    indexen = [i for i, l in enumerate(zin) if l == letter]
    if not indexen:
        print(None)
    else:
        print([indexen[0], indexen[-1]])

char_index("hello", "l") # [2, 3]
char_index("circumlocution", "c") # [0, 8]
char_index("happy", "h") # [0, 0]
char_index("happy", "e") # None