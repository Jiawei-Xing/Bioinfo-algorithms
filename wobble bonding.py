#include wobble bonding
def pair(a, b):
    if a == "A" and b == "U":
        return True
    elif a == "U" and b == "A":
        return True
    elif a == "G" and b == "C":
        return True
    elif a == "C" and b == "G":
        return True
    elif a == "G" and b == "U":
        return True
    elif a == "U" and b == "G":
        return True
    else:
        return False

# Motzkin number on the basis of Catalan number
def catalan(dna, cata):
    #bonding distance >= 4
    if len(dna) <= 4:
        return 1
    if dna in cata:
        return cata[dna]
    n = len(dna)
    c=0
    for m in range(4, n):
        if pair(dna[0], dna[m]):
            c += (catalan(dna[1:m], cata) * catalan(dna[m+1:], cata))
    c += catalan(dna[1:], cata)
    cata[dna] = c
    return cata[dna]

dna = 'CACCGUUUUCACACAAUUUGACUGUGAACCAGCGGAAAAUCCGACGGAGCUUGGAUUCAGUCCAGAACGAUAGAUCAUUUGAAGCUAUUUAUGUAUUCCCGUUUUUUGGUGGUACACCCAUUUUAGUUAAGUCCGACGUCCAUGUGUAAAGAUUCCUCGAGACUCAUGGCCGCCG'     
cata = {}       
print(catalan(dna,  cata))
