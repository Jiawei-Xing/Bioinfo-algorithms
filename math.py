#!python2

import math

#RNA structure perfect match
rna = 'UUGACUUCUGUCAAAGAGACGCACCGCCCGUCAAUAUCGUGUGGGGAGUACGGUACCUCUCAUUAACGGCAG'
a = rna.count('A')
g = rna.count('G')
n = math.factorial(a) * math.factorial(g)
print(n)

#partial permutation
def pper(n, k):
    p = math.factorial(n) / math.factorial(n-k)
    return p
    
print(int(pper(94, 9)%1000000))

#random strings
dna = 'AACTATAGTCTCTCTAACCGGTACCCAACGTCGCTTAGATATCATTTACACGTGTGCCGTGGGGTCAGACGAGGCGCTTTTATGTGTATAGCCCAT'
p_in = '0.094 0.162 0.216 0.246 0.294 0.355 0.409 0.488 0.550 0.586 0.634 0.714 0.777 0.824 0.837 0.897'.split()
p_out = []
i = dna.count('A') + dna.count('T')
j = dna.count('G') + dna.count('C')
for n in p_in:
    gc = float(n)/2
    at = (1-float(n))/2
    p_out.append(str(math.log(gc**j * at**i, 10)))
    
print(' '.join(p_out))


#Max matching RNA structure
rna='GUGUGGUCGCACCAGGAGGAGAUCAUGGACUGGCCUGGGCCCGACAAGCAGUUAGCCGCAGACAAGGCGAAGGGAAUAUCCGUUUUAUUU'
a = rna.count('A')
u = rna.count('U')
c = rna.count('C')
g = rna.count('G')

i = math.factorial(max(a, u)) / math.factorial(max(a,u) - min(a,u))
j = math.factorial(max(c, g)) / math.factorial(max(c,g) - min(c,g))
print(int(i * j))

#alternative splicing
m=928
n=1999
c=0
for k in range(m, n+1):
    c += math.factorial(n) // (math.factorial(n-k) * math.factorial(k))
print(int(c) % 1000000)


#expected number of restriction sites (二项分布期望=np)
def combination(n, r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

s = 'GTACACATG'    
n = 895811 - len(s) + 1
GC = '0.000 0.056 0.133 0.205 0.224 0.284 0.323 0.392 0.426 0.482 0.566 0.613 0.680 0.726 0.789 0.838 0.879 0.896 1.000'.split()
out=[]
for gc in GC:
    Pgc = float(gc)/2
    Pat = (1-float(gc))/2
    ngc = s.count('G') + s.count('C')
    nat = s.count('A') + s.count('T')
    p = Pgc**ngc * Pat**nat
    # ~ e = 0
    # ~ for i in range(n):
        # ~ e += i * combination(n, i) * p**i * (1-p)**(n-i)
    # ~ out.append(str(e))
    out.append(str(n*p))
print(' '.join(out))
print('\n')

#independent segregation
n=47
p=1/2
a=[]
for i in range(1, 2*n+1):
    a.append(combination(2*n, i) * p**i * (1-p)**(2*n-i))

out=[]
for j in range(2*n):
    out.append(sum(a[j:]))

print(' '.join([str(math.log(i, 10)) for i in out]))

# ~ import math

# ~ def binomial(n, k, p):
    # ~ return (math.factorial(n) / math.factorial(k) / math.factorial(n-k)) * (p**k * (1-p)**(n-k))

# ~ n = 5

# ~ prob = []
# ~ for k in range(2*n, -1, -1):
    # ~ prob = prob + [binomial(n*2, k, 0.5)]
# ~ print(prob)
# ~ prob = [math.log10(sum(prob[:i])) for i in range(2*n, 0, -1)]

# ~ print(' '.join([str(i) for i in prob]))


#count unrooted trees
n=951
print(math.prod(range(2*n-5, 0, -2)) % 1000000)

#count quartets
print(int(combination(4890, 4)%1000000))

#count rooted trees
print(math.prod(range(2*998-3, 0, -2)) % 1000000)
