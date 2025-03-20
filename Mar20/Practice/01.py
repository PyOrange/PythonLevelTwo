from types import MappingProxyType
from dis import dis
from unicodedata import name

'''
dict 예제
'''

d = {'k': 'v'}

d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)


d['k2'] = 'v2'

print(d)

print()
print()

s1 = {'a', 'b', 'c'}
s2 = frozenset({'a', 'b', 'a'})

for s1 in s1:
    if (s1.__len__() <= 10):
        s1.add('trash')
    else : 
        print("Full Enough")
        break

print(s1, type(s1))
print(s2, type(s2))

print('------')
print(dis('{10}'))

print('------')
print(dis('set([10])'))

print()
print()

print('------')

print({name(chr(i), '') for i in range(0,128)})
    