f=open('demo_2025_24.txt')
s=f.read()
s=s.replace('*-','A')
s=s.replace('--','A')
s=s.replace('**','A')
s=s.replace('-*','A')
s=s.replace('A*','A')
s=s.replace('A-','A')
s=s.replace('*00','*0A0')
s=s.replace('*06','*0A6')
s=s.replace('*07','*0A7')
s=s.replace('*08','*0A8')
s=s.replace('*09','*0A9')
s=s.replace('-00','-0A0')
s=s.replace('-06','-0A6')
s=s.replace('-07','-0A7')
s=s.replace('-08','-0A8')
s=s.replace('-09','-0A9')
while 'A00' in s:
    s=s.replace('A00','A0A0')
while 'A06' in s:
    s=s.replace('A06','A0A6')
while 'A07' in s:
    s=s.replace('A07','A0A7')
while 'A08' in s:
    s=s.replace('A08','A0A8')
while 'A09' in s:
    s=s.replace('A09','A0A9')
s=s.split('A')
s=sorted(s,key=len)
mx1=s[-1]
mx2=s[-2]
mx3=s[-3]
print(mx1,len(mx1))
print(mx2,len(mx2))
print(mx3,len(mx3))


