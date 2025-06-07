# Opdracht 17

def count_all(zin):
    resultaat = { "LETTERS": 0, "DIGITS": 0 }

    for char in zin:
        if char.isalpha():
            resultaat["LETTERS"] += 1
        elif char.isdigit():
            resultaat["DIGITS"] += 1

    return resultaat

print(count_all("Hello World"))   # { "LETTERS":  10, "DIGITS": 0 }
print(count_all("H3ll0 Wor1d"))   # { "LETTERS":  7, "DIGITS": 3 }
print(count_all("149990"))        # { "LETTERS":  0, "DIGITS": 6 }