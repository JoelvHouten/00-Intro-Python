# Opdracht 8A

lijst_dingen = ["auto", "Hond", "Nederland", "Boeing"]

empty_dict = {}
empty_dict['Voertuig'] = lijst_dingen[0]
empty_dict['Dier'] = lijst_dingen[1]
empty_dict['Land'] = lijst_dingen[2]
empty_dict['Vliegtuig'] = lijst_dingen[3]

print(f"Opdracht 8A \n{empty_dict}\n")

# Opdracht 8B

zoektocht = {'dict' : {'dict' : {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Deze': "Het antwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Deze': "Het andwo0rdt", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andw00rd", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}}}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}

print(f"Opdracht 8B \n{zoektocht['dict']['nou nog eentje dan']['nou nog eentje dan']['nou nog eentje dan']['dict']['dict']['Deze']}")



