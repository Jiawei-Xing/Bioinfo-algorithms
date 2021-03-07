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
    aa[float('%.2f' % float(a.split()[1]))] = a.split()[0]
    
L=[]
with open('rosalind_sgra.txt') as f1:
    for line in f1:
        L.append(float(line.strip()))

#directed acyclic graph
graph={}        
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        w = float('%.2f' % float(L[j]-L[i]))
        if w in aa:
            graph[i, j] = aa[w]

def DAG_path(node, graph=graph, d={}):
    if node in d:
        return d[node]
    temp=[]
    for n in graph.keys():
        if node == n[0]:
            temp.append(graph[n] + DAG_path(n[1]))
    if temp:
        d[node] = max(temp, key=len)
        return d[node]
    else:
        d[node] = ''
        return ''

out=[]
for node in range(len(L)):
    out.append(DAG_path(node))
    
print(max(out, key=len))
