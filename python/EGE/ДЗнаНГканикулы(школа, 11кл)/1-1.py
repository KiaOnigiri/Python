s='0123456789'
for i in range(ord('A'),ord('A')+8):
    s+=chr(i)
#print(s[1:])
cnt=0
for x1 in s[1:]:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        x=x1+x2+x3+x4+x5+x6
                        if sum([1 for smth in x if smth.isalpha() or int(smth)>7])<=2 and x.count('3')==1:
                            cnt+=1
print(cnt)
#2651537
