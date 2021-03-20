a = '''GATTACA
TACTACTAC
ATTGAT
GAAGA
'''.strip().split()

b = sorted(list(map(len, a)))
b.reverse()

c=0
l = sum(b)
for n in b:
    c += n
    if c >= l/2:
        print(n)
        break
        
d=0
for m in b:
    d += m
    if d >= l*0.75:
        print(m)
        break
