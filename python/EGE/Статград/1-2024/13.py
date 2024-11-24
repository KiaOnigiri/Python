def factorial(x):
    if x<=1:
        return x
    else:
        return factorial(x-1)*x


def CNK(n,k):
    return (factorial(n)/((factorial(k)*factorial(n-k))))

c=[1,3,5,7,9,11,13]
k=0
for p in c:
    k+=CNK(14,p)
print(k)
