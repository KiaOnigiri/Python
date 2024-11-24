f=open('26.txt')
s=f.read().splitlines()
n=int(s[0])
s=[[int(y) for y in x.split()] for x in s[1:]]
s.sort(key = lambda x: x[1])
hall=[s[0]]
for event in s:
    begintime=event[0]
    timefree=hall[-1][1]
    if begintime-timefree>=15:
        hall.append(event)
predposl=hall[-2]
lasts=[]
for event in s:
    begintime=event[0]
    if begintime-predposl[1]>=15:
        lasts.append(begintime-predposl[1])
print(len(hall),max(lasts))
