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
