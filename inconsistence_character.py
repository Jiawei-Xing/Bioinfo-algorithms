characters = '''100001
000110
111000
100111
'''.strip().split()

def c1_c0(character):
    c1=[]
    c0=[]
    for i in range(len(character)):
        if character[i] == '1':
            c1.append(i)
        else:
            c0.append(i)
    return set(c1), set(c0)

# Compare the first character with other characters. 
# Break when inconsistent character is found. 
# Warning: does not work if the first character itself is inconsistent.     
c1, c0 = c1_c0(characters[0])
for n in characters[1:]:
    d1, d0 = c1_c0(n)
    if c1 & d1 and c1 & d0 and c0 & d1 and c0 & d0:
        print("inconsistent")
        break
    else:
        print("consistent")

characters.remove(n)
for m in characters:
    print(m)
