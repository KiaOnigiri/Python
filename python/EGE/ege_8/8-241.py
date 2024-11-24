def ryadom(x):
    d='МКТ'
    f='АИ'
    for i in range(len(x)-1):
        if (x[i] in d and x[i+1] in d) or (x[i] in f and x[i+1] in f):
            return True
    return False


from itertools import *
x=permutations('АММИАКАТ')
x=set(x)
x=[z for z in x if ryadom(z)]
print(len(x))
