#fasta
seqs={}
with open('rosalind_corr.txt') as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()[1:]
            seqs[name] = ''
        else:
            seqs[name] += ''.join(line.strip())

#reverse complement            
def revc(dna):
    dna_revc = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return dna_revc

#find correct reads
correct={}
for name1,seq1 in seqs.items():
    for name2,seq2 in seqs.items():
        if name1 == name2:
            continue
        if seq1 == seq2 or revc(seq1) == seq2:
            if name1 not in correct:
                correct[name1] = seq1
            if name2 not in correct:
                correct[name2] = seq2

#count mutations
def mut(dna1, dna2):
    c=0
    for i in range(0, len(dna1)):
        if dna1[i] != dna2[i]:
            c+=1
    return c

#pair and print error reads            
for name1,seq1 in seqs.items():
    if name in correct:
        continue
    for name2,seq2 in correct.items():
        if mut(seq1, seq2) == 1:
            print(seq1 + "->" + seq2)
            break
        elif mut(seq1, revc(seq2)) == 1:
            print(seq1 + "->" + revc(seq2))
            break
