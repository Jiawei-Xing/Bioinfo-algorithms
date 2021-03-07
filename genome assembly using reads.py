#genome reads: [s]
def revc(dna):
    dna_revc = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return dna_revc

s=[]
with open('rosalind_gasm.txt') as f1:
    for line in f1:
        s.append(line.strip())
        s.append(revc(line.strip()))
s = list(set(s))

#find k for the de Bruijin graph
l = len(s[0])
def find_k(i, s=s, l=l):
    for n in range(1, l//2-1):
        k = l - n
        for j in s:
            if i[-k:] == j[:k]:
                return k, j

#genome assembly1: [g1]
i=s[0]
g1 = ''
while True:
    if find_k(i) == None:
        break
    k, j = find_k(i)
    g1 += j[k-l:]
    s[s.index(j)] = ''
    i=j
s=s[1:]
s=list(filter(None, s))
print(g1)

#genome assembly2: [g2]
i=s[0]
g2 = ''
while True:
    if find_k(i=i, s=s) == None:
        break
    k, j = find_k(i=i, s=s)
    g2 += j[k-l:]
    s[s.index(j)] = ''
    i=j
print(g2)
print(max(g1, g2, key=len))
