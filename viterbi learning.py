states = 'A B C D'.split()
observe = 'xxzzxyxxxyzxxxzzzxxyxxyzxyyyzxxxzzyxyyyyxzyyzyyyxxyyzxxxzxyxzxxyyxxzzyxxzyzzxxzyyzxzzyyyyxyyzyzzxxzz'
strings = 'x   y   z'.split()

p_states=[]
p_states.append('0.214	0.207	0.285	0.295'.split())
p_states.append('0.493	0.317	0.071	0.119'.split())
p_states.append('0.128	0.508	0.296	0.068'.split())
p_states.append('0.078	0.666	0.098	0.158'.split())

p_strings=[]
p_strings.append('0.494	0.172	0.334'.split())
p_strings.append('0.156	0.352	0.492'.split())
p_strings.append('0.522	0.195	0.283'.split())
p_strings.append('0.194	0.529	0.277'.split())


def viterbi(p_states, p_strings):
    track=[]
    for i in range(len(states)):
        track.append([0])
    p1=[]
    for k in range(len(states)):
        p1.append(1/len(states) * float(p_strings[k][strings.index(observe[0])]))
    for i in range(1, len(observe)):
        p2 = []
        for j in range(len(states)):
            s=[]
            for k in range(len(p_states)):
                s.append(float(p_states[k][j]) * p1[k] * float(p_strings[j][strings.index(observe[i])]))
            track[j].append(s.index(max(s)))
            p2.append(max(s))
        p1 = p2[:]
    for i in range(len(track)):
        track[i].append(p1.index(max(p1)))

    i = len(track[0])-2
    j = track[0][-1]
    hidden = states[j]
    while i > 0:
        hidden += states[track[j][i]]
        j = track[j][i]
        i-=1
    return hidden[::-1]


def transition(hidden):
    transition=[]
    for i in range(len(states)):
        transition.append([0] * len(states))
    for s in range(len(states)):
        total = hidden[:-1].count(states[s])
        if total == 0:
            for t in range(len(states)):
                transition[s][t] = 1/len(states)
            continue
        for t in range(len(states)):
            for i in range(len(hidden)-1):
                if hidden[i] == states[s] and hidden[i+1] == states[t]:
                    transition[s][t] += 1
            transition[s][t] /= total
    return transition


def emission(hidden):
    emission=[]
    for i in range(len(states)):
        emission.append([0] * len(strings))
    for s in range(len(states)):
        total = hidden.count(states[s])
        if total == 0:
            for t in range(len(strings)):
                emission[s][t] = 1/len(strings)
            continue
        for t in range(len(strings)):
            for i in range(len(hidden)):
                if hidden[i] == states[s] and observe[i] == strings[t]:
                    emission[s][t] += 1
            emission[s][t] /= total
    return emission


# iteration
for i in range(100):
    hidden = viterbi(p_states, p_strings)
    p_states = transition(hidden)
    p_strings = emission(hidden)


# output
with open('results.txt', 'w') as f1:
    f1.write('\t' + '\t'.join(states) + '\n')
    for i in range(len(p_states)):
        f1.write(states[i] + '\t' + '\t'.join(map(str, p_states[i])) + '\n')
    f1.write('-'*8 + '\n')

    f1.write('\t' + '\t'.join(strings) + '\n')
    for i in range(len(p_strings)):
        f1.write(states[i] + '\t' + '\t'.join(map(str, p_strings[i])) + '\n')
