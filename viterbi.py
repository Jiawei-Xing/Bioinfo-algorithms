hidden = ''
states = 'A   B'.split()
observe = 'yzxxyyxzxzyxyzxyyyyyxzxyyzxxyyxzxzzxzzxzzzyyzzyxxxzzyzyxyzxzzyzzxxzxzzzzzxzxzzxzyxyzyxyyxxyxxyxxyyyz'
string = 'x   y   z'.split()

p_states=[]
p_states.append('0.402	0.598'.split())
p_states.append('0.574	0.426'.split())
p_string=[]
p_string.append('0.011	0.06	0.929'.split())
p_string.append('0.293	0.489	0.218'.split())

for i in range(len(observe)):
    p=[]
    for j in range(len(states)):
        s=0
        for n in p_states:
            s += float(n[j])
        p.append(float(p_string[j][string.index(observe[i])]) * s)
    hidden += states[p.index(max(p))]
        
print(hidden)
