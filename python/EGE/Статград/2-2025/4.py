def Fano(n,c=''):
    if len(c)==n:
        return None
    else:
        if all(c+'0' != y[:len(c+'0')] and y != str(c+'0')[:len(y)] for y in fulldigit):
            f.append(c+'0')
        if all(c+'1' != y[:len(c+'1')] and y != str(c+'1')[:len(y)] for y in fulldigit):
            f.append(c+'1')
        Fano(n,c+'0')
        Fano(n,c+'1')
def Freedom():
    global f
    f=list(set(f)-set(fulldigit))
full='И – 00010, Н – 100, Ф – 11, О – 001,\
Р – 0000, М – 1010, А – 011, Т – 1011, К – 010'
full=full.split()
fulldigit=[]
for x in full:
    k=''
    for y in x:
        if y.isdigit()==True:
            k+=y
    if len(k)>0:
        fulldigit.append(k)
print(fulldigit)
        
f=[]
Fano(5)
Freedom()
f.sort(key=lambda x:(len(x),x))
'''
f1=[]
for ans in f:
    k=[1 for x in f if ans == x[:len(ans)]]
    if sum(k)<=1:
        f1.append(ans)'''
print(f)
#00011
