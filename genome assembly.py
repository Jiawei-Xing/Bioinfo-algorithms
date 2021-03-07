#fasta
seqs={}
with open('rosalind_long.txt') as f1:
    for line in f1:
        if ">" in line:
            name = line.strip()[1:]
            seqs[name] = []
        else:
            seqs[name].append(line.strip())
seqsl=[]            
for seq in seqs.values():
    seqsl.append(''.join(seq))
# ~ print(seqsl)

#find start seq
for seq in seqsl:
    if len(seq) % 2 == 1:
        r = int(len(seq)//2+1)
    else:
        r = int(len(seq)/2+1)
    f = seq[:r]
    seqsl2 = seqsl[:]
    seqsl2.remove(seq)
    flag=0
    for seq2 in seqsl2:
        if f in seq2:
            flag=1
            break
    if flag == 0:
        s = seq
    # ~ for seq2 in seqsl:
        # ~ if seq2 == seq:
            # ~ if seq2 == seqsl[-1]:
                # ~ s = seq
            # ~ else:
                # ~ continue
        # ~ elif f in seq2:
            # ~ i = seq2.rfind(f)
            # ~ if seq2[i:] == seq[:len(seq[i:])]:
                # ~ break
            # ~ elif seq2 == seqsl[-1]:
                # ~ s = seq
        # ~ elif seq2 == seqsl[-1]:
            # ~ s = seq
# ~ print(s)
            
# ~ #find end seq
for seq in seqsl:
    if len(seq) % 2 == 1:
        r = int(len(seq)//2)
    else:
        r = int(len(seq)/2-1)
    f = seq[r:]
    seqsl2 = seqsl[:]
    seqsl2.remove(seq)
    flag=0
    for seq2 in seqsl2:
        if f in seq2:
            flag=1
            break
    if flag == 0:
        e = seq
    # ~ for seq2 in seqsl:
        # ~ if seq2 == seq:
            # ~ if seq2 == seqsl[-1]:
                # ~ e = seq
            # ~ else:
                # ~ continue
        # ~ elif f in seq2:
            # ~ i = seq2.find(f)
            # ~ if seq[r-i:] == seq2[:i+len(f)]:
                # ~ break
            # ~ elif seq2 == seqsl[-1]:
                # ~ e = seq
        # ~ elif seq2 == seqsl[-1]:
            # ~ e = seq
# ~ print(e)

#find overlaps
def assembly(seq, spstr):
    if seq == e:
        return spstr
    elif len(seq) % 2 == 1:
        r = int(len(seq)//2)
    else:
        r = int(len(seq)/2-1)
    f = seq[r:]
    seqsl2 = seqsl[:]
    seqsl2.remove(seq)
    for seq2 in seqsl2:
        if f in seq2:
            i = seq2.find(f)
            spstr += seq2[i+len(f):]
            return assembly(seq2, spstr)
    # ~ for seq2 in seqsl:
        # ~ if seq2 == seq:
            # ~ continue
        # ~ elif f in seq2:
            # ~ i = seq2.find(f)
            # ~ if seq[r-i:] == seq2[:i+len(f)]:
                # ~ spstr += seq2[i+len(f):]
                # ~ return assembly(seq2, spstr)

print(assembly(s, s))
