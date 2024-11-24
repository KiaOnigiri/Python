a=[2526, 2527, 2528, 2530]
for i in range(len(a)-1):
    if a[i+1]-a[i]==1:
        print(a[i+1]+1,a[i+1]+2)
        if (a[i]-1) not in a and a[i]-2 in a:
           print(a[i]-1)
        if (a[i+1]+1) not in a and a[i+1]+2 in a:
            print(a[i+1]+1)
        if a[i]-1 in a and a[i]-2 not in a:
            print(a[i]-2)
        if a[i+1]+1 in a and a[i+1]+2 not in a:
            print(a[i+1]+2)
