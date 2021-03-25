hidden = ''
states = 'A   B'.split()
observe = 'zyyxyyxyzxxxzzxyyzzxxyxxyxxyzyxzxzzyyyxyxzxzyzzzyxxxzxxzyzxyyyyzxxzyzzxxyyxzyzzxzyyzzxzyzxzzyyxyzxzz'
string = 'x   y   z'.split()

p_states=[]
p_states.append('0.157	0.843'.split())
p_states.append('0.168	0.832'.split())
p_string=[]
p_string.append('0.588	0.217	0.195'.split())
p_string.append('0.384	0.504	0.112'.split())

p1=[]
for k in range(len(states)):
    p1.append(0.5 * float(p_string[k][string.index(observe[0])]))
hidden = 'A'

for i in range(1, len(observe)):
    p2 = []
    for j in range(len(states)):
        s=0
        for k in range(len(p_states)):
            s += float(p_states[k][j]) * p1[k] * float(p_string[j][string.index(observe[i])])
        p2.append(s)
    hidden += states[p2.index(max(p2))]
    p1 = p2[:]
        
print(hidden)
