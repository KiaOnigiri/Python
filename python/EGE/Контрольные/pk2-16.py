def F(n):
    if n==1 or n==2:
        return n
    else:
        return n*(n-1)*F(n-1)
print(F(123)/F(120))
#3216449665440
