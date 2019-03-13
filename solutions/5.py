f=open('../inputs/5.txt')
for w in f:
 a=range(1,len(w))
 r=a[::-1]+a[1:]
 for i in r:print w[:i]
 print ''
