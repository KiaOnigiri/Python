H=int(input())
M=int(input())
A=int(input())
B=int(input())
if (H*60+M)%A==0:
    a1=0
else:
    a1=A
if (H*60+M)%B==0:
    b1=0
else:
    b1=B
if (H==22 and M!=0) or H==23:
    print(-1)
elif H>=8:
    print(min(((H*60+M)//A)*A+a1-(H*60+M),((H*60+M)//B)*B+b1-(H*60+M)))
else:
    print(480-(H*60+M))
