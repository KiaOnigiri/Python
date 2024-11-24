v,m,z = [int(x) for x in input().split()]

s = 1
days = 0

while s<=z:
    s+=v
    days+=3
    if s<=z:
        s-=m
        days+=4
    else:
        print(days)
