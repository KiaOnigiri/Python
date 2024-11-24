f=open('24-174.txt')
spisok=f.read().splitlines()
spisok=[g for g in spisok if g.count('R')<30]
kmax=0
ch=0
for s in spisok:   
    for i in range(len(s)):
        k=s[i]
        for j in range(i+1,len(s)):
            if s[j]==k:
                z=s[i:j+1]
                ch+=1
                if len(z)>kmax:
                    print(len(z),'!')
                    kmax=len(z)
                    m=z
                    q=s
                break
            
print(kmax,ch)
print(len('WAEGTKUOHBLYMKKKIDDSJTBGPPXAJVVVIIMCQYYLLAAAMKCOJIIAAGCCAUUXOCITTTSSZZEEEVCDDFPPFFCALJFSSVGCLPYOOVVVVDDYFFRHLOVKNUUYLVZEZSRFFHHQXPRRPPVARHGGQIIUXJKQQVBVUUEXXZKIIIEZXTTLBBBKBYYGJKMICJEEAAAMPNNNJKGUXQQTDMMMJQQQQIOBEEMIDDHDGIFCAJJMBRVVVCIEEXXJYSCTSMKECSVGUJQQKZEMTCDOJDYOYYCXKJLIXPNNSDHJTTYSRJXXYETATTCVTYLUUFTEZUBLNCYENJOKIMIIABSEENHFBADZMYPJSGGBBUNNQKFUGFEW'))
print(q)
print(q.count('R'))
