# Opdracht 16

def even_nummer_zoeken(y):
    even_lijst = [i for i in range(1, y+1) if i % 2 == 0]
    return even_lijst

print(even_nummer_zoeken(8)) # [2, 4, 6, 8]
print(even_nummer_zoeken(4)) # [2, 4]
print(even_nummer_zoeken(2)) # [2]