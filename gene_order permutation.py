from itertools import permutations

perm = list(permutations(range(1,6)))

print(len(perm))
for i in perm:
    per = []
    for n in i:
        per.append(str(n))
    print(' '.join(per))
    
