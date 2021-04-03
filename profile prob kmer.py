string = 'CTAGATCTTTTTCGCTAAACTAGGATGTTCTGAGTACGGTGTATGATAAAAGGACTGAGCAAAGCGAACAGGTTACGGGTTAGTACTCGTGCCGGAGGACGCGTGATGCTGGTTCCAGCCACAACACCCACAATCCGCGTCATAGGGTTGGTCCGCTTCGGTCCACAGTTTGCTCCGTCCGGCAACCCTGTAAGGGAAAT'
k = 7
profile = '''0.214 0.286 0.321 0.25 0.107 0.25 0.179
0.143 0.214 0.214 0.143 0.393 0.286 0.25
0.429 0.321 0.321 0.357 0.286 0.25 0.286
0.214 0.179 0.143 0.25 0.214 0.214 0.286'''.split('\n')

profile = [n.split() for n in profile]
prob=[]
for i in range(len(string)-k+1):
    kmer = string[i:i+k]
    p = 1
    for j in range(k):
        if kmer[j] == 'A':
            p *= float(profile[0][j])
        elif kmer[j] == 'C':
            p *= float(profile[1][j])
        elif kmer[j] == 'G':
            p *= float(profile[2][j])
        else:
            p *= float(profile[3][j])
    prob.append((kmer, p))

print(max(prob, key = lambda x: x[1])[0])
