#fasta
seqs={}
with open('rosalind_lcsm.txt') as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()[1:]
            seqs[name] = []
        else:
            seqs[name].append(line.strip())
            
for name,seq in seqs.items():
    seqs[name] = ''.join(seq)

#find the longest shared motif    
m=min(seqs.values())
n=len(seqs)
for j in range(len(m),2,-1):
    for i in range(0,len(m)-j+1):
        flag = 0
        for seq in seqs.values():
            if m[i:i+j] in seq:
                flag+=1
            else:
                break
        if flag == n:
            print(m[i:i+j])
            break
    if flag == n:
        break

