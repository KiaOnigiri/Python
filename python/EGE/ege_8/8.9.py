c='012345678'
k=0
for x1 in c:
    for x2 in c:
        for x3 in c:
            for x4 in c:
                for x5 in c:
                    x=x1+x2+x3+x4+x5
                    if x1!='0' and x.count('3')==2 and all([j not in x for j in ['13','31','33','35','53','73','37']]):
                        k+=1
print(k)
#900
