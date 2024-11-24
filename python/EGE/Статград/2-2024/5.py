for n in range(100,20024):
    r=[int(str(n)[x]+str(n)[x+1]+str(n)[x+2]) for x in range(len(str(n))-2)]
    r=max(r)-min(r)
    if r==415:
        print(n)
        break
