from fnmatch import *
#30001050
for i in range(30001050,10**10+1,1917):
    if fnmatch(str(i),'3?12?14*5'):
        print(i,i//1917)
