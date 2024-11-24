'''
def rever(x):
    x=str(x)
    x=x[::-1]
    x=int(x)
    x=str(x)
    x=x[::-1]
    x=int(x)
    return x


N=int(input())
k=0
for i in range(1,N+1):
    k+=rever(i)
print(k%1000000007)
'''

#формула арифметической прогрессии
n=int(input())
'''
n1=n//10
n2=n//100
n3=n//1000
n4=n//10000

k=(((1+n)*n)/2)-((9*(((1+n1)*(n1))/2))+(9*(((1+n2)*(n2))/2))+(9*(((1+n3)*(n3))/2))+(9*(((1+n4)*(n4))/2)))
'''
k=((1+n)*n)/2
print(k)
d=10
while len(str(d))!=len(str(n)):
    n1=n//d
    k-=(9*(((1+n1)*(n1))/2))
    print(k)
    d*=10
    

print(k%1000000007)
