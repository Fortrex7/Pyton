word = input("Vvedite slovo: ") 
a, e, i, o, u = (0,) * 5
for letter in word:
    if letter == 'a' or letter == 'A':
        a += 1
    elif letter == 'e' or letter == 'E':
        e += 1
    elif letter == 'i' or letter == 'I':
        i += 1
    elif letter == 'o' or letter == 'O':
        o += 1
    elif letter == 'u' or letter == 'U':
        u += 1
print("Glasnyh: ", (a + e + i + o + u))
print("Soglasnyh: ", (len(word) - (a + e + i + o + u)))
print("Kolichestvo glasnyh po bukvam:")
if a == 0: 
    print("a = False")
else: print("a = ", a)
if e == 0: 
    print("e = False")
else: print("e = ", e)
if i == 0: 
    print("i = False")
else: print("i = ", i)
if o == 0: 
    print("o = False")
else: print("o = ", o)
if u == 0: 
    print("u = False")
else: print("u = ", u)