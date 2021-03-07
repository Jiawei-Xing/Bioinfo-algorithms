import urllib.request
import re

#get fasta seqs from uniprot
ids=[]
with open('uniprot.txt') as f1:
    for line in f1:
        ids.append(line.strip())

seqs={}
for i in ids:
    seqs[i] = str(urllib.request.urlopen('http://www.uniprot.org/uniprot/' + i + '.fasta').read())

for i,j in seqs.items():
    seqs[i] = ''.join(j.split("\\n")[1:-1])

#find motif N{P}[ST]{P}
motif={}
for i,j in seqs.items():
    motif[i] = list(str(m.start()+1) for m in re.finditer('(?=N[^P][ST][^P])', j))
    

with open('motif.txt', 'w') as f2:
    for i,j in motif.items():
        if j != []:
            f2.write(i + "\n" + ' '.join(j) + "\n")
