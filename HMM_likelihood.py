states = 'A   B'.split()
observe = 'yyxxyzxyzyyxyyzzzyxyyxxzyyzzzyyxyyxxyxzzyxyyxyzzxxxzxyzzxzzxyyxzyyzyxyyzxxzxzzyyyzzxyxxyxxxxzyyyzzzz'
string = 'x   y   z'.split()

p_states=[]
p_states.append('0.108	0.892'.split())
p_states.append('0.801	0.199'.split())
p_string=[]
p_string.append('0.489	0.192	0.319'.split())
p_string.append('0.577	0.22	0.203'.split())

p1=[]
for k in range(len(states)):
    p1.append(0.5 * float(p_string[k][string.index(observe[0])]))
    
for i in range(1, len(observe)):
    p2 = []
    for j in range(len(states)):
        s=0
        for k in range(len(p_states)):
            s += float(p_states[k][j]) * p1[k] * float(p_string[j][string.index(observe[i])])
        p2.append(s)
    p1 = p2[:]
    
print(sum(p1))

