from functools import lru_cache
@lru_cache(None)
def recurs(x):
    if x==12:
        return 0
    if x==3:
        return 1
    if x<3:
        return 0
    b=[x-3]
    if x%2==0:
        b.append(x//2)
    else:
        b.append(x-5)
    return sum([recurs(y) for y in b])

print(recurs(36))
