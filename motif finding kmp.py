a=[]
with open("rosalind_kmp.txt") as f1:
    for line in f1:
        if ">" in line:
            continue
        a.append(line.strip())
s = ''.join(a)

#next array p
p = ['0'] * len(s)
j=0
for i in range(1, len(s)):
    if s[i] == s[j]:
        p[i] = str(j+1)
        j+=1
    else:
        while j > 1:
            j = int(p[j-1])
            if s[i] == s[j]:
                p[i] = str(j+1)
                j+=1
                break
        if j == 1:
            if s[i] == s[j]:
                p[i] = str(j+1)
                j+=1
            elif s[i] == s[0]:
                p[i] = '1'
                j=1
            else:
                p[i] = '0'
                j=0
                

with open("out.txt", 'w') as f2:
    f2.write(' '.join(p))
