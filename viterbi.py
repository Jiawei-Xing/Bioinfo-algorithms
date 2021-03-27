states = 'A   B C'.split()
observe = 'zyxyzzxyzzyzyxyzzxzyzxzxxzyzyzxyyyzyzyyzzzzzyyxzzyzxzyyzzxyzyxzyxyyyxxyxyyyxzzzyxzxzxyxxxxzzzyzxyyzx'
string = 'x   y   z'.split()

p_states=[]
p_states.append('0.222	0.74	0.038'.split())
p_states.append('0.252	0.327	0.421'.split())
p_states.append('0.391	0.071	0.538'.split())

p_string=[]
p_string.append('0.127	0.167	0.706'.split())
p_string.append('0.167	0.35	0.483'.split())
p_string.append('0.033	0.292	0.674'.split())

# initialize track
track=[]
for i in range(len(states)):
    track.append([0])

p1=[]
for k in range(len(states)):
    p1.append(1/len(states) * float(p_string[k][string.index(observe[0])]))

# track max
for i in range(1, len(observe)):
    p2 = []
    for j in range(len(states)):
        s=[]
        for k in range(len(p_states)):
            s.append(float(p_states[k][j]) * p1[k] * float(p_string[j][string.index(observe[i])]))
        track[j].append(s.index(max(s)))
        p2.append(max(s))
    p1 = p2[:]

# end track
for i in range(len(track)):
    track[i].append(p1.index(max(p1)))

# trackback
i = len(track[0])-2
j = track[0][-1]
hidden = states[j]

while i > 0:
    hidden += states[track[j][i]]
    j = track[j][i]
    i-=1

print(hidden[::-1])
