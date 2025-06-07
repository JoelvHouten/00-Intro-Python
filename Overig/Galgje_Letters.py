def toon_woord(woord, geraden_letters):
    weergave = [letter if letter in geraden_letters else '_' for letter in woord]
    return " ".join(weergave)

woord = "jemoederiseenplopkoek"
geraden_letters = ["a"]
print(toon_woord(woord, geraden_letters))
print(f"Welkom bij Galgje. het woord bestaat uit {len(woord)} letters.")

while '_' in toon_woord(woord, geraden_letters):
    gok = input("Vul een letter in: ")

    if gok in woord:
        geraden_letters.append(gok)
        print(toon_woord(woord, geraden_letters))
    else:
        print("Helaas, die letter zit er niet in.")
else:
    print("Gefeliciteerd je moeder is inderdaad een plopkoek!")