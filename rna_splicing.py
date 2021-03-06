codon={}
with open("codon.txt") as f1:
    for line in f1:
        n = line.strip().split()
        codon[n[0]] = n[1]
        codon[n[2]] = n[3]
        codon[n[4]] = n[5]
        codon[n[6]] = n[7]
codon2={}
for c,aa in codon.items():
    codon2[c.replace('U', 'T')] = aa

dna = ''.join('''ATGACTTTCCTGTCTAGTATAGCCTATGGTGTGCTGCCGACAAAGAAGGTGTCCAACAGC
TCGGGCGGGTGCCGCCCTCAAAAAACAGGTAATACTACAATGTAGTACCCATTACCTCGT
CATATCCACCCCAAGCTCCGACCACTAGCTGGGGGGGAGCTACTGGCATATGTTAGCTGC
TATGGCGATGCAAGACAGATACTCTCATCTATGGATGATCGTACCTACCAGTGCAACAAC
GCCCTGCTGGGAAGGAAACCACAACGAGAACTGTCGCCCATGTTTCAAGACTGGGGGACA
CAGTACTCGTCGCCGTAATTGAAGAGAGGAGTACTTATGACATCTGGAGCAGCATCACTC
ATTGAACTGAAGCTGCACATTTAAAATCCCATGCTATACGACAGGAAGGCAGTTTCACTG
GTCAATATTTCGTAGCGCCTCGTAACTGTTCGGTACCTCTGGGAATATCAGTCATCAGGC
GCATTCACTGTATCCCGAGATCGTATTGCACGTTTCCACTGCAACAATCGATTAGATCCG
GTTTTACGATCTTATGTAATCGTCTCTTAAGGTAGGATCTGACGGAAGGCTCCACTGGAT
TGTAGTGATTGGGACAGGACTCGTGACTTTGTCATAACAAGAGTAATGTGCACATATTAG
CTTGCGTCCCGAGGCGGGATAGCGGCTGGCTTGACCTATGCTTAACCCGTAGAACAAAAC
CGCGACTGGGTTGGTAGCTTGGGCACCCCCTTTTCGATGGTAGTTACTGCGTGTGAGCCA
GTGTGCTCGGCCACACCTCCGTTGCGAAGAGCCTCGGCAGTATCTGGACGGCGCCCTAAA
GGTCCGGCCTCGACGGCTCGTCTACTACTTTACAGTTAAGCGGCGTCCTACTCTCATCGA
CCGGACTTCCAAGTCAAATCCACACTTGGGTGTCTCCAGTAG
'''.split("\n"))
intron = '''>Rosalind_0303
AGGAAACCACAACGAGAACTGTCGCC
>Rosalind_9003
TTACGATCTTATGTAATCGTCTCTTAAG
>Rosalind_0561
ACTGGTCAATATTTCGTA
>Rosalind_4573
AAACCGCGACTGGGTTGGTAGCTTGGGCACCCCCTT
>Rosalind_7694
ACAGTACTCGTCGCCGTAATTGAAGAGAGGAGTACTTATGACATCTGGA
>Rosalind_2609
GAACTGAAGCTGCACATTTA
>Rosalind_8805
TGAGCCAGTGT
>Rosalind_4415
TACTCTCATCTATGGATGATCGTACC
>Rosalind_0971
TCAGTCATCAGGCGCATTCACTGTATCCCGAGATCGTATTGCACGTTTC
>Rosalind_2200
CACTGGATTGTAGTGATTGGGACAGGACTCGTGACTTTGTC
>Rosalind_9341
TGCGAAGAGCCTCGGCAGTATCTGGACGG
>Rosalind_7294
GCTCGTCTACTACTTT
>Rosalind_0690
TATTAGCTTGCGTCCCG
>Rosalind_2767
GTGTCCAACA
>Rosalind_1093
CATTACCTCGTCATATCCACCCCAAGCTCCGACCACTAGCTGGGG
>Rosalind_8105
CCTACTCTCATCGACCG
'''.split("\n")

#cutoff introns
for i in range(1, len(intron), 2):
    n = intron[i]
    k = dna.find(n)
    dna = dna[:k] + dna[k+len(n):]

#translate the extron
p=''    
for i in range(0, len(dna), 3):
    if codon2[dna[i:i+3]] != "Stop":
        p += codon2[dna[i:i+3]]
print(p)
