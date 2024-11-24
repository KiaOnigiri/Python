from random import *
from time import *
nums=[]
for i in range(1000000):
    nums.append(randint(-300000000,300000000))
target=nums[randint(0,1000000)]+nums[randint(0,1000000)]
t1=time()

for i in range(len(nums)):
    if (target-nums[i]) in nums[:i]+nums[i+1:]:
        t2=time()
        print(sorted([nums.index(nums[i]),nums.index(target-nums[i],i+1)]),t2-t1)
        break
print('=========')
t3=time()
for x in range(len(nums)):
    for y in range(len(nums)):
        xi = nums[x]
        yi = nums[y]
        if x != y and xi+yi == target:
            t4=time()
            print([x,y],t4-t3)
