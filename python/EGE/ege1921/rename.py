from os import *
dirr='C:/python/EGE/ege1921/'
for flnm in listdir(dirr):
    flnm=flnm[:-3]
    if flnm[0]=='-':
        rename(flnm+'.py',flnm[1:]+'.py')
    
