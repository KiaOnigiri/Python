a=int(input())
r=[int(x) for x in str(a)]
r.sort(reverse=True)
print(*r, sep='')
