g=0
for x in '0123456789ABCDEFGHI':
    if (int(f'98897{x}21',19)+int(f'2{x}923',19))%18==0:
        g=(int(f'98897{x}21',19)+int(f'2{x}923',19))/18
print(g)
#469034148
