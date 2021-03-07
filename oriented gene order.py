n=3
num = list(range(1,n+1)) + list(range(-n,0))
per = []
for i in num:
    for j in num:
        for k in num:
            if abs(i) != abs(j) and abs(i) != abs(k) and abs(j) != abs(k):
                per.append(str(i) + " " + str(j) + ' ' + str(k))

print(len(per))
for n in per:
    print(n)
