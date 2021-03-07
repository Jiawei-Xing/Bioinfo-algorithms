c = 'A B C D'.split()

for i in c:
    out = ''
    out += i
    for j in c:
        out += j
        for k in c:
            out += k
            for q in c:
                out += q
                print(out)
                out = out[:-1]
            out = out[:-1]
        out = out[:-1]
    out = out[:-1]
