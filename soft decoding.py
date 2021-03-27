states = 'A   B'.split()
observe = 'xxzzzyzxzz'
strings = 'x   y   z'.split()

p_states=[]
p_states.append('0.384	0.616'.split())
p_states.append('0.9	0.1'.split())
p_strings=[]
p_strings.append('0.316	0.258	0.425'.split())
p_strings.append('0.178	0.006	0.817'.split())


# forward algorithm (likelihood)
f=[]
p1=[]
for n in range(len(states)):
    p1.append(1/len(states) * float(p_strings[n][strings.index(observe[0])]))
f.append(p1)    
            
for i in range(1, len(observe)):
    p2 = []
    for j in range(len(states)):
        s=0
        for k in range(len(states)):
            s += float(p_states[k][j]) * p1[k] * float(p_strings[j][strings.index(observe[i])])
        p2.append(s)
    p1 = p2[:]
    f.append(p1)


# backward algorithm
b=[]
p1=[]
for n in range(len(states)):
    p1.append(1)
b.append(p1)    
        
for i in range(len(observe)-2, -1, -1):
    p2 = []
    for j in range(len(states)):
        s=0
        for k in range(len(states)):
            s += float(p_states[j][k]) * p1[k] * float(p_strings[k][strings.index(observe[i+1])])
        p2.append(s)
    p1 = p2[:]
    b.append(p1)
b = b[::-1]


# forward * backward / Px
with open('out.txt', 'w') as f1:
    f1.write('\t'.join(states) + '\n')
    for i in range(len(f)):
        t=[]
        for j in range(len(f[0])):
            t.append(str(f[i][j] * b[i][j] / sum(f[-1])))            
        f1.write('\t'.join(t) + '\n')
