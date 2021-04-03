import itertools

k = 6
dna = '''TACCGTACTTAACAGACGTCTGACGCCCCTAATAACGGGCCA
TGAGCGTATGGCAAACAGATCCGGTAACTGCGGACTGCCCAT
GCTCCTGCGTCCTTGGACATCATCTCATGAGTAGTGGCCCAT
CGTGCTTGTACAAACTCGCCAAACATTTGACGGCTAGCCCAT
ACATAGGTACAGGTCGGTTCACATCGCAGAGCCCGTTGTGCC
TCCGTAAAGCCCATTAGAATAGATGCCCCTCTCGTCTCACGG
TGTGGATGGTGAACTAATACTCATGCCGCCGCCCTTCGCATA
GGCATCGCCCGTTAGCGCTGTTAAGTGCAGGAATCGCGCTAA
CGTGGATCATTAAGTTCAGCCCTTGGTCGAACTGCTGGGGCG
CCCGTAATGCTCGGTTGGCTTAGACTATGGGCCCATATGGTT'''.split()

bases = ['A', 'C', 'G', 'T']
kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]

out={}
for kmer in kmers:
    dd=0
    for string in dna:
        d=[]
        for i in range(len(string)-k+1):
            d.append(sum([x != y for x, y in zip(kmer, string[i:i+k])]))
        dd += min(d)
    out[kmer] = dd

for n in out:
    if out[n] == min(out.values()):
        print(n)
        break
