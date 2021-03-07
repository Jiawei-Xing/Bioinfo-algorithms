#fasta
seqs={}
with open('rosalind_pdst.txt') as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()[1:]
            seqs[name] = []
        else:
            seqs[name].append(line.strip())
            
for name,seq in seqs.items():
    seqs[name] = ''.join(seq)

#count mutations
def mut(dna1, dna2):
    c=0
    for i in range(0, len(dna1)):
        if dna1[i] != dna2[i]:
            c+=1
    return c

#distance matrix
distance = []
for seq1 in seqs.values():
    distance.append([])
    for seq2 in seqs.values():
        distance[-1].append(mut(seq1, seq2) / len(seq1))
        
for n in distance:
    print(' '.join(map(str, n)))
