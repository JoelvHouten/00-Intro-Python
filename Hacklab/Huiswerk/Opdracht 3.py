# Opdracht 3A

getal = int(input("Voer een getal in "))

if getal > 10:
    print("Het ingevoerde getal is groter dan 10")
elif getal < 10:
    print("Het ingevoerde getal is kleiner dan 10")
else:
    print("Het ingevoerde getal is 10")

# Opdacht 3B

maand = input("Hoeevel dagen heeft de maand? Vul een maand in: ").lower()

match maand:
    case "januari":
        print("Januari heeft 31 dagen")
    case "februari":
        print("Februari heeft 28 dagen (29 in een schrikkeljaar)")
    case "maart":
        print("Maart heeft 31 dagen")
    case "april":
        print("April heeft 30 dagen")
    case "mei":
        print("Mei heeft 31 dagen")
    case "juni":
        print("Juni heeft 30 dagen")
    case "juli":
        print("Juli heeft 31 dagen")
    case "augustus":
        print("Augustus heeft 31 dagen")
    case "september":
        print("September heeft 30 dagen")
    case "oktober":
        print("Oktober heeft 31 dagen")
    case "november":
        print("November heeft 30 dagen")
    case "december":
        print("December heeft 31 dagen")
    case _:
        print("Dit is geen geldige maand. Probeer opnieuw.")