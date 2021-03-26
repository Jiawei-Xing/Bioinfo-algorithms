import numpy as np

observe = 'zyxxxzzyxxxxyzzzyzyxyyxxyxyxyyxyyxzxyyzyyyzzyyxzzzyyyzxzzxyyzzzzyyzxxxyyzyxxyzzzyzyxxzyyyxyyzzzzzyyz'
strings = 'x   y   z'.split()
hidden = 'AACCCAAACAAACBACBCAAACCAACBBABCAAAACACBCBAACCBCABCCCACCABCACAABBACABABABAAAAAAAACBCBCABABBABCBCBBCAB'
states = 'A   B   C'.split()

transition = np.zeros((len(states), len(states)))
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

emission = np.zeros((len(states), len(strings)))
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

with open("parameters.txt", 'w') as f1:
    f1.write('\t' + '\t'.join(states) + '\n')
    for i in range(len(states)):
        f1.write(states[i] + '\t' + '\t'.join(map(str, list(transition[i][:]))) + '\n')
    f1.write('-'*8 + '\n')
    f1.write('\t' + '\t'.join(strings) + '\n')
    for i in range(len(states)):
        f1.write(states[i] + '\t' + '\t'.join(map(str, list(emission[i][:]))) + '\n')
