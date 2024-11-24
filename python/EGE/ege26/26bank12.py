f=open('26bank12.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[[x for x in z.split()] for z in s]
s=[[int(z[0]),int(z[1]),z[2]] for z in s]
s.sort()
light=[]
microbus=[]
clv_mcr=0
clv_left=0
for i in range(1,2000):
    for car in s:
        if i==car[0]:
            if car[2]=='A':
                if len(light)>70:
                    if len(microbus)>30:
                        clv_left+=1
                        continue
                    microbus.append(car[0]+car[1])
                    continue
                light.append(car[0]+car[1])
            if car[2]=='B':
                if len(microbus)>30:
                    clv_left+=1
                    continue
                microbus.append(car[0]+car[1])
                clv_mcr+=1
        if i in light:
            light.remove(i)
        if i in microbus:
            microbus.remove(i)
print(clv_mcr,clv_left)
