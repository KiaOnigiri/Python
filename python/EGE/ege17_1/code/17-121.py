b=[]
for i in range(198372,876194):
    if i%sum([int(x) for x in str(i)])==11:
        b.append(i)
print(len(b),max(b))
