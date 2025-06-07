# DNA Strikes Back

dna_dict = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
dna_sequentie = "CGCCAATTTTCGTCAAAGGA"        
complementaire_sequentie = ""
         
for base in dna_sequentie:
    complementaire_sequentie += dna_dict[base]

print(dna_sequentie)
print(len(dna_sequentie) * "|")
print(complementaire_sequentie)