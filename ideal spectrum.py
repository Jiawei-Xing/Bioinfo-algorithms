mass  = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333""".split("\n")
aa={}
for a in mass:
    aa[int(float(a.split()[1]))] = a.split()[0]

L = list(map(int, '87 97 200 226 363 373 476 486 604 614 717 743 848 871 968 1004 1091 1115 1206 1218 1346 1353 1481 1493 1584 1608 1695 1731 1828 1851 1956 1982 2085 2095 2213 2223 2326 2336 2473 2499 2602 2612 2699'.split()))
L.insert(0,0)

# create a directed acyclic graph
graph={}        
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        w = L[j]-L[i]
        if w in aa:
            if i in graph:
                graph[i].append(j)
            else:
                graph[i] = [j]

# find all paths in the graph
def DAG_path(path, paths=[]):
    if path[-1] in graph:
        for n in graph[path[-1]]:
            paths = DAG_path(path=path+[n], paths=paths)
    else:
        paths.append(path)
    return paths

# find ideal spectrum from paths
paths = DAG_path(path=[0])
for m in paths:
    p=[]
    i=0
    for j in m:
        p.append(L[j] - L[i])
        i = j
        
    s=[]
    for k in range(1, len(p)):
        s.append(sum(p[:k]))
        s.append(sum(p[k:]))
    s.sort()
    if s == L:
        break

# print peptide
out=[]
for i in p[1:]:
    out.append(aa[i])
print(''.join(map(str, out)))
