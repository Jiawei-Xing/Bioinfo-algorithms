#fasta
dna = {}
with open("rosalind_gc.txt") as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()
            dna[name]=[]
            continue
        else:
            dna[name].append(line.strip())

for name, seq in dna.items():
    dna[name] = ''.join(seq)

#calculate gc content
gc = {}
for name, seq in dna.items():
    g = seq.count('G')
    c = seq.count('C')
    gc[name] = (g+c)/len(seq)*100

print(gc)
