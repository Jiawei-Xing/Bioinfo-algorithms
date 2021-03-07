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
    aa['%.2f' % float(a.split()[1])] = a.split()[0]

prefix=[]
with open("rosalind_spec.txt") as f1:
    for line in f1:
        prefix.append(line.strip())

out=[]
k=prefix[0]
for n in prefix[1:]:
    weight = '%.2f' % float(float(n)-float(k))
    print(weight)
    out.append(aa[weight])
    k=n
print(''.join(out))
