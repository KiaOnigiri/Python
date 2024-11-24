def combs(x):
    if x>24:
        return 0
    if x==24:
        return 1
    if x==11 or x==17:
        return 0
    if x<24:
        return combs(x+1)+combs(x+4)+combs(x*2)

print(combs(3))
