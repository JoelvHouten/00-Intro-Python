# DNA wars

from DNA_Generator import DNA_Gen

Codon_Dict = {'T' : {'T' : {'T' : "Phenylalanine", 'C' : "Phenylalanine", 'A' : "Leucine", 'G' : "Leucine"},'C' : {'T' : "Serine", 'C' : "Serine", 'A' : "Serine", 'G' : "Serine"}, 'A' : {'T' : "Tyrosine", 'C' : "Tyrosine", 'A' : "Stop (Ochre)", 'G' : "Stop (Amber)"}, 'G' : {'T' : "Cysteine", 'C' : "Cysteine", 'A' : "Stop (Opal)", 'G' : "Tryptophan"}}, 'C' : {'T' : {'T' : "Leucine", 'C' : "Leucine", 'A' : "Leucine", 'G' : "Leucine"}, 'C' : {'T' : "Proline", 'C' : "Proline", 'A' : "Proline", 'G' : "Proline"}, 'A' : {'T' : "Histidine", 'C' : "Histidine", 'A' : "Glutamine", 'G' : "Glutamine"}, 'G' : {'T' : "Arginine", 'C' : "Arginine", 'A' : "Arginine", 'G' : "Arginine"}}, 'A' : {'T' : { 'T' : "Isoleucine", 'C' : "Isoleucine", 'A' : "Isoleucine", 'G' : "Methionine"}, 'C' : {'T' : "Threonine", 'C' : "Threonine", 'A' : "Threonine", 'G' : "Threonine"}, 'A' : {'T' : "Asparagine", 'C' : "Asparagine", 'A' : "Lysine", 'G' : "Lysine"}, 'G' : {'T' : "Serine", 'C' : "Serine", 'A' : "Arginine", 'G' : "Arginine"}}, 'G' : {'T' : { 'T' : "Valine", 'C' : "Valine", 'A' : "Valine", 'G' : "Valine"}, 'C' : {'T' : "Alanine", 'C' : "Alanine", 'A' : "Alanine", 'G' : "Alanine"}, 'A' : {'T' : "Aspartic acid", 'C' : "Aspartic acid", 'A' : "Glutamic acid", 'G' : "Glutamic acid"}, 'G' : {'T' : "Glycine", 'C' : "Glycine", 'A' : "Glycine", 'G' : "Glycine"}}}

def Codon_Translate(Codons, sequence):
    First, Second, Third = 0, 1, 2
    Codon_List = []
    while First <= len(sequence)-1 and Second <= len(sequence)-1 and Third <= len(sequence)-1:
        Codon_List.append(Codons[sequence[First]][sequence[Second]][sequence[Third]])
        First += 3
        Second += 3
        Third += 3
    Last_nucs = len(sequence) % 3
    if Last_nucs == 1:
        Codon_List.append(Codons[sequence[-1]])
    elif Last_nucs == 2:
        Codon_List.append(Codons[sequence[-2]][sequence[-1]])
    return Codon_List

def Codon_Translate_2(Codons, sequence):
    Codon_List = []
    remains = len(sequence) % 3
    for i in range(0, len(sequence) - remains, 3):
    # for i in range(0, len(sequence), 3):
        Codon_List.append(Codons[sequence[i]][sequence[i+1]][sequence[i+2]])
    if remains == 1:
        Codon_Set = set()
        for nuc in Codons[sequence[-1]]:
            for nucnuc in Codons[sequence[-1]]:
                Codon_Set.add(Codons[sequence[-1]][nuc][nucnuc])
        Codon_List.append(list(Codon_Set))
    elif remains == 2:
        Codon_List.append(list(set(Codons[sequence[-2]][sequence[-1]].values())))
    return Codon_List

Codon_Dict = {'T' : {'T' : {'T' : "Phenylalanine", 'C' : "Phenylalanine", 'A' : "Leucine", 'G' : "Leucine"},'C' : {'T' : "Serine", 'C' : "Serine", 'A' : "Serine", 'G' : "Serine"}, 'A' : {'T' : "Tyrosine", 'C' : "Tyrosine", 'A' : "Stop (Ochre)", 'G' : "Stop (Amber)"}, 'G' : {'T' : "Cysteine", 'C' : "Cysteine", 'A' : "Stop (Opal)", 'G' : "Tryptophan"}}, 'C' : {'T' : {'T' : "Leucine", 'C' : "Leucine", 'A' : "Leucine", 'G' : "Leucine"}, 'C' : {'T' : "Proline", 'C' : "Proline", 'A' : "Proline", 'G' : "Proline"}, 'A' : {'T' : "Histidine", 'C' : "Histidine", 'A' : "Glutamine", 'G' : "Glutamine"}, 'G' : {'T' : "Arginine", 'C' : "Arginine", 'A' : "Arginine", 'G' : "Arginine"}}, 'A' : {'T' : { 'T' : "Isoleucine", 'C' : "Isoleucine", 'A' : "Isoleucine", 'G' : "Methionine"}, 'C' : {'T' : "Threonine", 'C' : "Threonine", 'A' : "Threonine", 'G' : "Threonine"}, 'A' : {'T' : "Asparagine", 'C' : "Asparagine", 'A' : "Lysine", 'G' : "Lysine"}, 'G' : {'T' : "Serine", 'C' : "Serine", 'A' : "Arginine", 'G' : "Arginine"}}, 'G' : {'T' : { 'T' : "Valine", 'C' : "Valine", 'A' : "Valine", 'G' : "Valine"}, 'C' : {'T' : "Alanine", 'C' : "Alanine", 'A' : "Alanine", 'G' : "Alanine"}, 'A' : {'T' : "Aspartic acid", 'C' : "Aspartic acid", 'A' : "Glutamic acid", 'G' : "Glutamic acid"}, 'G' : {'T' : "Glycine", 'C' : "Glycine", 'A' : "Glycine", 'G' : "Glycine"}}}

DNA_seq = DNA_Gen(20)
DNA_seq = "CAAGGCCTGAATCCCAATAT"
print(DNA_seq)
print(DNA_seq[:-1])

print(Codon_Translate(Codon_Dict, DNA_seq))
print(Codon_Translate(Codon_Dict, DNA_seq[:-1]))

print(Codon_Translate_2(Codon_Dict, DNA_seq))
print(Codon_Translate_2(Codon_Dict, DNA_seq[:-1]))