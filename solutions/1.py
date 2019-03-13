import re
def p(n):return re.match(r'^1?$|^(11+?)\1+$','1'*n)==None
for n in range(3,10**5-1,2):
 if p(n) and p(n+2):print(n,n+2)
