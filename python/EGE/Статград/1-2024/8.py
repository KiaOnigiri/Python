def podhodit(x):
    for i in range(len(x)-1):
        sm=int(x[i])+int(x[i+1])
        if sm%2==0 and int(x[i])>=int(x[i+1]):
            return False
        if sm%2!=0 and int(x[i])<=int(x[i+1]):
            return False
    return True


a=(26,63,30,2630,26308,2638)
print([podhodit(str(x)) for x in a])
            
