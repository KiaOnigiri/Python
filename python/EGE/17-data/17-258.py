f=open('17-257.txt')
s=f.read().splitlines()
s=[int(z) for z in s]
mxC=max([z for z in s if z%2==0])
mxN=max([z for z in s if z%2!=0])
print(mxC,mxN)
sC=[z for z in s if z%2==0]
print(len(sC),min(sC))
