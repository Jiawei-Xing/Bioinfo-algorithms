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
Y   163.06333
"""
l = mass.split("\n")[:-1]
aa={}
for a in l:
    aa['%.5f' % float(a.split()[1])] = a.split()[0]

t=[]
with open("rosalind_full.txt") as f1:
    for line in f1:
        t.append(float(line.strip()))
t.sort()

out=[]
k=t[0]
for n in t[1:]:
        weight = '%.5f' % (n-k)
        if str(weight) in aa:
            out.append(aa[weight])
            k=n

print(''.join(out[:-1]))