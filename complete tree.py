(n-1) - number of edges
# ~ l=[]
# ~ with open("rosalind_tree.txt") as f1:
    # ~ for line in f1:
        # ~ l.append(line.strip())
# ~ n = int(l.pop(0))

# ~ #count isolated nodes
# ~ t=0
# ~ nodes=[]
# ~ for i in l:
    # ~ nodes.append(i.split()[0])
    # ~ nodes.append(i.split()[1])
# ~ node = list(set(nodes))
# ~ if len(node) != n:
    # ~ for j in range(1, n+1):
        # ~ if str(j) not in node:
            # ~ t+=1

# ~ #count other taxa
# ~ taxa=[]
# ~ for k in l:
    # ~ a = k.split()[0]
    # ~ b = k.split()[1]
    # ~ flag=0
    # ~ for taxon in taxa:
        # ~ if (a in taxon) and (b not in taxon):
            # ~ flag=1
            # ~ taxon.append(b)
            # ~ break
        # ~ elif (a not in taxon) and (b in taxon):
            # ~ flag=1
            # ~ taxon.append(a)
            # ~ break
    # ~ if flag == 0:
        # ~ taxa.append([a, b])
        # ~ print(taxa)

# ~ t += len(taxa)
# ~ print(t-1)

# ~ su=0
# ~ for d in taxa:
    # ~ su += len(d)
# ~ print(su)
