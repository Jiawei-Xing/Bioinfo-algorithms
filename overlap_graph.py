#fasta
seqs={}
with open('rosalind_grph.txt') as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()[1:]
            seqs[name] = []
        else:
            seqs[name].append(line.strip())
            
for name,seq in seqs.items():
    seqs[name] = ''.join(seq)

#find overlapped seqs
start={}
end={}    
for name,seq in seqs.items():
    start[name] = seq[:3]
    end[name] = seq[-3:]
    
for name1,dna1 in end.items():
    for name2,dna2 in start.items():
        if dna1 == dna2 and name1 != name2:
            print(name1, name2)
