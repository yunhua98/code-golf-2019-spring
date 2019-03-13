f=open('../inputs/2.txt')
for p in f:print(bin(int(p.split()[0])^int(p.split()[1])).count('1'))
