def first_last(a):
    a=a.split()
    a[0]=a[0][::-1]
    a[-1]=a[-1][::-1]
    return ' '.join(a)


x=input('x=')
print(first_last(x))
