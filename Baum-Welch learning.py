states = 'A B C'.split()
observe = 'yxzzxyyyzxyxyzxzzxyzyyyxxxxyzyxzzxxzyxxyyyxxxzzzxzyxxzxyyxzyyyxzzxxzzzyxxzzxzzzxzxxxzzzzyzzxyzzyyyxx'
strings = 'x y z'.split()

p_states=[]
p_states.append('0.028	0.468	0.504'.split())
p_states.append('0.281	0.433	0.287'.split())
p_states.append('0.413	0.342	0.246'.split())

p_strings=[]
p_strings.append('0.389	0.125	0.486'.split())
p_strings.append('0.118	0.396	0.486'.split())
p_strings.append('0.07	0.742	0.187'.split())

# forward algorithm
def forward(p_states, p_strings):
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
    f_out=[]    
    for i in range(len(f[0])):
        f_out.append([])
        for j in range(len(f)):
            f_out[-1].append(f[j][i])
    return f_out, sum(f[-1])

# backward algorithm
def backward(p_states, p_strings):
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
    b_out=[]    
    for i in range(len(b[0])):
        b_out.append([])
        for j in range(len(b)):
            b_out[-1].append(b[j][i])
    return b_out

# edge responsibility matrix
def pi_star_star(f, b, p):
    pss=[]
    for i in range(len(states)):
        for j in range(len(states)):
            pss.append([])
            for k in range(len(observe)-1):
                pss[-1].append(f[i][k] * float(p_states[i][j]) * float(p_strings[j][strings.index(observe[k+1])]) * b[j][k+1] / p)
    return pss
    
# transition matrix
def transition(pi_star_star):
    t=[]
    c=0
    for i in range(len(states)):
        t.append([])
        for j in range(len(states)):
            t[-1].append(sum(pi_star_star[c]))
            c+=1
    return t
    
# node responsibility matrx
def pi_star(f, b, p):
    ps=[]
    for i in range(len(states)):
        ps.append([])
        for j in range(len(observe)):
            ps[-1].append(f[i][j] * b[i][j] / p)
    return ps
    
# emission matrix
def emission(pi_star):
    e=[]
    for i in range(len(states)):
        e.append([])
        for j in range(len(strings)):
            c=0
            for k in range(len(observe)):
                if observe[k] == strings[j]:
                    c += pi_star[i][k]
            e[-1].append(c)
    return e
    
# normalize matrix
def normalize(l):
    out=[]
    for i in l:
        out.append([])
        for j in i:
            out[-1].append(j/sum(i))
    return out

# iteration
for i in range(100):
    f, p = forward(p_states, p_strings)
    b = backward(p_states, p_strings)
    pss = pi_star_star(f, b, p)
    ps = pi_star(f, b, p)
    p_states = normalize(transition(pss))
    p_strings = normalize(emission(ps))

# output
with open('results.txt', 'w') as f1:
    f1.write('\t' + '\t'.join(states) + '\n')
    for i in range(len(p_states)):
        f1.write(states[i] + '\t' + '\t'.join(map(str, p_states[i])) + '\n')
    f1.write('-'*8 + '\n')
    f1.write('\t' + '\t'.join(strings) + '\n')
    for i in range(len(p_strings)):
        f1.write(states[i] + '\t' + '\t'.join(map(str, p_strings[i])) + '\n')

