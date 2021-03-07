dna=[]
with open('rosalind_cstr.txt') as f1:
    for line in f1:
        dna.append(line.strip())

j=0
n=[]
while j < len(dna[0]):
    n.append([])
    for i in range(len(dna)):
        n[j].append(dna[i][j])
    j+=1

for s in n:
    flag=0
    for e in s:
        if s.count(e) >= len(dna)-1:
            flag=1
            break
    if flag == 0:
        c=''
        for h in s:
            if h == s[0]:
                c+='1'
            else:
                c+='0'
        print(c)

