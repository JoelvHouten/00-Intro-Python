import random
import os

woordlijst_bestand = os.path.join(os.path.dirname(__file__), 'Woordlijst.txt')
score_bestand = os.path.join(os.path.dirname(__file__), 'scores.txt')

with open(woordlijst_bestand) as file:
    woordlijst = file.read().split()

def laad_score(naam, score_bestand):
    if os.path.exists(score_bestand):
        with open(score_bestand, 'r') as f:
            for lijn in f:
                speler, speler_score = lijn.strip().split(',')
                if speler == naam:
                    return int(speler_score)
    return 0

def sla_score_op(naam, score, score_bestand):
    scores = {}
    if os.path.exists(score_bestand):
        with open(score_bestand, 'r') as f:
            for lijn in f:
                speler, speler_score = lijn.strip().split(',')
                scores[speler] = int(speler_score)

    scores[naam] = score

    with open(score_bestand, 'w') as f:
        for speler, speler_score in scores.items():
            f.write(f"{speler},{speler_score}\n")

def start_spel(woordlijst, score_bestand, naam=None, score=0):
    max_fouten = 10
    fouten = 0
    woord_info = False
    welkom = False

    woord = random.choice(woordlijst)
    verborgen_woord = ["_"] * len(woord)
    geraden_letters = []

    while fouten <= max_fouten - 1 and "_" in verborgen_woord:
        if not welkom:
            if naam == None:
                naam = input("Wat is je naam?: ")
            else:
                welkom = True
            score = laad_score(naam, score_bestand)
            print(f"\nHallo {naam}, welkom bij Galgje.")
            if score > 0:
                print(f"Je score is {score}. We gaan weer verder.")
            welkom = True

        elif not woord_info:
            print(f"Het gekozen woord bestaat uit {len(woord)} letters")
            print(f"Je mag in totaal {max_fouten} fouten maken. Success!")
            woord_info = True

        else:
            print(f"\nHuidige staat van het woord: {' '.join(verborgen_woord)}")
            print(f"Aantal fouten: {fouten}/{max_fouten}")
            print(f"Geraden woorden: {score}")
            print(f"Gebruikte Letters: {', '.join(geraden_letters)}")
            gok = input("\nVul een letter/woord in om te raden: ").lower()
            os.system("cls")

            if gok == woord:
                verborgen_woord = list(woord)
            elif gok != "cheat" and len(gok) > 1:
                print(f"\nHelaas komt {gok.upper()} niet overeen met het verborgen woord")
                fouten += 1
            elif gok == "cheat":
                print(f"\nValspeler!! Nou vooruit het woord is: {woord.upper()}")
            elif not gok.isalpha():
                print("\nVoer een geldige letter in!")
            elif gok in geraden_letters:
                print(f"\nDe letter {gok.upper()} is al een keer geprobeerd. Probeer een andere letter.")
            elif len(gok) == 1:
                geraden_letters.append(gok)
                if gok in woord:
                    for i in range(len(woord)):
                        if woord[i] == gok:
                            verborgen_woord[i] = gok
                    print(random.choice([
                        f"\nGoed geraden! De letter {gok.upper()} zit inderdaad in het verborgen woord!",
                        f"\nLekker bezig {naam}. De letter {gok.upper()} zit in het woord.",
                        f"\nNetjes! De letter {gok.upper()} zit in het verborgen woord."
                    ]))
                else:
                    fouten += 1
                    print(f"\nHelaas de letter {gok.upper()} komt niet voor in het woord")

    if "_" not in verborgen_woord:
        os.system("cls")
        score += 1
        sla_score_op(naam, score, score_bestand)
        print(f"\nGefeliciteerd {naam}, het woord was inderdaad {woord.upper()}")
        print(f"\nJe hebt een punt verdiend. Je score is nu: {score}.")
    else:
        os.system("cls")
        print(f"\nHelaas {naam}, je hebt het woord niet geraden")
        if score > 0:
            print(f"\nJe verliest een punt. Je score gaat van {score} naar {score - 1}.")
            score -= 1
            sla_score_op(naam, score, score_bestand)
        else:
            print("Je hebt nog geen punten. Zet hem op!")
        print(f"Het te raden woord was: {woord.upper()}")

    return naam, score

def begin_opnieuw(woordlijst, score_bestand):
    naam = None
    score = 0

    while True:
        naam, score = start_spel(woordlijst, score_bestand, naam, score)
        while True:
            herstart_vraag = input(f"\nWil je nog een keer spelen? J is ja, N is nee: ").lower()
            if herstart_vraag == "j":
                os.system("cls")
                break
            elif herstart_vraag == "n":
                os.system("cls")
                print(f"Bedankt voor het spelen {naam} en tot de volgende keer.")
                print("De scores zijn opgeslagen. Gebruik dezelfde naam om verder te spelen.")
                exit()
            else:
                print("Ongeldige invoer. Voer 'J' in voor ja of 'N' voor nee.")

begin_opnieuw(woordlijst, score_bestand)