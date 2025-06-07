# DNA

# DNA sequenties
dna_sequentie = "CGCCAATTTTCGTCAAAGGA"
complementaire_dna_sequentie = ""

# Zet standaard DNA om naar complementaire sequentie en print de sequenties
for letter in dna_sequentie:
    if letter == "C":
        complementaire_dna_sequentie += "G" # Cytosine - Guanine
    elif letter == "G":
        complementaire_dna_sequentie += "C" # Guanine - Cytosine
    elif letter == "A":
        complementaire_dna_sequentie += "T" # Adenine - Thymine
    elif letter == "T":
        complementaire_dna_sequentie += "A" # Thymine - Adenine

print(f"Standaard DNA sequentie: \t{dna_sequentie}")
print ("\t\t\t\t" + len(dna_sequentie) * "|")
print(f"Complementaire DNA sequentie: \t{complementaire_dna_sequentie}")