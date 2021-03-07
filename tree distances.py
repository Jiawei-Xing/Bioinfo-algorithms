from Bio import Phylo
from io import StringIO

with open('rosalind_nkew.txt') as f1:
    f = f1.readlines()

trees=[]
nodes=[]
for i in range(0, len(f), 3):
    trees.append(f[i].strip())
    nodes.append(''.join(f[i+1].strip()))

distances=[]
for n in range(len(trees)):
    tree = Phylo.read(StringIO(trees[n]), 'newick')
    # ~ clades = tree.find_clades()
    # ~ for clade in clades:
        # ~ clade.branch_length = 1
    distances.append(str(int(tree.distance(nodes[n].split()[0], nodes[n].split()[1]))))
print((' '.join(distances)))

# ~ distances=[]
# ~ for n in range(len(trees)):
    # ~ d=0
    # ~ node1 = nodes[n].split()[0]
    # ~ node2 = nodes[n].split()[1]
    # ~ tree = trees[n]
    # ~ i = tree.find(node1)
    # ~ j = tree.find(node2)
    # ~ l = tree[i:j].count("(")
    # ~ r = tree[i:j].count(")")
    # ~ d += abs(l-r)
    # ~ if node1+";" in tree or node2+";" in tree:
        # ~ d += 1
    # ~ else:
        # ~ d += 2
    # ~ distances.append(str(d))

# ~ print(' '.join(distances))
