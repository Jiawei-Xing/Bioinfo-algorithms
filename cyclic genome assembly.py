l=[]
with open('rosalind_pcov.txt') as f1:
    for line in f1:
        l.append(line.strip())
        
k = len(l[0])-1
i=l[0]
out = i[-k:]
while len(out) < len(l):
    for j in l:
        if i[-k:] == j[:k]:
            out += j[-1]
            i=j
            break

print(out)
