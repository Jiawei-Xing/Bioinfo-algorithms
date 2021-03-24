data = '''ECDCC-ABD
EADC-B-BD
EADB-BBBD
E---C-C-D
EADCCACBB
EADCCB-B-
E--CCBBB-
EAB-CBBBD
AAD-CBBBC
EADCCBBBD'''.split()

msa=[]
for n in data:
    msa.append("^" + n + "$")
    
states = 'A B C'.split()

# insertion sites
theta = 0.254
insert=[]
not_insert=[]
for i in range(len(msa[0])):
    c=0
    for n in msa:
        if n[i] == '-':
            c+=1
    if c/len(msa) < theta:
        not_insert.append(i)
    else:
        insert.append(i)

# not insertion site i
def p_not_insert(i):
    dd=0
    md=0
    mm=0
    dm=0
    for n in msa:
        if n[i] == '-':
            if n[i-1] == '-':
                dd+=1
            else:
                md+=1
        else:
            if n[i-1] == '-':
                dm+=1
            else:
                mm+=1
    if mm:
        output['M'+str(not_insert.index(i)-1)]['M'+str(not_insert.index(i))] = mm/(mm+md)
    if md:
        output['M'+str(not_insert.index(i)-1)]['D'+str(not_insert.index(i))] = md/(mm+md)
    if dm:
        output['D'+str(not_insert.index(i)-1)]['M'+str(not_insert.index(i))] = dm/(dm+dd)
    if dd:
        output['D'+str(not_insert.index(i)-1)]['D'+str(not_insert.index(i))] = dd/(dm+dd)

# insertion starting site i
def p_insert(i):
    j = not_insert[not_insert.index(i-1)+1]
    c=[]
    mm=0
    md=0
    dm=0
    dd=0
    mi=0
    di=0
    for n in msa:
        c.append(j - i - n[i:j].count('-'))
        if j-i == n[i:j].count('-'):
            if n[i-1] == '-':
                if n[j] == '-':
                    dd+=1
                else:
                    dm+=1
            else:
                if n[j] == '-':
                    md+=1
                else:
                    mm+=1
        else:
            if n[i-1] == '-':
                di+=1
            else:
                mi+=1
    if di:
        output['D'+str(not_insert.index(i-1))]['I'+str(not_insert.index(i-1))] = di/(dd+dm+di)
    if mi:
        output['M'+str(not_insert.index(i-1))]['I'+str(not_insert.index(i-1))] = mi/(mi+mm+md)
    if sum(c)-(len(msa)-dd-dm-md-mm):
        output['I'+str(not_insert.index(i-1))]['I'+str(not_insert.index(i-1))] = 1-(len(msa)-dd-dm-md-mm)/sum(c)
    if dd:
        output['D'+str(not_insert.index(i-1))]['D'+str(not_insert.index(i-1)+1)] = dd/(dd+dm+di)
    if dm:
        output['D'+str(not_insert.index(i-1))]['M'+str(not_insert.index(i-1)+1)] = dm/(dd+dm+di)
    if md:
        output['M'+str(not_insert.index(i-1))]['D'+str(not_insert.index(i-1)+1)] = md/(md+mm+mi)
    if mm:
        output['M'+str(not_insert.index(i-1))]['M'+str(not_insert.index(i-1)+1)] = mm/(md+mm+mi)
    output['I'+str(not_insert.index(i-1))]['M'+str(not_insert.index(i-1)+1)] = (len(msa)-dd-dm-md-mm)/sum(c)

# transition probability matrix
output={}
output['M0']={}
output['I0']={}
for i in range(1, len(not_insert)-1):
    output['M'+str(i)]={}
    output['D'+str(i)]={}
    output['I'+str(i)]={}
output['M'+str(len(not_insert)-1)]={}

for k in output:
    for l in output:
        output[k][l]=0

for i in range(1, len(msa[0])):
    if i in not_insert:
        if i-1 in not_insert:
            p_not_insert(i)
    else:
        if i-1 not in insert:
            p_insert(i)

# emission probability matrix
output2={}
output2['M0']={}
output2['I0']={}
for i in range(1, len(not_insert)-1):
    output2['M'+str(i)]={}
    output2['D'+str(i)]={}
    output2['I'+str(i)]={}
output2['M'+str(len(not_insert)-1)]={}

for k in output2:
    for s in states:
        output2[k][s]=0

for i in not_insert:
    if i-1 in not_insert:
        s=[]
        for n in msa:
            s.append(n[i])
        for state in states:
            output2['M'+str(not_insert.index(i))][state] = s.count(state)/(len(msa)-s.count('-'))

for i in insert:
    if i-1 not in insert:
        j = not_insert[not_insert.index(i-1)+1]
        s=''
        for n in msa:
            s += n[i:j]
        for state in states:
            output2['I'+str(not_insert.index(i-1))][state] = s.count(state)/(len(s)-s.count('-'))
        s=[]
        for n in msa:
            s.append(n[j])
        for state in states:
            output2['M'+str(not_insert.index(i-1)+1)][state] = s.count(state)/(len(msa)-s.count('-'))


# add pseudocount to each possible value before normalization.
sigma=0.01
s = output['M0']['I0'] + output['M0']['M1'] + output['M0']['D1'] + 3*sigma
output['M0']['I0'] = (output['M0']['I0']+sigma)/s
output['M0']['M1'] = (output['M0']['M1']+sigma)/s
output['M0']['D1'] = (output['M0']['D1']+sigma)/s
s = output['I0']['I0'] + output['I0']['M1'] + output['I0']['D1'] + 3*sigma
output['I0']['I0'] = (output['I0']['I0']+sigma)/s
output['I0']['M1'] = (output['I0']['M1']+sigma)/s
output['I0']['D1'] = (output['I0']['D1']+sigma)/s

s = output['M'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)] + output['M'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)] + 2*sigma
output['M'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)] = (output['M'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)]+sigma)/s
output['M'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)] = (output['M'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)]+sigma)/s
s = output['D'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)] + output['D'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)] + 2*sigma
output['D'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)] = (output['D'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)]+sigma)/s
output['D'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)] = (output['D'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)]+sigma)/s
s = output['I'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)] + output['I'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)] + 2*sigma
output['I'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)] = (output['I'+str(len(not_insert)-2)]['I'+str(len(not_insert)-2)]+sigma)/s
output['I'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)] = (output['I'+str(len(not_insert)-2)]['M'+str(len(not_insert)-1)]+sigma)/s

for i in range(1, len(not_insert)-2):
    for n in ['M', 'D', 'I']:
        s = output[n+str(i)]['I'+str(i)] + output[n+str(i)]['M'+str(i+1)] + output[n+str(i)]['D'+str(i+1)] + 3*sigma
        output[n+str(i)]['I'+str(i)] = (output[n+str(i)]['I'+str(i)]+sigma)/s
        output[n+str(i)]['M'+str(i+1)] = (output[n+str(i)]['M'+str(i+1)]+sigma)/s
        output[n+str(i)]['D'+str(i+1)] = (output[n+str(i)]['D'+str(i+1)]+sigma)/s
        
for m in output2:
    if m == 'M0' or 'D' in m or m == 'M'+str(len(not_insert)-1):
        continue
    else:
        s = sum(output2[m].values()) + len(states)*sigma
        for n in states:
            output2[m][n] = (output2[m][n]+sigma)/s
            
# output matrices
with open('matrices.txt', 'w') as f1:
    f1.write('\t')
    f1.write('\t'.join(list(output.keys())))
    f1.write('\n')
    for k in output:
        f1.write(k)
        for l in output:
            f1.write('\t'+str(output[k][l]))
        f1.write('\n')
    f1.write('-'*8+'\n')
    f1.write('\t')
    f1.write('\t'.join(states))
    f1.write('\n')
    for k in output2:
        f1.write(k)
        for l in states:
            f1.write('\t'+str(output2[k][l]))
        f1.write('\n')
        
# finally, change M0 to S; Mlast to E. 
