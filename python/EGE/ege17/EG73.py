def raz(x):
    g=[int(z) for z in str(x)]
    return max(g)-min(g)


b=[]
for i in range(1005,147870):
    if '1' not in str(i) and raz(i)<4:
        b.append(i)
b.reverse()
print(len(b),b[24])
