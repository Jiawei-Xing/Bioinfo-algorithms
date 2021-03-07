#fasta
seqs={}
with open('rosalind_cons.txt', 'r') as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()
            seqs[name]=[]
        else:
            seqs[name].append(line.strip())

for name,seq in seqs.items():
    seqs[name] = ''.join(seqs[name])
    j = len(seqs[name])

#matrix
A = []
C = []
G = []
T = []
for i in range(0, j):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)

for i in range(0, j):
    for seq in seqs.values():
        if seq[i] == 'A':
            A[i] += 1
        elif seq[i] == 'C':
            C[i] += 1
        elif seq[i] == 'G':
            G[i] += 1
        else:
            T[i] += 1

#consensus seq            
consensus=[]
for i in range(0, j):
    m = max(A[i], C[i], G[i], T[i])
    if m == A[i]:
        consensus.append('A')
    elif m == C[i]:
        consensus.append('C')
    elif m == G[i]:
        consensus.append('G')
    else:
        consensus.append('T')
    
print(''.join(consensus))
print('A:', ' '.join(str(n) for n in A))
print('C:', ' '.join(str(n) for n in C))
print('G:', ' '.join(str(n) for n in G))
print('T:', ' '.join(str(n) for n in T))
