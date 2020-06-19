#!/usr/bin/env python
print('Hello World !')
a = 'Hello'
b = 'World'
c = '!'
#+
print(a+' '+b+' '+c)
#%
print('%s %s %s'%(a,b,c))
#format
print('{} {} {}'.format(a,b,c))
#join
print(' '.join([a,b,c]))
#for
for i in range(1,10):
    print(i,end='')
print()
#while
i = 1
while i < 10:
    print(i,end='')
    i+=1
print()
#99 ChengFaBiao
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%d'%(i,j,i*j),end=' ')
    print()
