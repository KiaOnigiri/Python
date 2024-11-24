f=open('24-J4.txt')
s=f.read()
print(s.count('BOSS')-s.count('JBOSS')-s.count('BOSSJ')+s.count('JBOSSJ'))
