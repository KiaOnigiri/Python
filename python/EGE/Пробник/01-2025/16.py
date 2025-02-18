def F(n):
    ans=1
    while n>=5:
        ans*=2*n
        n-=4
    ans*=n
    return ans
print((F(13766)-9*F(13762))/F(13758))
