def a(x,y,w):
 for l in range(x,y):
  if w[l]>w[l+1]:return False
 return True
f=open('../inputs/3.txt')
for w in f:
 m=0
 s=""
 for j in range(len(w)):
  for i in range(j):
   if j-i<=m:continue
   if a(i,j,w):
    m=j-i
    s=w[i:j+1]
 print(s)
