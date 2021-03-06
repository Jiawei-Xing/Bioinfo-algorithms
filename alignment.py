a = ''.join('''CVYGNVTDRQEYWQMAQKDRVIHTNTLLHSQKKLEYNFTVLHKYGMPTQNGQLDRGWRCC
NLTFYRIARANSALRAYLYAIWTKCDICDWNRYESPNKTTMWYTDIHQRDPHSIHAYQGK
KQTAATCQHQTDGFFTTRVRACDHMNRSRDDVVKKVAWPQWIAAIWSPMKMYNIVRMRNA
RIEPGYRNRQNPPEIYWYIYYMPNLLSPFQAEIRTLLNVMIYAHQEGWHHTLRMVFPWNI
KEQHHSIQSLLHRFRIYEKSHMHHNPKRKRCCGVYQTFCCVDFDAWLSDRACRTVLKCQM
VIFFKVCYCGNRRAYEYWRDCRPNQKVGMKLNHKFTIFWHYHPPHQVDKGGICWAVKQRC
CILKWIYIPMWNHDMRYDHYFRCPYWGNRMNTMGTPMFREMEWMMEHMQFQQMPLLTHIQ
FMPSTTHHANCIQVYNTECFMYTWMIMDFKGCFDKGAEVATPKMCGQSGRPCAVVSDPLA
RDNHQKYTDGGNTIWNLSMVSTESKEHRHDYNIFAIWWSGFNDHHMPCFMMANRHDGLHD
KDDWYREKRFHYEIEMWCVYVREVRAYFQFIGPWIHSSDFIWFCLGDNNKRMDTYGCGNK
TQDDKLAGYSDPFRTFLCFKPESLPAMYFTHQHKYMHFCWMCYFSTDEHCQHIMQYQHPN
TKQHWQLDNRSLQDKAMYYCWWKPVSPPASEHCSASGYCFHPKFSVQVVKDKGLNDMVHG
CGHQERPTSNANIFTMEPKFAYVIHMHYTIMPWYLISHPDEADFGLQGWEIFFKWEVFDM
WIQLCKGPWPKDDNPEYMMICHPWFYTVKQFLPYCQCNMPKMWEKQWYVMASKMCHTNYQ
AHGELDWGHMQEEIVYCAEALTCD'''.split())

b = ''.join('''CVYGMDRQEYAQMAQKDRVQHAICAKTNTVYMCIQIRDQINFYTGNNKDPDWGWQLDRGW
RCCNLTFYRIARANSARAYLYAIWTKTFLWSICDWMRYEIQKTCQHNTPDIWKTTMWYTD
IHEIFDSERDPHANIHAYQTKKQTAATCQHQTDGFFTTRVRACEKTIGDWLLHMNFSKKV
AWPQDETTNTIIMKMYNIVCVYNIAMRNCDRYLHYSRIEPGFRNRKENGIVNPPFESEIW
CCMEMWAQLSPFQAWIRTLLNQILKDMIYAHQSRWYMENEGWHCTYRMVFPANIHSIQSL
LHRRAVFMFRIYKETQNKGVYQTFCCVDFDADRPSKSQMILSERAVQSLCAKRMVIFFKV
CYCENRRAYSYWRDCRPRQKVGMKLNHYVPYHGVFFTIFIHYHPPFQVDKGGICWAVHQR
CCILKWIYMPWNHDIGWYDVSYDHYFRCPYWGNDSGVKKANTMGKHHAWWMQFQQMPLYT
HIQFMSQKRLPKSTTHHMICIIFWKPRNCTRYNTECFMYTWMIMDFKGCFIKGAEVATPQ
VGRPCVVSMPLARNHQKYEDFSMVSTESHDLQGNLNIFAIWWMKFDNGGFDTIFCGPQHH
MPCFMWWQMESGFSGDKLDWYREKRFEVTTYEIEQVYFYACSRCVGFVRAYIMWHGGEPQ
FLGPWIHSSDFIWYLEHCLGDNNKRMMTYGCGCQTQDSAGNSPFETFLCFKPEHFILPAM
YFAHQHKYMDWAAIEKKEFCWHFFHLARQHWYHMCGHCQHTPYSVICLNMQYQHPVYDLA
NTKQHWQLDPKHGTKSLQDAAMYYCWWKPHSYAPASYCFHPEFNVSVDKDKGLLDMVHSC
GHQERPTSNFTMEKFAYHIHMHYTIMAWYLISDPDEAHFGLQGWEEFFEWEEIQLCKGPW
PKDDNPEVKQFPYCQCNKPKMWEKVMASKMCHTNYQSHGELDWGHDQEEIVYCAEALTKD'''.split())

#edit distance
t=[[]]
for n in range(len(b)+1):
    t[0].append(n)
for i in range(1, len(a)+1):
    t.append([i] + [0]*len(b))
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            t[i][j] = t[i-1][j-1]
        else:
            t[i][j] = min(t[i-1][j], t[i][j-1], t[i-1][j-1]) + 1
print(t[len(a)][len(b)])

#alignment    
a_align=[]
b_align=[]
i=len(a)
j=len(b)
while i>0 and j>0:
    if a[i-1] == b[j-1]:
        a_align.insert(0, a[i-1])
        b_align.insert(0, b[j-1])
        i = i-1
        j = j-1
    elif t[i][j] == t[i][j-1] + 1:
        a_align.insert(0, '-')
        b_align.insert(0, b[j-1])
        j = j-1
    elif t[i][j] == t[i-1][j] + 1:
        a_align.insert(0, a[i-1])
        b_align.insert(0, '-')
        i = i-1
    elif t[i][j] == t[i-1][j-1] + 1:
        a_align.insert(0, a[i-1])
        b_align.insert(0, b[j-1])
        i = i-1
        j = j-1

print(''.join(a_align))
print(''.join(b_align))
