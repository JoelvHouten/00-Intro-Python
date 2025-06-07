# Opdracht 12

def double_char(zin):
    zin_dubbel = ""
    
    for i in zin:
        zin_dubbel += i * 2

    print(zin_dubbel)

double_char("String") # "SSttrriinngg"
double_char("Hello World!") # "HHeelllloo  WWoorrlldd!!"
double_char("1234!_ ") # "11223344!!__  "