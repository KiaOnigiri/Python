
for x in range(0,9+1):
    s=f'3{x}69064'
    if int(s)%2024==0:
        print(s)

for x in range(0,9+1):
    for y1 in range(0,9+1):
        s=f'3{x}6906{y1}4'
        if int(s)%2024==0:
            print(s)

for x in range(0,9+1):
    for y1 in range(0,9+1):
        for y2 in range(0,9+1):
            s=f'3{x}6906{y1}{y2}4'
            if int(s)%2024==0:
                print(s)

for x in range(0,9+1):
    for y1 in range(0,9+1):
        for y2 in range(0,9+1):
            for y3 in range(0,9+1):
                s=f'3{x}6906{y1}{y2}{y3}4'
                if int(s)%2024==0:
                    print(s)

