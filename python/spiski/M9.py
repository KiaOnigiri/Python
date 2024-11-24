import random
n=10
a=[random.randint(-9,9) for x in range (n)]
print(a)
m=-10
gh=int(input())
kr=int(input('Введите {}, если хотите, чтобы число было отрицательным и {}, чтобы положительным)'.format(-1,1)
for i in range(len(a)):
    if a[i]<0 and a[i]%gh==0 and m<a[i]:
        m=a[i]
if m==-10:
    print('такого нет')
else:
    print(m)
print(kr)
print(gh)
