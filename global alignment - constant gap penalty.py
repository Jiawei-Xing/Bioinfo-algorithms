a = ''.join('''YFFITESGQSLSCVCYSKNNENENFFQMLLWICFLSKYLPHLYVKFHDRGWLCYIVIDFP
QDRVGVGTPTTCIETFPIWAKVFLFRCPSVCKLPQMIWRPTLLLPWNSECYNKQCMRMWT
TSIQGLEFHHYSLREYDGINWLRAMRCLLKGQLMGLEQCSLDKPFDVEEHWVSLEHTTNY
WGKGNWDKTQRIEVIAKNSTQWFHMPWHFIMKQTIPKGCGYESGFEGTVVFVLGSITWYE
KASLCLNMVSVISDMHEGIVGILDREHLMTQRTCCMAWYTQMQRQKPTTTWPNHYQTKLV
VMNMMPCKEYFRFAIVRCFPLHIIHMNLYCYALHANLKYFPWKYSWRENVMQYAIVKPLH
GMWWRITPIQRDENQNLNNWHGASVTSDDKNTKYPFHVQSTLVKPDNMHGQYAAQAFLKF
VVYPRQLSFQAYIPNSMPWWGDAAKNYILTVGCDGCDAHFVRMNAYAKDCKVFWFEEFQP
QYPAGRNVLKVSCMISQMTPVFMTCPVHMANIERIVACAHSIGPSHKRSSRQLESSQDDC
AVPFERKTVRTKQHKTSFLIRCGLHCSNVCESFAHGKGMSYNDEFACAFEIIEQGVSEHH
EGYVNYRKFNIVGTIGFRHSEYAEAFTEQGAPGNFAYSYHVGLTTSCASHTWYSPNPRFI
AGNTYQAECMFDISPYQEVHYDTNCPVTQNTYGMIGDWIVNRAAAPSEEAVHQRMWLMCK
DTYCQEQQAILWKVEMHHHSVVCMMLIHTREWLFYNCCHGQKLQRSVWMPDKHASKNWFG
FGAGENDDWKSYTEPIDMWDDLSQEPLQITCTSKTHSFIPASSESAGPVEKGMTVNNFEE
RSFARHIAYFAAFMIRSMCWKHWGPQLHIASFGYAMLQYCTDISELLVGQ'''.split())

b = ''.join('''YFFITFTWSESGMVRHQTLSENRNFFQMVHPCICFLSKYLPHQWPIRTEYGCGWLCYIVI
FMFVQKRNQWAQTCIETFPIWAKMFLNLYTRPQMIWRPTLLFPWNSECYNSQCDRMWTLE
FHHYSLREVDYWINDLRKMMGLEQCSLDMAYDCTHALEHTTNYWGKGNWTQIGEPKIEVI
AKNSTQWMHIPDHFIMKQTIPGFEGTVVFVLGSIGGKWYDFGYSCKASLCLNMVSVQSDM
HEPYNPIVGENKLDREHLQLTQRCSMARIHNYTTTPNHYQTKLVENPTEASGIFYDRFAT
VVCVCLGKCFPAHIIHMSLYCYALIRGRPPDHFANLKYFNDCFYYAINNNKPLLYEPGHT
GMWWRITYILSKWIQCDEYFSMLHPMQNLNNWHGASVTSDDKNTAPYDMYSPYPFHVTST
LVKPDNMWGQMQVAQAFLTFVVYPRQLSFQAYSPNAAKLHFWTPQCVSVDCKVFWFEEFQ
PQYPAGLMGGMRNVEKVSCMISQMTCGWTYMNVMFMTCTVHMANITRSVACAHSIGWSSH
CMKPMWHLQLESSQDDDAVPFNCQHWMRKTVRNGQHKTWMYNTRKLIRCGLHCSNVCESF
AHGKGMSYNDEEIEQGVSEHHTGKHELKAGYVNYRKFHIVGTIGFSGARYEAFDEQGAPG
NFAASTHNYQGECMFDISPHYDTNCPVTGNLYGMIGDILADDREFGVNRAAAPSEEKRWL
MPHQWWCSTMAYMASPVDQAIWKVEPNDHHLVHTREWLNCCVKQKLHFRSVWMPPVLCIG
PKAVSKNWFGAGENDPPKSGFQDNQYKTEPIDMWDDLTQNPLMITWTGKTHSQTLYFTRP
PASSESAGPVEKGMTVNNDSLERSFAHIAYVLAFNIFPHYMIRSMCWKHWGPQLHGIHPE
ASFGPFMLQYCTDISELLVGQ'''.split())

BLOSUM62 = '''A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7'''.split('\n')

for i in range(len(BLOSUM62)):
    BLOSUM62[i] = BLOSUM62[i].split()

m={}
for i in range(len(BLOSUM62)):
    for j in range(1, len(BLOSUM62[0])):
        m[BLOSUM62[i][0] + '\t' + BLOSUM62[j-1][0]] = int(BLOSUM62[i][j])

#middle matrix, upper matrix and lower matrix
mid=[[0]]
for j in range(1, len(b)+1):
    mid[0].append(-5)
for i in range(1, len(a)+1):
    mid.append([-5] + [0]*len(b))

up=[[-100]]
for j in range(1, len(b)+1):
    up[0].append(-5)
for i in range(1, len(a)+1):
    up.append([-100] + [0]*len(b))

low=[[-100]*(len(b)+1)]
for j in range(1, len(a)+1):
    low.append([-5] + [0]*len(b))

#calculate scores
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        up[i][j] = max(up[i][j-1], mid[i][j-1]-5)
        low[i][j] = max(low[i-1][j], mid[i-1][j]-5)
        mid[i][j] = max(up[i][j], low[i][j], mid[i-1][j-1] + m[a[i-1]+'\t'+b[j-1]])

print(mid[len(a)][len(b)])
