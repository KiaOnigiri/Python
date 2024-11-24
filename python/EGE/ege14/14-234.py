def inAny(x,y):
    m=''
    while x>1:
        m+=str(x%y)
        x//=y
    return m


s=5*6561**46+5*729**15-5*5832-5
print(inAny(s,9).count('4'))
