from math import ceil
for power in range(1,10):
    t=377*power
    t=ceil(t/8)
    if t*23155>5536*1024:
        print(power)
