def test(s):
    for i in range(len(s)-2):
        k=s[i]+s[i+1]+s[i+2]
        if k in s[i+3:]:
            return False
    return True


f=open('24-173.txt')
s=f.read()
print('len=',len(s))
kmax=0
for i1 in range(len(s)-1):
    if i1%100==0:
        print(i1)
    for i2 in range(len(s),i1-1,-1):
        c=s[i1:i2+1]
        if test(c)==True:
            if len(c)>kmax:
                kmax=len(c)
                m=c
            break
print(m,kmax)
print(len('WAEGTKUOHBLYMKKKIDDSJTBGPPXAJVVVIIMCQYYLLAAAMKCOJIIAAGCCAUUXOCITTTSSZZEEEVCDDFPPFFCALJFSSVGCLPYOOVVVVDDYFFRHLOVKNUUYLVZEZSRFFHHQXPRRPPVARHGGQIIUXJKQQVBVUUEXXZKIIIEZXTTLBBBKBYYGJKMICJEEAAAMPNNNJKGUXQQTDMMMJQQQQIOBEEMIDDHDGIFCAJJMBRVVVCIEEXXJYSCTSMKECSVGUJQQKZEMTCDOJDYOYYCXKJLIXPNNSDHJTTYSRJXXYETATTCVTYLUUFTEZUBLNCYENJOKIMIIABSEENHFBADZMYPJSGGBBUNNQKFUGFEW'))
