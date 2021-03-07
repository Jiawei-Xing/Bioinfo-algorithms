def revc(dna):
    dna_revc = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return dna_revc

s=[]
with open('rosalind_dbru.txt') as f1:
    for line in f1:
        s.append(line.strip())
        s.append(revc(line.strip()))
s = set(s)

for n in s:
    k = len(n) - 1
    print("(" + n[:k] + ", " + n[1:] + ")")
