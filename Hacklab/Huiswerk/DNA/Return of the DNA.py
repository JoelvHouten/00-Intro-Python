# Return of the DNA

import random

def dna_seq(lengte):
    karakters = ['C', 'G', 'A', 'T']
    return ''.join(random.choice(karakters) for _ in range(lengte))

def dna_comp_seq(dna_sequentie):
    return ''.join(["G" if letter == "C" else
                    "C" if letter == "G" else
                    "T" if letter == "A" else
                    "A" for letter in dna_sequentie])

input_lengte = int(input("Geef een lengte in voor uw DNA: "))

dna_sequentie = dna_seq(input_lengte)
print(dna_sequentie)

print(len(dna_sequentie) * "|" )

complementaire_dna_sequentie = dna_comp_seq(dna_sequentie)
print(complementaire_dna_sequentie)
