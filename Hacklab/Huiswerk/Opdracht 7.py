# Opdracht 7A

namen_lijst = ["Joe","Lau","Destiny"]

print(f"Hallo ik ben {namen_lijst[0]}")
print("{0} is mijn naam en de naam van mijn vrouw is {1}".format(namen_lijst[0],namen_lijst[1]))
print("Mijn naam is " + namen_lijst[0] + " mijn vrouw heet " + namen_lijst[1] + " en de naam van onze kat is " + namen_lijst[2])

# Opdracht 7B

letterList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
zin = "Hallo ik ben Joe"
uiteindelijke_zin = ""

for letter in zin:
    if letter == ' ' or letter.upper or letter in letterList:
        uiteindelijke_zin += letter

print("\n- Zin geprint met For loop -")
print(uiteindelijke_zin)

print("\n- Zin geprint met elke losse letterlist index -")
print(f"{letterList[13].upper()}{letterList[18]}{letterList[10]}{letterList[10]}{letterList[8]} {letterList[7]}{letterList[11]} {letterList[23]}{letterList[2]}{letterList[24]} {letterList[12].upper()}{letterList[8]}{letterList[2]}{letterList[10]} {letterList[2]}{letterList[24]} {letterList[7]}{letterList[11]} {letterList[19]}{letterList[7]}{letterList[4]} {letterList[23]}{letterList[7]}{letterList[12]} {letterList[13].upper()}{letterList[18]}{letterList[21]}{letterList[11]}{letterList[10]}{letterList[18]}{letterList[23]}")

