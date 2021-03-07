#input [seqs]
s=[]
with open('rosalind_trie.txt') as f1:
    for line in f1:
        s.append(line.strip())

#initialize {out} dict
out={}
out['0-1'] = '1'
i=1
for n in s[0]:
    i+=1
    out['0' + str(i-2)] = str(i)
    print(i-1, i, n)

#add other seqs to {out} & print an adjacent list
for j in range(1, len(s)):
    p=0
    for n in range(j):
        k=0
        while s[j][k] == s[n][k]:
            k+=1
        if k > p:
            p = k
            o = n
    i+=1
    out[str(j) + str(p)] = str(i)
    print(out[str(o) + str(p-1)] , i, s[j][p])
    for l in range(p+1, len(s[j])):
        i+=1
        out[str(j) + str(l)] = str(i)
        print(i-1 , i, s[j][l])
