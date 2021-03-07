s = '''S H W Z C J M R O X A
'''.split()
s.insert(0, '')

# ~ # k=3
# ~ out=[]
# ~ for i in s[1:]:
    # ~ for j in s:
        # ~ if j != '':
            # ~ for k in s:
                    # ~ print(i+j+k)
        # ~ else:
            # ~ print(i)

# k=4
with open('out.txt', 'w') as f1:
    for i in s[1:]:
        for j in s:
            if j != '':
                for k in s:
                    if k != '':
                        for l in s:
                            f1.write(i+j+k+l+"\n")
                    else:
                        f1.write(i+j+"\n")
            else:
                f1.write(i+"\n")
