#simple code that counts the frequencies of characters
word = 'bbbbaaa'
d = dict()
for c in word:
    #if c not in d:
    #    d[c] = 1
    #else:
    #    d[c] = d[c] + 1
    d[c] = d.get(c, 0) + 1
print(d)
