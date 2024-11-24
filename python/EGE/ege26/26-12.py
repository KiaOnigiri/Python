f=open('26-12.txt')
s=f.read().splitlines()
space,n=[int(z) for z in s[0].split()]
s=s[1:]
s=[int(i) for i in s]
s.sort()
load=0
for i in range(len(s)):
    if load+s[i]>space:
        break
    load+=s[i]
print(i,load,s[i-1])
for z in range(i,i+200):
    print(s[z],s[z]-49)
#1551 51
