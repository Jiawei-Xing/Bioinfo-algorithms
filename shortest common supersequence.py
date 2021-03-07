#longest common subsequence
def subseq(a, b):
    # t stores the length of lgsq
    t = [[0]*(len(b)+1)]
    add=[]
    for i in range(1, len(a)+1):
        t.append([0]*(len(b)+1))
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                t[i][j] = t[i-1][j-1] + 1
                add.append([i, j])
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    # find the elements of lgsq
    sub = ''
    i, j = len(a), len(b)
    a_i=[]
    b_j=[]
    while t[i][j] > 0:
        if [i, j] in add:
            sub += a[i-1]
            a_i.insert(0, i-1)
            b_j.insert(0, j-1)
            i-=1
            j-=1
        elif t[i-1][j] > t[i][j-1]:
            i-=1
        else:
            j-=1
    return sub[::-1], a_i, b_j


#shortest common supersequence
def superseq(a, b):
    sub, a_i, b_j = subseq(a, b)
    supe=[]
    i=0
    j=0
    for n in range(len(a_i)):
        k = a_i[n]
        l = b_j[n]
        supe.append(a[i:k])
        supe.append(b[j:l+1])
        i = k+1
        j = l+1
    if a[a_i[-1]] != a[-1] or b[b_j[-1]] != b[-1]:
        supe.append(a[a_i[-1]+1:])
        supe.append(b[b_j[-1]+1:])
    return ''.join(supe)


a = 'ACTCTTCCACCCAGACCTTCAGTCTCAGCCCTCTCATAAAGAAGAGTGGGCAATTATGATTGTCCTGAAGAACTGCCTGTCGGTCTGT'
b = 'CCATTTAGAATCCCAGAGATCCTGAGCCAGAGCCGGGCGTTACCCGTGGACAAGTCTACCTCGGCCGCGCCTAAAGCGGAATC'
print(superseq(a, b))
