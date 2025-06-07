# Opdracht 10

def zin_hamming(woord1, woord2):
    if len(woord1) != len(woord2):
        print("De zinnen zijn niet dezelfde lengte")
        return

    verschil = 0
    for l1, l2 in zip(woord1, woord2):
        if l1 != l2:
            verschil += 1

    print(f"Er zijn {verschil} letters die verschillend zijn in de woorden {woord1} en {woord2}")

zin_hamming("abcde", "bcdef") # 5
zin_hamming("abcde", "abcde") # 0
zin_hamming("strong", "strung") # 1